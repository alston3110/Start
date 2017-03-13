#!/usr/bin/env python
# -*- coding: utf8 -*-
# ----------------------------------------------------------------------
import os
import sys
import logging
import __builtin__
import gtk
import gobject

sys.path.append('./lib')
sys.path.append('./network')
sys.path.append('./video')
sys.path.append('./gpu')
sys.path.append('./audio')

# ----------------------------------------------------------------------
import define
import Info
import layout
import state
#import network
import Video
import Audio
import Gpu
import inspect

# - Initial ------------------------------------------------------------
__builtin__.MPAllstatus = []

__builtin__.MPManubuttons = []
__builtin__.MPManustatus = []

__builtin__.MPAutobuttons = []
__builtin__.MPAutostatus = []
__builtin__.MPtestcheck = []

__builtin__.MPInputEntrys = []
__builtin__.MPInputstatus = []

__builtin__.files = []
files.append("mp-tools.log")
files.append("debug.log")

# - Main Windows class -------------------------------------------------
class MainWindow(gtk.Window):

    def __init__(self):       
        super(MainWindow,self).__init__()
        file = open('tools/info_config', 'r')
        mpver = file.read(20)
        file.close()
        self.set_title(mpver)
        self.set_border_width(10)
        #self.connect("delete-event", gtk.main_quit)
        self.connect("destroy", gtk.main_quit)
        
        ManuItems = {
            0 , #: TestDisplayState
#            1 , #: TestAudioState
#            2 , #: TestMediaState
        }
        
        AutoItems = {
            0 , #: TestSDStorageState
            1 , #: TestUsbStorage1State
            2 , #: TestUsbStorage2State
            3 , #: TestEthernet0State
            4 , #: TestWifiState
            5 , #: TestCanbusState
            6 , #: TestMCUState
            7 , #: TestBSPState
#            8 , #: TestUart1State
#            9 , #: TestUart2State
#            10 , #: TestUart5State
#            11 , #: TestCanbusState
#            12 , #: TestSpiState
#            13 , #: TestI2C0State
        }

        Autocheck = [
            "eth0" , #: TestEthernet0State
            "wlan0" , #: TestWifiState
            "can0" , #: TestCanbusState
#            "eth1" , #: TestEthernet1State
#            "hci0" , #: TestBluetoothState
#            "uart1" , #: TestUart1State
#            "uart2" , #: TestUart2State
#            "uart5" , #: TestUart5State
#            "spi1" , #: TestSpiState
#            "i2c0" , #: TestI2C0State
        ]

        InputItems = {
            0 , #: SerrialNum
            1 , #: Mac1
#            2 , #: Mac2
        }
        
        logging.info('MainWindow...__init__')

        print( "%s" % (Info.Get_OSType()) )
        #print("%s"%os.getcwd() )

        self.SysQuitButton        = gtk.Button("Quit")
        
        #Allstatus
        MPAllstatus.append(0)
        
        #Manual Item
        for i in ManuItems:
            MPManubuttons.append(gtk.Fixed())
            MPManustatus.append(0)
        
        #Auto Item
        for i in AutoItems:
            MPAutobuttons.append(gtk.Fixed())
            MPAutostatus.append(0)
        for i in Autocheck:
            MPtestcheck.append(i)
        
        #Input Item
        for i in InputItems:
            MPInputEntrys.append(gtk.Entry())
            MPInputstatus.append(0)
        
        # VBoxFrame 
        self.MainFrame = gtk.VBox(spacing=6)
        self.add(self.MainFrame)

        #Net = network.NetWork(parent=self,drawarea=self.MainFrame)
        
        # initial screen layout
        self.Layout = layout.Layout(parent=self) 

        self.SysQuitButton.connect( "clicked", self.Run_Quit)
        
        #self.Audio   = Audio.Main( filename="/home/rtx/LetItGo.wav" , hw="0,0" )
        Video_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/tools/001.MP4"
        self.Player  = Video.Main( filename=Video_path , fb="/dev/fb4" , x=0 , y=0 , width=1024 , height=768 , rotate=0)
        #self.Gpu     = Gpu.Main( )
        
        # start run time function
        self.StateProc = state.State(parent=self)
        
        os.system("echo 0 > /sys/class/graphics/fb0/blank")
        os.system("setterm -powersave off -blank 0")
        
        # Create Timer for run time functions , about 200 ms
        gobject.timeout_add( 200 , self.RunTimeCallBack )
 
        self.show_all()
        self.move(0,0)
        #self.maximize()
        self.set_default_size(1024,768)
        self.resize(1920, 1080)
 
    def Run_Quit(self,button):
        #self.Audio.Stop()
        #self.Gpu.Stop()
        self.Player.Stop()
        gtk.main_quit()

    def RunTimeCallBack(self):
        self.StateProc.RunTimeProc()
        #self.Gpu.RunTimeProc()
        #self.Audio.RunTimeProc()
        return True

# - Main Loop ----------------------------------------------------------
for i in files:
    os.system("rm " + i )

logging.basicConfig( filename=files[0] , filemode='w' , level=logging.INFO )
logging.info('Start process...')
gobject.threads_init()
Video.Init()
win = MainWindow()
#win.connect("delete-event", gtk.main_quit)
#win.show_all()
#win.move(0,0)
#win.maximize()
#win.set_default_size(1024,768)
#win.resize(1920, 1080)
gtk.main()
