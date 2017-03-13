import Serial

Uart1 = Serial.Main( port="/dev/ttymxc3" , baudrate=115200 , parity=Serial.PARITY_EVEN, rtscts=1)
Uart2 = Serial.Main( port="/dev/ttymxc4" , baudrate=115200 , rtscts=1)

if Uart1.LoopTest() :
    print "OK"

if Uart2.LoopTest() :
    print "OK"

if Uart1.OtherPortTest( Uart2 ) :
    print "OK"

Uart1.Close()
Uart2.Close()
