# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
import logging
import socket
import gtk
import gobject

class NetWork:
    def __init__ ( self , parent , drawarea ):
        logging.info( 'New Network class & Initial' )
        self.Parent = parent
        self.DrawArea = drawarea
        self.HostName = socket.gethostname( )
        self.Set_Layout( parent )

    def Set_Layout( self , parent ):
        label = gtk.Label()
        label.set_text( "Host Name : " + self.HostName + "\ntest")
        label.set_justify(gtk.JUSTIFY_LEFT)
        self.DrawArea.pack_start(label, False, False, 0)
 
