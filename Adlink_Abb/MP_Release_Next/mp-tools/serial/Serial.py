#! python

import serial

PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE = 'N', 'E', 'O', 'M', 'S'
STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO = (1, 1.5, 2)
FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS = (5, 6, 7, 8)

class Main:
    def __init__ ( self , port , baudrate=115200 , parity=PARITY_NONE , stopbits=STOPBITS_ONE , bytesize=EIGHTBITS , rtscts=0 , xonxoff=0):
        self.Serial = serial.Serial( port=port , baudrate=baudrate , parity=parity , stopbits=stopbits , bytesize=bytesize , timeout=1.0 , xonxoff=xonxoff , rtscts=rtscts )
        if not self.Serial.isOpen():
            self.Serial.open()

    def Close( self ) :
        self.Serial.close()

    def Write( self , data ) :
        self.Serial.write( data )

    def Read( self , size ) :
        return self.Serial.read( size )

    def IsOpen( self ) :
        return self.Serial.isOpen()

    def LoopTest( self ) :
        if not self.Serial.isOpen():
            return False
        self.Serial.write('Loop Test 1234567890')
        ReadData = self.Serial.read(20)
        if not ReadData == 'Loop Test 1234567890':
            return False
        return True

    def OtherPortTest( self , other ) :
        if not self.Serial.isOpen():
            return False
        if not other.IsOpen():
            return False
        self.Serial.write('Loop Test 1234567890')
        ReadData = other.Read(20)
        if not ReadData == 'Loop Test 1234567890':
            return False
        
        other.Write( 'Loop Test 0987654321' )
        ReadData = self.Serial.read(20)
        if not ReadData == 'Loop Test 0987654321':
            return False
        
        return True
