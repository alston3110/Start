# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
import os
import logging
import __builtin__
import gtk
import gobject

# ----------------------------------------------------------------------
import define
import dialog
import dialog_3g
import dialog_result
# ----------------------------------------------------------------------
class Test:
    def __init__ (self, parent,root):
        self.parent = parent
        self.rootparent = root
        self.Status       = 0
        self.Count        = 0
        self.DialogLocX   = 260
        self.DialogLocY   = 500
        
    # ------------------------------------------------------------------
    # Run time function
    def RunTimeCallBack(self):
        StateProcs = {
            0 : self.RunDispayTest,
#            1 : self.RunAudioTest,
#            2 : self.RunMediaTest,
            1 : self.RunExit,
        }
        
        logging.info("TestManual=======RunTimeCallBack...%s" , StateProcs[self.Status])
        return StateProcs[self.Status]()

    # ------------------------------------------------------------------
    def RunDispayTest(self):
        self.rootparent.Player.Play()
#        os.system("./tools/mp_lvds1 >> " +  files[1])
        Dialog = dialog.Dialog(self, "Display test...", define.gImageDisplay, "Display test..." )
        Dialog.move(self.DialogLocX,self.DialogLocY)
        Response = Dialog.run()
        self.rootparent.Player.Stop()
        Dialog.destroy()
        
        Image = MPManubuttons[self.Status].get_children()[0]
        if Response == gtk.RESPONSE_OK:
            MPManustatus[self.Status] = 1
            Image.set_from_file(define.gImageDisplayOK)
        elif Response == gtk.RESPONSE_CANCEL:
            MPManustatus[self.Status] = 0
            Image.set_from_file(define.gImageDisplayFail)
        
        self.Status = self.Status + 1
        return True  

    def RunAudioTest(self):
        os.system("./tools/mp_mic >> " +  files[1] + " &")
        Dialog = dialog.Dialog(self, "AUDIO test...", define.gImageAudio, "AUDIO test..." )
        Dialog.move(self.DialogLocX,self.DialogLocY)
        Response = Dialog.run()

        Image = MPManubuttons[self.Status].get_children()[0]
        if Response == gtk.RESPONSE_OK:
            MPManustatus[self.Status] = 1
            Image.set_from_file(define.gImageAudioOK)
        elif Response == gtk.RESPONSE_CANCEL:
            MPManustatus[self.Status] = 0
            Image.set_from_file(define.gImageAudioFail)
            
        os.system("rm /run/lock/aplay.pid")
        Dialog.destroy()
        self.Status = self.Status + 1
        return True  

    def RunMediaTest(self):
        os.system("./tools/player &")
        Dialog = dialog.Dialog(self, "Gpu test...", define.gImageMedia, "Gpu test..." )
        Dialog.move(self.DialogLocX,self.DialogLocY)
        Response = Dialog.run()

        Image = MPManubuttons[self.Status].get_children()[0]
        if Response == gtk.RESPONSE_OK:
            MPManustatus[self.Status] = 1
            Image.set_from_file(define.gImageMediaOK)
        elif Response == gtk.RESPONSE_CANCEL:
            MPManustatus[self.Status] = 0
            Image.set_from_file(define.gImageMediaFail)

        Dialog.destroy()
        self.Status = self.Status + 1
        
        os.system("killall -2 player")
        return True  

    def RunExit(self):
        return False


