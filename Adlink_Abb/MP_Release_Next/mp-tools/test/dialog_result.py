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

        self.set_default_size(250, 150)
        DialogBox = self.get_content_area()
        
        VBoxFrame = gtk.VBox(spacing=6)
        DialogBox.add(VBoxFrame)
        
        HBox = gtk.HBox(spacing=2)
        VBoxFrame.pack_start(HBox, False, False, 0)
        
        Label = gtk.Label()
        Label.set_markup(text)
        Label.set_width_chars(20)
        HBox.pack_start(Label, False, False, 0)

        Button = gtk.Button()
        HBox.pack_start(Button, False, False, 0)
        Image = gtk.Image()
        Image.set_from_file(image)
        Button.set_image(Image)
#        Button.set_sensitive(False)
		
        self.show_all()
