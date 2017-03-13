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

        Button = gtk.Button("Quit")
        #HBox.pack_start(Button, True, True, 0)
        Image = gtk.Image()
        Button.connect( "clicked", self.TestQuit)

        Response = 0
        Response = os.system("./tools/mp_3g info >> " +  files[1] )
        if Response == 256:
            Button = gtk.Button("Test 3G")
            HBox.pack_start(Button, True, True, 0)
            Button.connect( "clicked", self.Test3g)
        self.show_all()

    def run(self):
        result = super(Dialog, self).run()

        if result == gtk.RESPONSE_NONE :
            gtk.main_quit()
        return result

    def TestPass(self,button):
        self.response(gtk.RESPONSE_OK)

    def TestFail(self,button):
        self.response(gtk.RESPONSE_CANCEL)

    def Test3g(self,button):
        self.response(gtk.RESPONSE_YES)

    def TestQuit(self,button):
        self.response(gtk.RESPONSE_NONE)
