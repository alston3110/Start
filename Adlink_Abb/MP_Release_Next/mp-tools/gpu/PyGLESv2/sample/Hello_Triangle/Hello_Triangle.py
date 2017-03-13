# -*- coding: utf-8 -*-


from PyGLESv2 import *
from PyGLESv2.ESUtil import *

def LoadShader(type, shader_src):
    """Create a shader object, load the shader source, and compile the shader.
    """

    # Create the shader object
    shader = glCreateShader(type)
    if shader == 0:
        return 0

    # Load the shader source
    src = ctypes.c_char_p(shader_src)
    glShaderSource(shader, 1, ctypes.byref(src), ctypes.cast(0, ctypes.POINTER(GLint)))

    # Compile the shader
    glCompileShader(shader)

    # Check the compile status
    compiled = GLint()
    glGetShaderiv(shader, GL_COMPILE_STATUS, ctypes.byref(compiled))
    if not(compiled.value):
        infoLen = GLint()

        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, ctypes.byref(infoLen)) 

        if infoLen.value >= 1:
            infoLog = ctypes.create_string_buffer(infoLen.value)

            glGetShaderInfoLog(shader, infoLen, 0, infoLog)
            print "Error compiling shader:\n%s\n", infoLog

            glDeleteShader(shader)

        return 0;

    return shader

def Init(esContext):
    """Initialize the shader and program object
    """
    vShaderStr = """
attribute vec4 vPosition;

void main()
{
   gl_Position = vPosition;
}
"""
    
    fShaderStr = """
precision mediump float;

void main()
{
  gl_FragColor = vec4 ( 1.0, 0.0, 0.0, 1.0 );
}
"""

    # Load the vertex/fragment shaders
    vertexShader = LoadShader(GL_VERTEX_SHADER, vShaderStr)
    fragmentShader = LoadShader(GL_FRAGMENT_SHADER, fShaderStr)

    # Create the program object
    programObject = glCreateProgram()

    if programObject == 0:
        return False

    glAttachShader(programObject, vertexShader)
    glAttachShader(programObject, fragmentShader)

    # Bind vPosition to attribute 0
    glBindAttribLocation(programObject, 0, "vPosition")

    # Link the program
    glLinkProgram(programObject)

    # Check the link status
    linked = GLint()
    glGetProgramiv(programObject, GL_LINK_STATUS, ctypes.byref(linked))

    if not(linked.value):
        infoLen = GLint()

        glGetProgramiv(programObject, GL_INFO_LOG_LENGTH, ctypes.byref(infoLen))

        if infoLen > 1:
            infoLog = ctypes.create_string_buffer(infoLen)

            glGetProgramInfoLog(programObject, infoLen, NULL, infoLog)
            print "Error linking program:\n%s\n", infoLog           

        glDeleteProgram(programObject)

        return False

    # Store the program object
    esContext.userData.programObject = programObject

    glClearColor(0.0, 0.0, 0.0, 0.0)

    return True

def Draw(esContext):
    """Draw a triangle using the shader pair created in Init()
    """

    vertices = (GLfloat * (3 * 3))(0.0, 0.5, 0.0,
                -0.5, -0.5, 0.0,
                0.5, -0.5, 0.0)

    # Set the viewport
    glViewport(0, 0, esContext.width, esContext.height)

    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)

    # Use the program object
    glUseProgram(esContext.userData.programObject)

    # Load the vertex data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, vertices)
    glEnableVertexAttribArray(0)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    eglSwapBuffers(esContext.eglDisplay, esContext.eglSurface)

#    print esContext.GetFps()

def Main():
    es = ESContext()

    es.InitContext()

    es.CreateWindow("Hello Triangle!", 320, 240, ES_WINDOW_RGB)

    if False == Init(es):
        exit()

    es.RegisterDrawFunc(Draw)

    es.MainLoop()

    es.TerminateContext()

    exit()

if __name__ == '__main__':
    Main()
