# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
from array import *
from collections import namedtuple

# ----------------------------------------------------------------------
import os
import sys
import logging
import datetime
import __builtin__
import gtk
import gobject

# ----------------------------------------------------------------------
sys.path.append('./test')

import define
import TestManual 
import TestAuto
import dialog_result
import dialog_errorcode
# ----------------------------------------------------------------------
class State:
    def __init__ (self, parent):
        self.parent = parent
        
        self.Status       = 0
        self.Count        = 0
        self.ManualProc   = TestManual.Test(parent=self,root=parent)
        self.AutoProc     = TestAuto.Test(parent=self,root=parent)

    # ------------------------------------------------------------------
    # Run time function        
    def RunTimeProc(self):
        StateProcs = {
            0 : self.RunManualTest,
            1 : self.RunAutoTest,
            2 : self.RunEFM32Test,
            3 : self.RunBSPTest,
            4 : self.RunShowResult,
            5 : self.RunSerialNumber,
            6 : self.RunMac1Address,
#            6 : self.RunMac2Address,
            7 : self.RunReportTest,
            8 : self.RunNullTest,
        }
        logging.info("RunTimeProc...%s" , StateProcs[self.Status])
        if MPAllstatus[0] == 1:
            self.Status=8
            
        if StateProcs[self.Status]() == False:
            return False
                     
        return True

    # ------------------------------------------------------------------
    def RunManualTest(self):
        # goto RunAutoTest
        if self.ManualProc.RunTimeCallBack() == False:
            self.Status = self.Status + 1
            return True

    def RunAutoTest(self):
        if self.AutoProc.RunTimeCallBack() == False:
            self.Status = self.Status + 1
            return True

    def RunEFM32Test(self):
        print "------MCUVer Test------"
        Response = 0
        Response = os.system("./tools/mp_mcuver >> " +  files[1] )
        print "Result=", Response

        Image = MPAutobuttons[6].get_children()[0]
        if Response == 512:
            MPAutostatus[6] = 1
            Image.set_from_file(define.gImageRTCOK)
        elif Response == 256:
            MPAutostatus[6] = 0
            Image.set_from_file(define.gImageRTCFail)
        elif Response == 0:
            MPAutostatus[6] = 0
            Image.set_from_file(define.gImageRTCFail)

        self.Status = self.Status + 1
        return True

    def RunBSPTest(self):
        print "------BSPVer Test------"
        Response = 0
        Response = os.system("./tools/mp_bspver >> " +  files[1] )
        print "Result=", Response

        Image = MPAutobuttons[7].get_children()[0]
        if Response == 256:
            MPAutostatus[7] = 1
            Image.set_from_file(define.gImageBSPOK)
        elif Response == 512:
            MPAutostatus[7] = 0
            Image.set_from_file(define.gImageBSPFail)
        elif Response == 0:
            MPAutostatus[7] = 0
            Image.set_from_file(define.gImageBSPFail)

        self.Status = self.Status + 1
        return True
        
    def RunShowResult(self):
        fopw=open("mp_result.log","w")

        if MPManustatus[0] == 1:
            fopw.write("Display +++++ Pass\n")
        else: 
            fopw.write("Display -------- Fail\n")

        if MPAutostatus[0] == 1:
            fopw.write("SDCARD ++++++ Pass\n")
        else:
            fopw.write("SDCARD --------- Fail\n")
        
        if MPAutostatus[1] == 1:
            fopw.write("USB1 ++++++++ Pass\n")
        else:
            fopw.write("USB1 ----------- Fail\n")

        if MPAutostatus[2] == 1:
            fopw.write("USB2 ++++++++ Pass\n")
        else:
            fopw.write("USB2 ----------- Fail\n")
                    
        if MPAutostatus[3] == 1:
            fopw.write("Ethernet0 +++ Pass\n")
        else:
            fopw.write("Ethernet0 ------ Fail\n")

        if MPAutostatus[4] == 1:
            fopw.write("Wifi ++++++++ Pass\n")
        else:
            fopw.write("Wifi ----------- Fail\n")

        if MPAutostatus[5] == 1:
            fopw.write("Canbus +++++ Pass\n")
        else:
            fopw.write("Canbus ---- Fail\n")
 
        if MPAutostatus[6] == 1:
            fopw.write("MCU +++++++ Pass\n")
        else:
            fopw.write("MCU ---------- Fail\n")

        if MPAutostatus[7] == 1:
            fopw.write("BSP +++++++ Pass\n")
        else:
            fopw.write("BSP ---------- Fail\n")
               
        fopw.close()
        test_result = 1
        
        for i in MPManustatus:
            test_result &= i
            
        for i in MPAutostatus:
            test_result &= i

        if test_result == 1:
            Dialog = dialog_result.Dialog(self, "test result", define.gImageAllOK, "<b><big>Test Result :</big></b>" )
            Dialog.move(260,500)
        else:
            Dialog = dialog_errorcode.Dialog(self, "test result", define.gImageE600, "<b><big>Error Code :</big></b>" ) 
            Dialog.move(650,210)
        
        
        
        self.Status = self.Status + 1
        
        return True

    def RunSerialNumber(self):
        if self.Count == 0:
            MPInputEntrys[0].grab_focus()
            MPInputEntrys[0].set_editable(True)
            self.Count = self.Count + 1
        else:
            if MPInputEntrys[0].get_text_length() == define.gSerialNumberMaxLength:
                MPInputEntrys[0].set_editable(False)
                self.Status = self.Status + 1
                self.Count = 0
                line = "./tools/rtx_setting -write serialno %s mp " % MPInputEntrys[0].get_text()
                Response = os.system(line)
        MPInputstatus[0] = 1
        return True

    def RunMac1Address(self):
        if self.Count == 0:
            MPInputEntrys[1].grab_focus()
            MPInputEntrys[1].set_editable(True)
            self.Count = self.Count + 1
        else:
            if MPInputEntrys[1].get_text_length() == define.gMacAddressMaxLength:
                MPInputEntrys[1].set_editable(False)
                self.Status = self.Status + 1
                self.Count = 0
                line = "./tools/rtx_setting -write mac 0 %s mp " % MPInputEntrys[1].get_text()
                Response = os.system(line)
		MPInputstatus[1] = 1
        return True

    def RunMac2Address(self):
        if self.Count == 0:
            MPInputEntrys[2].grab_focus()
            MPInputEntrys[2].set_editable(True)
            self.Count = self.Count + 1
        else:
            if MPInputEntrys[2].get_text_length() == define.gMacAddressMaxLength:
                MPInputEntrys[2].set_editable(False)
                self.Status = self.Status + 1
                self.Count = 0
                line = "./tools/rtx_setting -write mac 1 %s mp" % MPInputEntrys[2].get_text()
                Response = os.system(line)
		MPInputstatus[2] = 1
        return True

    def RunReportTest(self):
        if MPInputstatus[0] == 1:
            line = MPInputEntrys[0].get_text() + "_" + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + ".log"
        else:
            line = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S') + ".log"

        files.append(line)
        fopw=open(line,"w")

        if MPManustatus[0] == 1:
            fopw.write("Display +++++ Pass\n")
        else: 
            fopw.write("Display -------- Fail\n")

        if MPAutostatus[0] == 1:
            fopw.write("SDCARD ++++++ Pass\n")
        else:
            fopw.write("SDCARD --------- Fail\n")
        
        if MPAutostatus[1] == 1:
            fopw.write("USB1 ++++++++ Pass\n")
        else:
            fopw.write("USB1 ----------- Fail\n")

        if MPAutostatus[2] == 1:
            fopw.write("USB2 ++++++++ Pass\n")
        else:
            fopw.write("USB2 ----------- Fail\n")
                    
        if MPAutostatus[3] == 1:
            fopw.write("Ethernet0 +++ Pass\n")
        else:
            fopw.write("Ethernet0 ------ Fail\n")

        if MPAutostatus[4] == 1:
            fopw.write("Wifi ++++++++ Pass\n")
        else:
            fopw.write("Wifi ----------- Fail\n")

        if MPAutostatus[5] == 1:
            fopw.write("Canbus +++++ Pass\n")
        else:
            fopw.write("Canbus ---- Fail\n")
 
        if MPAutostatus[6] == 1:
            fopw.write("MCU +++++++ Pass\n")
        else:
            fopw.write("MCU ---------- Fail\n")

        if MPAutostatus[7] == 1:
            fopw.write("BSP +++++++ Pass\n")
        else:
            fopw.write("BSP ---------- Fail\n")
            
        fopw.close()
        self.Status = self.Status + 1
        
        test_result = 1
        
	line = "./tools/mp_save %s" % line
        Response = os.system(line) 

        for i in MPManustatus:
            test_result &= i
            
        for i in MPAutostatus:
            test_result &= i

        for i in MPInputstatus:
            test_result &= i

        if test_result == 1:
            Dialog = dialog_result.Dialog(self, "test finish", define.gImageAllPASS, "<b><big>Test Finish :</big></b>" )
        else:
            Dialog = dialog_result.Dialog(self, "test finish", define.gImageAllFAIL, "<b><big>Test Finish :</big></b>" )            
        Dialog.move(260,500)
        
        return True
        
    def RunNullTest(self):
        return True

