#!/usr/bin/env python
# -*- coding: utf8 -*-
import time
import Gpio

GpioObjs = []
GpioObjs.append( Gpio.Main(gpio=16 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=80 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=81 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=82 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=83 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=88 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=89 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=91 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=104 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=105 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=130 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=167 , direction=Gpio.OUTPUT , default=Gpio.LOW) )
GpioObjs.append( Gpio.Main(gpio=168 , direction=Gpio.OUTPUT , default=Gpio.LOW) )

for Obj in GpioObjs :
    Obj.OutLow()
time.sleep( 1 )
for Obj in GpioObjs :
    Obj.OutHigh()
