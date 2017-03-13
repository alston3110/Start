# -*- coding: utf8 -*-
# ----------------------------------------------------------------------

import os
import gtk
import gobject
import TestManual 
import TestAuto
import define
# ----------------------------------------------------------------------

class Dialog(gtk.Dialog):

    def __init__(self, parent, title, image, text):
        gtk.Dialog.__init__(self, title , None, 0, None)

	self.image = 0
	self.Index = 0
	self.Errcode = 0

        for i in MPManustatus:
            if i == 0:
            	self.Errcode = self.Errcode + 1
        for i in MPAutostatus:
            if i == 0:
            	self.Errcode = self.Errcode + 1

	self.set_default_size(150, 70)
        
        DialogBox = self.get_content_area()
                
        VBoxFrame = gtk.VBox(spacing=1)
        DialogBox.add(VBoxFrame)
        
        HBox = gtk.HBox(spacing=1)
        VBoxFrame.pack_start(HBox, False, False, 0)
        
        Label = gtk.Label()
        Label.set_markup(text)
        Label.set_width_chars(20)
        HBox.pack_start(Label, False, False, 0)

	for k in range(0,self.Errcode):
        	HBox = gtk.HBox(spacing=1)
        	VBoxFrame.pack_start(HBox, False, False, 0)
        	Button = gtk.Button()
        	HBox.pack_start(Button, False, False, 0)
        	Image = gtk.Image()
        	self.ErrCodeCheck()
        	Image.set_from_file(self.image)
        	Button.set_image(Image)
        self.show_all()
        
    def ErrCodeCheck(self):
	for j in range(self.Index,10):
		self.Index = j + 1
    		if j == 0:
    			if MPManustatus[0] == 0:
        			self.image = define.gImageE600
    				break
    		if j == 1:
    			if MPAutostatus[0] == 0:
        			self.image = define.gImageE610
    				break
    		if j == 2:
    			if MPAutostatus[1] == 0:
        			self.image = define.gImageE620
    				break
    		if j == 3:
    			if MPAutostatus[2] == 0:
        			self.image = define.gImageE630
    				break
    		if j == 4:
    			if MPAutostatus[3] == 0:
        			self.image = define.gImageE640
    				break
    		if j == 5:
    			if MPAutostatus[4] == 0:
        			self.image = define.gImageE650
    				break
    		if j == 6:
    			if MPAutostatus[5] == 0:
        			self.image = define.gImageE660
    				break
    		if j == 7:
    			if MPAutostatus[6] == 0:
        			self.image = define.gImageE670
    				break
    		if j == 8:
    			if MPAutostatus[7] == 0:
        			self.image = define.gImageE680
    				break
    		if j == 9:
    			if MPAutostatus[8] == 0:
        			self.image = define.gImageE690
    				break
    
    
