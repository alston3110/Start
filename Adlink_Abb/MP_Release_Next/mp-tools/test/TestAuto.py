# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
import os
import logging
import __builtin__
import gtk
import gobject

# ----------------------------------------------------------------------
import define
import dialog
import dialogdipsw
import dialog_rs485

# ----------------------------------------------------------------------
class Test:
    def __init__ (self, parent,root):
        self.parent = parent
        self.rootparent = root
        self.Status       = 0
        self.Count        = 0

    # ------------------------------------------------------------------
    # Run time function
    def RunTimeCallBack(self):
        StateProcs = {
            0 : self.RunSDTest,
            1 : self.RunStorage1Test,
            2 : self.RunStorage2Test,
            3 : self.RunEth0Test,
            4 : self.RunWifiTest,
            5 : self.RunCanbusTest,
            6 : self.RunExit,
        }

        logging.info("TestAuto=======RunTimeCallBack...%s" , StateProcs[self.Status])
        return StateProcs[self.Status]()
#        return True

    # ------------------------------------------------------------------
    def RunAutoTest(self):
#        os.system("./tools/mp_uart 1 >> " +  files[1] + " &")
#        os.system("./tools/mp_uart 2 >> " +  files[1] + " &")
#        os.system("./tools/mp_uart 5 >> " +  files[1] + " &")
        os.system("./tools/mp_wifi >> " +  files[1] + " &")
#        os.system("./tools/mp_bt >> " +  files[1] + " &")
        os.system("./tools/mp_eth >> " +  files[1] + " &")
        os.system("./tools/mp_canbus_client >> " +  files[1] + " &")
#        os.system("./tools/mp_spibus >> " +  files[1] + " &")
#        os.system("./tools/mp_i2cbus >> " +  files[1] + " &")
        print "------Auto Test------"
        return True

    def RunSDTest(self):
        if self.Count == 0:
            print "------SD Test------"
            Response = 0
            Response = os.system("./tools/mp_sdcard mmcblk1p1>> " +  files[1] )
            print "Result=", Response
            Image = MPAutobuttons[self.Status].get_children()[0]
        	#if return 1/2, python will recognize as 256/512
            if Response == 256:
                MPAutostatus[self.Status] = 1
                Image.set_from_file(define.gImagemicroSDOK)
            elif Response == 0:
                MPAutostatus[self.Status] = 0
                Image.set_from_file(define.gImagemicroSDFail)

            self.Count = self.Count + 1
        else:
            self.Status = self.Status + 1
       	return True

    def RunStorage1Test(self):
        if self.Count == 1:
            print "------USB1 Test------"
            Response = 0
            Response = os.system("./tools/mp_usb1 >> " +  files[1] )
            print "Result=", Response
            Image = MPAutobuttons[self.Status].get_children()[0]
            if Response == 256:
                MPAutostatus[self.Status] = 1
                Image.set_from_file(define.gImageStorage1OK)
            elif Response == 0:
                MPAutostatus[self.Status] = 0
                Image.set_from_file(define.gImageStorage1Fail)

            self.Count = self.Count + 1
        else:
            self.Status = self.Status + 1
        return True

    def RunStorage2Test(self):
        if self.Count == 2:
            print "------USB2 Test------"
            Response = 0
            Response = os.system("./tools/mp_usb2 >> " +  files[1] )
            print "Result=", Response
            Image = MPAutobuttons[self.Status].get_children()[0]
            if Response == 256:
                MPAutostatus[self.Status] = 1
                Image.set_from_file(define.gImageStorage2OK)
            elif Response == 0:
                MPAutostatus[self.Status] = 0
                Image.set_from_file(define.gImageStorage2Fail)

            self.Count = self.Count + 1
        else:
            self.Status = self.Status + 1
        return True
        
    def RunEth0Test(self):
        if self.Count == 3:
            print "------ETHERNET0 Test------"
            Response = 0
            Response = os.system("./tools/mp_eth eth0 >> " +  files[1] )
            print "Result=", Response        	
            Image = MPAutobuttons[self.Count].get_children()[0]
            if Response == 256:
                MPAutostatus[self.Count] = 1
                Image.set_from_file(define.gImageEthernet0OK)
            elif Response == 0:
                MPAutostatus[self.Count] = 0
                Image.set_from_file(define.gImageEthernet0Fail)
                
            self.Count = self.Count + 1
        else:
            self.Status = self.Status + 1
        return True
	
    def RunWifiTest(self):
        if self.Count == 4:
            print "------WIFI Test------"
            Response = 0
            Response = os.system("./tools/mp_wifi >> " +  files[1] )
            print "Result=", Response        	
            Image = MPAutobuttons[self.Count].get_children()[0]
            if Response == 256:
                MPAutostatus[self.Count] = 1
                Image.set_from_file(define.gImageWifiOK)
            elif Response == 0:
                MPAutostatus[self.Count] = 0
                Image.set_from_file(define.gImageWifiFail)
                
            self.Count = self.Count + 1
        else:
            self.Status = self.Status + 1
        return True	

    def RunCanbusTest(self):
        if self.Count == 5:
            print "------Canbus Test------"
            Response = 0
            Response = os.system("./tools/mp_canbus_client >> " +  files[1] )
            print "Result=", Response        	
            Image = MPAutobuttons[self.Count].get_children()[0]
            if Response == 256:
                MPAutostatus[self.Count] = 1
                Image.set_from_file(define.gImageCanbusOK)
            elif Response == 0:
                MPAutostatus[self.Count] = 0
                Image.set_from_file(define.gImageCanbusFail)
                
            self.Count = self.Count + 1
        else:
            self.Status = self.Status + 1
        return True

    def RunExit(self):
        return False



