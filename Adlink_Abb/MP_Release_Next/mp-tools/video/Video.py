#!/usr/bin/env python
# -*- coding: utf8 -*-

import shlex, subprocess
import sys
import os
import time
import gtk
import gobject

def Init():
    return
    Gst.init(None) 


class Main:
    def __init__ ( self , filename , fb="/dev/fb0" , x=0 , y=0 , width=512 , height=256 , rotate=0 ) :
        return
        self.GstPlayer = Gst.ElementFactory.make( "playbin" , "player" )
        if not self.GstPlayer:
            print("[gstreamer] Not all elements could be created.")
            exit(-1)
        
        # --------------------------------------------------------------
        GstBus = self.GstPlayer.get_bus()
        GstBus.add_signal_watch()
        GstBus.enable_sync_message_emission()
        
        #used to get messages that GStreamer emits
        GstBus.connect("message", self.GstPlayer_OnMessage)
        
        #used for connecting video to your application
        GstBus.connect("sync-message::element",self.GstPlayer_OnSyncMessage)
        
        # --------------------------------------------------------------
        self.MediaFileName = "file://" + filename
        self.GstPlayer.set_property("uri", self.MediaFileName )
        
        self.GstSink = Gst.ElementFactory.make( "imxg2dvideosink" , "videosink" )
        if not self.GstSink:
            print("[gstreamer] Not all elements could be created.")
            exit(-1)
        
        self.GstPlayer.set_property("video-sink", self.GstSink )
        self.GstPlayer.set_property("flags", 0x57 )
        self.GstPlayer.set_property("force-aspect-ratio", True )
        
        self.GstSink.set_property( "framebuffer"     , fb )
        self.GstSink.set_property( "window-x-coord"  , x )
        self.GstSink.set_property( "window-y-coord"  , y )
        self.GstSink.set_property( "window-width"    , width )
        self.GstSink.set_property( "window-height"   , height )
        self.GstSink.set_property( "output-rotation" , rotate )
        self.GstSink.set_property( "force-aspect-ratio" , True )

    def RePlay( self ) :
        return
        self.GstPlayer.set_property("uri", self.MediaFileName )
        ret = self.GstPlayer.set_state( Gst.State.PLAYING )
        if ret == Gst.StateChangeReturn.FAILURE :
            print("Unable to set the pipeline to the playing state.")

    # ------------------------------------------------------------------
    def GstPlayer_OnMessage( self, bus , message):
        return
        Type      = message.type
        GstPlayer = message.src
        if Type == Gst.MessageType.EOS:
            # End of Stream
            GstPlayer.set_state(Gst.State.NULL)
            self.RePlay()
        elif Type == Gst.MessageType.ERROR:
            GstPlayer.set_state(Gst.State.NULL) 

    # Gst sync message 
    def GstPlayer_OnSyncMessage(self, bus, message):
        return
        Structure = message.get_structure()
        if Structure is None:
            return False
        print("%s"%Structure.get_name())
        #if Structure.get_name() == "prepare-window-handle":
        #    WinID = self.MediaWindow.get_property('window').get_xid()
        #    imagesink = message.src
        #    imagesink.set_property("force-aspect-ratio", True)

    # ------------------------------------------------------------------
    def Play( self ) :
        return
        # play video
        ret = self.GstPlayer.set_state( Gst.State.PLAYING )
        if ret == Gst.StateChangeReturn.FAILURE :
            print("Unable to set the pipeline to the playing state.")
            exit(-1)

    def Stop( self ) :
        return
        self.GstPlayer.set_state( Gst.State.NULL )
