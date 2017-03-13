# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
import os
import gtk
import gobject

# ----------------------------------------------------------------------
import define
import struct  
import fcntl, struct, glob

RTC_RD_TIME=0x80247009
rtcList = glob.glob('/dev/rtc[0-9]')


class Dialog(gtk.Dialog):

    def __init__(self, parent, title, image, text):
        gtk.Dialog.__init__(self, title , None, 0, None)

        self.set_default_size(150, 100)
        self.set_default_response(gtk.RESPONSE_CANCEL)

        DialogBox = self.get_content_area()
        
        VBoxFrame = gtk.VBox(spacing=6)
        DialogBox.add(VBoxFrame)
        
        HBox = gtk.HBox(spacing=2)
        VBoxFrame.pack_start(HBox, False, False, 0)
        
        Label = gtk.Label(text)
        Label.set_width_chars(32)
        HBox.pack_start(Label, False, False, 0)

        Button = gtk.Button()
        HBox.pack_start(Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(image)
        Button.set_image(Image)
        Button.set_sensitive(False)
		
        self.Label = gtk.Label(" x=0,y=0")
        self.Label.set_width_chars(32)
        HBox.pack_start(self.Label, False, False, 0)
        
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
        self.x = rtcList 
        self.y = 0

        #reate Timer for run time functions , about 200 ms
        gobject.timeout_add( 1000 , self.RunTimeCallBack )

    def RunTimeCallBack(self):
        a=struct.pack('iiiiiiiii', 0,0,0,0,0,0,0,0,0)
        fo=open(rtcList)
        input=fcntl.ioctl(fo.fileno(), RTC_RD_TIME, a)
        result=struct.unpack('iiiiiiiii', input)
        self.y = 0
        #self.y = "str(1900+result[5])+ "-" + str(1+result[4])"

 
#+ "-" + str(1+result[4]) + "-" + str(result[3]) + " " + str(result[2]) + ":" + str(result[1]) + ":" + str(result[0])  
#	in_file = open ("/dev/input/event1","rb")
#	event = in_file.read(16)
#	fmt = 'iihhi'
#	num = 0
#	while event:
#		(time1,time2, type, code, value) = \
#			struct.unpack(fmt,event)
#		if type == 2 or type == 3:
#			if code == 0:
#				self.x = value
#				num = num + 1
#			if code == 1:
#				self.y = value
#				num = num + 1
#			if code == 2:
#				self.z = value
#				num = num + 1
#		event = in_file.read(16)
#		if num >= 3 :
#			break
        fo.close()
        show_str = "x:%s y:%d " %(self.x,self.y,) 
        self.Label.set_text( show_str )        

        return True


    def run(self):
        result = super(Dialog, self).run()
        if result != gtk.RESPONSE_OK:
			return gtk.RESPONSE_CANCEL
        return result

    def TestPass(self,button):
        self.response(gtk.RESPONSE_OK)

    def TestFail(self,button):
        self.response(gtk.RESPONSE_CANCEL)
