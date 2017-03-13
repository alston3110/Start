#!/usr/bin/env python
# -*- coding: utf8 -*-

import Video
import gtk
import gobject

class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.set_title("MP-tools")
        #Gtk.Window.__init__(self, title="MP-tools")
        self.set_border_width(10)
        
        self.Player    = Video.Main("/home/rtx/ttttt.mp4" , fb="/dev/fb0" , x=0 , y=0 , width=512 , height=256 , rotate=0 )
        self.Player.Play()
        

gobject.threads_init()
Video.Init()

win = MainWindow()
win.connect("delete-event", gtk.main_quit)
win.show_all()
win.move(800,0)
#win.maximize()
win.set_default_size(10,480)
win.resize(100, 480)

gtk.main()
