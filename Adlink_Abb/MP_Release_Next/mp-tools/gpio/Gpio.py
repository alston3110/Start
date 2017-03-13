#!/usr/bin/env python
# -*- coding: utf8 -*-

import os.path

LOW, HI = (0, 1)
INPUT, OUTPUT = (0, 1)
STOP, RUN , PAUSE = (0, 1, 2)
GPIO_list = ['209c000' , '20a0000' , '20a4000' , '20a8000' , '20ac000' , '20b0000' , '20b4000' ]

class Main:
    def __init__ ( self , gpio , direction=INPUT , default=LOW ) :
        self.GpioExist    = 0 ;
        self.GpioNum      = gpio
        self.GpioCtlFile  = "/sys/devices/soc0/soc.1/2000000.aips-bus/" \
			+ GPIO_list[gpio/32] + ".gpio/gpio/gpio" + `gpio`
	self.GpioCtlValue = self.GpioCtlFile + "/value"
        self.GpioCtlDir   = self.GpioCtlFile + "/direction"
        self.Direction    = direction
        self.Default      = default

        if not os.path.exists( self.GpioCtlFile ) :
            print "Error : file(%s) not exist." % ( self.GpioCtlFile )
        else :
            self.GpioExist    = 1 ;
            try :
                fp = open( self.GpioCtlDir , "w" )
            except IOError:
                print "Error : file(%s) can not open." % ( self.GpioCtlValue )
            else :
                if self.Direction == INPUT :
                    fp.write('in')
                else :
                    fp.write('out')
                fp.close()

            if self.Direction == OUTPUT :
                if self.Default == LOW :
                    self.OutLow()
                else :
                    self.OutHigh()

    def Direction( self ) :
        return self.Direction

    def OutLow( self ) :
        if self.Direction == OUTPUT :
            try :
                fp = open( self.GpioCtlValue , "w" )
            except IOError:
                print "Error : file(%s) can not open." % ( self.GpioCtlValue )
            else :
                fp.write('0')
                fp.close()

    def OutHigh( self ) :
        if self.Direction == OUTPUT :
            try :
                fp = open( self.GpioCtlValue , "w" )
            except IOError:
                print "Error : file(%s) can not open." % ( self.GpioCtlValue )
            else :
                fp.write('1')
                fp.close()

    def Out( self , data ) :
        if data == LOW :
            self.OutLow()
        else :
            self.OutHigh()

    def In( self ) :
        Ret = 0
        try :
            fp = open( self.GpioCtlValue , "r" )
        except IOError:
            print "Error : file(%s) can not open." % ( self.GpioCtlValue )
        else :
            TmpData = fp.read()
            fp.close()
            Ret = ord(TmpData[0]) - ord('0')
        return Ret

    def LoopTest( self , other ) :
        if self.Direction == OUTPUT :
            if other.Direction() == OUTPUT :
                print "Error : The Gpios are same direction."
                return False
            else :
                self.OutLow()
                if other.In() == 1 :
                    return False
                self.OutHigh()
                if other.In() == 0 :
                    return False                
        else :
            if other.Direction() == INPUT :
                print "Error : The Gpios are same direction."
                return False
            else :
                other.OutLow()
                if self.In() == 1 :
                    return False
                other.OutHigh()
                if self.In() == 0 :
                    return False                  

        return True
