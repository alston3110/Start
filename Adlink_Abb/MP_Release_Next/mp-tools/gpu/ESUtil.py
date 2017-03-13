# -*- coding: utf-8 -*-

from EGL import *
from GLESv2 import *
import math

def ESUtil_ErrorCheck( exp=True ) :
    retval = eglGetError()
    if EGL_SUCCESS != retval or False == exp:
        class EGLError(Exception):
            pass
        raise EGLError()

class Main:
    def  __init__( self , fb=0 ) :
        self.EGLNativeDisplay = EGLNativeDisplayType()
        self.EGLDisplay       = EGLNativeDisplayType()
        self.EGLWidth         = EGLint()
        self.EGLHeight        = EGLint()
        self.EGLMajor         = EGLint()
        self.EGLMinor         = EGLint()
        self.EGLSurface       = EGLSurface()
        self.EGLContext       = EGLContext()

        self.EGLNativeDisplay = fbGetDisplayByIndex( fb ) ;

        fbGetDisplayGeometry( self.EGLNativeDisplay , ctypes.byref( self.EGLWidth ) , ctypes.byref( self.EGLHeight ) )

        print self.EGLWidth.value
        print self.EGLHeight.value

        self.EGLDisplay = eglGetDisplay( self.EGLNativeDisplay ) ;

        eglInitialize( self.EGLDisplay , ctypes.byref( self.EGLMajor ) , ctypes.byref( self.EGLMinor ) )
    
        Attrs = (EGL_DEPTH_SIZE , EGL_DONT_CARE ,
                 EGL_RED_SIZE   , 8 ,
                 EGL_GREEN_SIZE , 8 ,
                 EGL_BLUE_SIZE  , 8 ,
                 EGL_ALPHA_SIZE , 8 ,
                 EGL_NONE)

        Config = EGLConfig()
        Num = EGLint()
        ESUtil_ErrorCheck( eglChooseConfig( self.EGLDisplay , (EGLint * len(Attrs))(*Attrs) , ctypes.byref(Config) , 1 , ctypes.byref(Num) ) )
    
        Window = fbCreateWindow( self.EGLNativeDisplay , 0 , 0 , self.EGLWidth.value , self.EGLHeight.value )

        self.EGLSurface = eglCreateWindowSurface(self.EGLDisplay, Config, Window, ctypes.cast(ctypes.c_void_p(0), ctypes.POINTER(EGLint)))
        ESUtil_ErrorCheck( (self.EGLSurface != EGL_NO_SURFACE) )

        ESUtil_ErrorCheck( eglBindAPI( EGL_OPENGL_ES_API ) )

        CtxAttrs = (EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE)
        self.EGLContext = eglCreateContext( self.EGLDisplay , Config , ctypes.c_void_p(0) , (EGLint * len(CtxAttrs))(*CtxAttrs) )
        ESUtil_ErrorCheck( self.EGLContext != EGL_NO_CONTEXT )

        eglMakeCurrent( self.EGLDisplay , self.EGLSurface , self.EGLSurface , self.EGLContext )
        ESUtil_ErrorCheck()

        vShaderStr = """
attribute vec4 a_position;
attribute vec2 a_texCoord;
varying vec2 v_texCoord;
void main()
{
    gl_Position = a_position;
    v_texCoord = a_texCoord;
}
"""
   
        fShaderStr = """
precision mediump float;
varying vec2 v_texCoord;
uniform sampler2D s_texture;
void main()
{
    gl_FragColor = texture2D( s_texture, v_texCoord );
}
"""

        self.ProgramObject = self.LoadProgram(vShaderStr, fShaderStr)

        glClearColor(0.0, 0.0, 0.0, 0.0)
        
        
    def LoadShader( self , type , shadersrc ) :
        # Create the shader object
        Shader = glCreateShader( type )
        if Shader == 0 :
            return 0

        # Load the shader source
        Src = ctypes.c_char_p( shadersrc )
        glShaderSource( Shader , 1 , ctypes.byref(Src) , ctypes.cast( 0 , ctypes.POINTER( GLint ) ) )

        # Compile the shader
        glCompileShader( Shader )

        # Check the compile status
        Compiled = GLint()
        glGetShaderiv( Shader , GL_COMPILE_STATUS , ctypes.byref( Compiled ) )
        if not( Compiled.value ) :
            InfoLen = GLint()

            glGetShaderiv( Shader , GL_INFO_LOG_LENGTH , ctypes.byref( InfoLen ) )

            if InfoLen.value >= 1 :
                InfoLog = ctypes.create_string_buffer( InfoLen.value )

                glGetShaderInfoLog( Shader , InfoLen , 0 , InfoLog )
                print "Error compiling shader:\n%s\n", InfoLog

                glDeleteShader( Shader )

            return 0

        return Shader

    def LoadProgram(self, vertShaderSrc, fragShaderSrc):
        """Load a vertex and fragment shader, create a program object, link program
        @param vertShaderSrc: Vertex shader source code
        @param fragShaderSrc:  Fragment shader source code
        @return: A new program object linked with the vertex/fragment shader pair, 0 on failure
        """

        # Load the vertex/fragment shaders
        vertexShader = self.LoadShader(GL_VERTEX_SHADER, vertShaderSrc)
        if vertexShader == 0:
            return 0
        
        fragmentShader = self.LoadShader(GL_FRAGMENT_SHADER, fragShaderSrc)
        if fragmentShader == 0:
            glDeleteShader(vertexShader)
            return 0

        # Create the program object
        programObject = glCreateProgram()

        if programObject == 0:
            return 0
        
        glAttachShader(programObject, vertexShader)
        glAttachShader(programObject, fragmentShader)
        
        # Link the program
        glLinkProgram(programObject)

        # Check the link status
        linked = gleshelper.glGetProgramiv(programObject, GL_LINK_STATUS)
        
        if not(linked):

            infoLen = gleshelper.glGetProgramiv(programObject, GL_INFO_LOG_LENGTH)

            if infoLen > 1:
                infoLog = gleshelper.glGetProgramInfoLog(programObject, infoLen)
                print "Error linking program:\n%s\n", infoLog            

            glDeleteProgram(programObject)
            return 0

        # Free up no longer needed shader resources
        glDeleteShader(vertexShader)
        glDeleteShader(fragmentShader)

        return programObject

    def SwapSurface( self ) :
        vertices = (GLfloat * (3 * 3))(0.0, 0.5, 0.0,
                -0.5, -0.5, 0.0,
                0.5, -0.5, 0.0)

        # Set the viewport
        #glViewport(0, 0, esContext.width, esContext.height)

        # Clear the color buffer
        glClear(GL_COLOR_BUFFER_BIT)

        # Use the program object
        glUseProgram( self.ProgramObject )

        # Load the vertex data
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, vertices)
        glEnableVertexAttribArray(0)

        glDrawArrays(GL_TRIANGLES, 0, 3)
        
        eglSwapBuffers( self.EGLDisplay , self.EGLSurface )
        ESUtil_ErrorCheck()

    def Close( self ) :
        if self.EGLDisplay is not None:
            eglMakeCurrent( self.EGLDisplay , EGL_NO_SURFACE , EGL_NO_SURFACE , EGL_NO_CONTEXT )
            eglDestroyContext( self.EGLDisplay , self.EGLContext )
            eglDestroySurface( self.EGLDisplay , self.EGLSurface )
            eglTerminate( self.EGLDisplay )
