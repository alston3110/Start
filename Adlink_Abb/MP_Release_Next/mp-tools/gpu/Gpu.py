# -*- coding: utf-8 -*-

#import ESUtil
import shlex, subprocess

class Main:
    def __init__ ( self ) :
        Command = "./player"
        self.RunProc = subprocess.Popen( Command )

    def IsPlaying( self ) :
        if self.RunProc is not None:
            if self.RunProc.poll() is None :
                return False
        else :
            return False
        return True

    def Stop( self ) :
        if self.RunProc is not None:
            self.RunProc.terminate()
            self.RunProc = None
            #if self.RunProc.poll() is not None :
            #    subprocess.Popen.kill( self.RunProc )

    def RunTimeProc( self ) :
        return
