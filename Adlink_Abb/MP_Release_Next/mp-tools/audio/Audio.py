#! python

import shlex, subprocess

#p1_args = shlex.split("aplay -D hw:0,0 LetItGo.wav")
#p2_args = shlex.split("aplay -D hw:1,0 LetItGo.wav")
#subprocess.call(["aplay", "-D hw:1,0 LetItGo.wav"])
#p1 = subprocess.Popen(p1_args)
#p2 = subprocess.Popen(p2_args)

class Main:
    def __init__ ( self , filename , hw="0,0" ) :
        Command = "aplay -D hw:" + hw + " " + filename
        self.Command_Args = shlex.split( Command )
        self.RunProc = subprocess.Popen( self.Command_Args )

    def Play( self ) :
        if self.RunProc is not None:
            self.RunProc.terminate()
            self.RunProc = None
            self.RunProc = subprocess.Popen( self.Command_Args )
        else :
            self.RunProc = subprocess.Popen( self.Command_Args )

    def IsPlaying( self ) :
        if self.RunProc is None:
            return False
        else :
            if self.RunProc.poll() is None:
                return True
        return False

    def Stop( self ) :
        if self.RunProc is not None:
            self.RunProc.terminate()
            self.RunProc.wait()
            self.RunProc = None
            #if self.RunProc.poll() is not None :
            #    subprocess.Popen.kill( self.RunProc )

    def RunTimeProc( self ) :
        if self.RunProc is not None :
            if not self.IsPlaying() :
                self.RunProc = None
                self.Play()
