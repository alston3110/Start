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

        self.set_default_size(150, 100)
        self.set_default_response(gtk.RESPONSE_CANCEL)

        DialogBox = self.get_content_area()
        
        VBoxFrame = gtk.VBox(spacing=6)
        DialogBox.add(VBoxFrame)
        
        HBox = gtk.HBox(spacing=2)
        VBoxFrame.pack_start(HBox, False, False, 0)

        Button = gtk.Button()
        HBox.pack_start(Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(image)
        Button.set_image(Image)
        Button.set_sensitive(False)
		
        Label = gtk.Label(text)
        Label.set_markup(text)
        Label.set_width_chars(32)
        HBox.pack_start(Label, False, False, 0)

        HBox = gtk.Box(spacing=2)
        VBoxFrame.pack_start(HBox, False, False, 0)        
        Button = gtk.Button()
        HBox.pack_start(Button, True, True, 0)
        Image = gtk.Image()
        Image.set_from_file(define.gImageenter)
        Button.set_image(Image)
        Button.connect( "clicked", self.ContinueTest)

        self.show_all()
    def run(self):
        result = super(Dialog, self).run()
        return result

    def ContinueTest(self,button):
        Response = 0
        Response = os.system("./tools/mp_uart_rs485 client >> " +  files[1] )
        if Response == 256:
            self.response(gtk.RESPONSE_OK)
        else :
            self.response(gtk.RESPONSE_NONE)
            
    def TestQuit(self,button):
        self.response(gtk.RESPONSE_NONE)
