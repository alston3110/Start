# -*- coding: utf8 -*-
# ----------------------------------------------------------------------

import os
import gtk
import gobject

# ----------------------------------------------------------------------
import define

class Dialog(gtk.Dialog):

    def __init__(self, parent, title, image, text):
        gtk.Dialog.__init__(self, title , None, 0, None)
        self.isRun = 1
        self.set_default_size(150, 100)
        self.set_default_response(gtk.RESPONSE_CANCEL)

        DialogBox = self.get_content_area()
        
        VBoxFrame = gtk.VBox(spacing=6)
        DialogBox.add(VBoxFrame)
        
        HBox = gtk.HBox(spacing=2)
        VBoxFrame.pack_start(HBox, False, False, 0)
        #------------------------------
        self.Dip1Button = gtk.Button()
        HBox.pack_start(self.Dip1Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageDipSwOn)
        self.Dip1Button.set_image(Image)
        self.Dip1Button.set_sensitive(False)
        
        self.Dip2Button = gtk.Button()
        HBox.pack_start(self.Dip2Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageDipSwOn)
        self.Dip2Button.set_image(Image)
        self.Dip2Button.set_sensitive(False)
 
        self.Dip3Button = gtk.Button()
        HBox.pack_start(self.Dip3Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageDipSwOn)
        self.Dip3Button.set_image(Image)
        self.Dip3Button.set_sensitive(False)

        self.Dip4Button = gtk.Button()
        HBox.pack_start(self.Dip4Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageDipSwOn)
        self.Dip4Button.set_image(Image)
        self.Dip4Button.set_sensitive(False)
        # -------------------     		
        Label = gtk.Label(text)
        Label.set_width_chars(32)
        HBox.pack_start(Label, False, False, 0)

        HBox = gtk.HBox(spacing=2)
        VBoxFrame.pack_start(HBox, False, False, 0)        
        Button = gtk.Button()
        HBox.pack_start(Button, True, True, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageOK)
        Button.set_image(Image)
        Button.connect( "clicked", self.TestPass)

        Button = gtk.Button()
        HBox.pack_start(Button, True, True, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageFail)
        Button.set_image(Image)
        Button.connect( "clicked", self.TestFail)

        self.show_all()
        # start timer , 20 ms
        GObject.timeout_add(100,self.RunTimeCallBack)

    def run(self):
        result = super(Dialog, self).run()
        if result != gtk.RESPONSE_OK:
			return gtk.RESPONSE_CANCEL
        return result

    def TestPass(self,button):
        self.isRun = 0
        self.response(gtk.RESPONSE_OK)

    def TestFail(self,button):
        self.isRun = 0 
        self.response(gtk.RESPONSE_CANCEL)
        
    # ------------------------------------------------------------------
    # Run time function
    def RunTimeCallBack(self):
        Index = 0
        Gpios = ['75','76','69','70']
        DipValue = ["0" , "1" , "0" ,  "1"]

        if self.isRun == 0:
            return True
        for Gpio in Gpios:
            DipFP = open("/sys/class/gpio/gpio" + Gpio + "/value","r")
            DipValue[Index] = DipFP.read()
            DipFP.close()
            Index=Index+1

        #dip1 = open("/sys/class/gpio/gpio75/value","r")
        #dip2 = open("/sys/class/gpio/gpio76/value","r")
        #dip3 = open("/sys/class/gpio/gpio69/value","r")
        #dip4 = open("/sys/class/gpio/gpio70/value","r")
        #dip1value = dip1.read()
        #dip2value = dip2.read()
        #dip3value = dip3.read()
        #dip4value = dip4.read()
        #dip1.close()
        #dip2.close()
        #dip3.close()
        #dip4.close()
        #dip1value='0'
        #dip2value='1'
        #dip3value='1'
        #dip4value='0'
        Image = gtk.Image()
        if DipValue[0][0]=='1':
            Image.set_from_file(define.gImageDipSwOn)
        else:
            Image.set_from_file(define.gImageDipSwOff)
        self.Dip1Button.set_image(Image)

        Image = gtk.Image()
        if DipValue[1][0]=='1':
            Image.set_from_file(define.gImageDipSwOn)
        else:
            Image.set_from_file(define.gImageDipSwOff)
        self.Dip2Button.set_image(Image)

        Image = gtk.Image()
        if DipValue[2][0]=='1':
            Image.set_from_file(define.gImageDipSwOn)
        else:
            Image.set_from_file(define.gImageDipSwOff)
        self.Dip3Button.set_image(Image)

        Image = gtk.Image()
        if DipValue[3][0]=='1':
            Image.set_from_file(define.gImageDipSwOn)
        else:
            Image.set_from_file(define.gImageDipSwOff)
        self.Dip4Button.set_image(Image)
        return True
