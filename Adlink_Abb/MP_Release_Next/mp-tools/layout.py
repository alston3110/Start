# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
import __builtin__
import gtk
import gobject

# ----------------------------------------------------------------------
import define

# ----------------------------------------------------------------------
class Layout:
    def __init__ (self, parent):
        
        self.parent = parent
        
        # VBoxFrame 
        VBoxFrame = gtk.VBox(spacing=6)
        #parent.add(VBoxFrame)
        self.parent.MainFrame.pack_start(VBoxFrame, False, False, 0)
        # vboxframe1 , rows
        functions = [
            self.Layout_ManualTitle ,
            self.Layout_Separator   ,
            self.Layout_ManualItem  ,
            self.Layout_Separator   ,
            self.Layout_AutoTitle   ,
            self.Layout_Separator   ,
            self.Layout_AutoItem1    ,
#            self.Layout_AutoItem2    ,
            self.Layout_Separator   ,
            self.Layout_InputSerialNumber,
            self.Layout_Separator   ,
            self.Layout_InputMACAddress1,
#            self.Layout_InputMACAddress2,
            self.Layout_Separator   ,
        ]
        for function in functions:
            hbox = gtk.HBox(spacing=2)
            VBoxFrame.pack_start(hbox, False, False, 0)
            function(hbox)

    def Layout_ManualTitle(self, hbox):
        label = gtk.Label()
        label.set_text( u"Manual Test Item" )
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(16)
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.parent.SysQuitButton, False, False, 0)

    def Layout_AutoTitle(self, hbox):
        label = gtk.Label()
        label.set_text( u"Auto Test Item" )
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(16)
        hbox.pack_start(label, True, True, 0)    

    def Layout_Separator(self, hbox):
        separator = gtk.HSeparator()
        hbox.pack_start(separator, True, True, 0)   

    def Layout_ManualItem(self, hbox):
        Items  = [ 
            MPManubuttons[0]    , 
#            MPManubuttons[1]    , 
#            MPManubuttons[2]    , 
            ]
        Images = [ 
            define.gImageDisplay     , 
#            define.gImageAudio       , 
#            define.gImageMedia       , 
            ]
        Index = 0
        for Item in Items:
            Image = gtk.Image()
            Image.set_from_file(Images[Index])
            Item.put(Image,0,0)
            hbox.pack_start(Item, False, False, 0)
            Index = Index + 1

    def Layout_AutoItem1(self, hbox):
        Items  = [ 
            MPAutobuttons[0]    , 
            MPAutobuttons[1]    , 
            MPAutobuttons[2]    , 
            MPAutobuttons[3]    ,
            MPAutobuttons[4]    , 
            MPAutobuttons[5]    , 
            MPAutobuttons[6]    , 
            MPAutobuttons[7]    , 
            ]
        Images = [ 
            define.gImagemicroSD        , 
            define.gImageStorage1   , 
            define.gImageStorage2   , 
            define.gImageEthernet1  , 
            define.gImageWifi , 
            define.gImageCanbus	   ,
            define.gImageRTC	    ,
            define.gImageBSP	    ,
            ]
        Index = 0
        for Item in Items:
            Image = gtk.Image()
            Image.set_from_file(Images[Index])
            Item.put(Image,0,0)
            hbox.pack_start(Item, False, False, 0)
            Index = Index + 1

    def Layout_AutoItem2(self, hbox):
        Items  = [ 
            MPAutobuttons[4]    , 
            MPAutobuttons[5]    , 
            MPAutobuttons[6]    , 
            MPAutobuttons[7]    , 
            MPAutobuttons[8]    , 
            MPAutobuttons[9]    , 
            MPAutobuttons[10]    , 
            MPAutobuttons[11]    , 
            MPAutobuttons[12]    ,
            MPAutobuttons[13]    ,
            ]
        Images = [ 
            define.gImageEthernet0  , 
            define.gImageEthernet1  , 
            define.gImageWifi , 
            define.gImageBluetooth , 
            define.gImageUart1      , 
            define.gImageUart2  , 
            define.gImageUart5      , 
            define.gImageCanbus	   ,
            define.gImageSpi  , 
            define.gImageI2cbus  ,
            ]
        Index = 0
        for Item in Items:
            Image = gtk.Image()
            Image.set_from_file(Images[Index])
            Item.put(Image,0,0)
            hbox.pack_start(Item, False, False, 0)
            Index = Index + 1

    def Layout_InputSerialNumber(self, hbox):
        # column 1 , Label
        label = gtk.Label()
        label.set_text("Serial Number")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(16)
        hbox.pack_start(label, False, False, 0)
        
        # column 2 , entry
        MPInputEntrys[0].set_text("")
        MPInputEntrys[0].set_max_length(define.gSerialNumberMaxLength)
        MPInputEntrys[0].set_editable(False)
        hbox.pack_start(MPInputEntrys[0], True, True, 0)   

    def Layout_InputMACAddress1(self, hbox):
        # column 1 , Label
        label = gtk.Label()
        label.set_text("Mac1 Address")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(16)
        hbox.pack_start(label, False, False, 0)

        # column 2 , entry
        MPInputEntrys[1].set_text("")
        MPInputEntrys[1].set_max_length(define.gMacAddressMaxLength)
        MPInputEntrys[1].set_editable(False)
        hbox.pack_start(MPInputEntrys[1], True, True, 0)

    def Layout_InputMACAddress2(self, hbox):
        # column 1 , Label
        label = gtk.Label()
        label.set_text("Mac2 Address")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(16)
        hbox.pack_start(label, False, False, 0)

        # column 2 , entry
        MPInputEntrys[2].set_text("")
        MPInputEntrys[2].set_max_length(define.gMacAddressMaxLength)
        MPInputEntrys[2].set_editable(False)
        hbox.pack_start(MPInputEntrys[2], True, True, 0)

