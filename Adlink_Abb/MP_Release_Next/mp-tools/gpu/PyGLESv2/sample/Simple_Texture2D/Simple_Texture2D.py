# -*- coding: utf-8 -*-

from PyGLESv2 import *
from PyGLESv2.ESUtil import *

def CreateSimpleTexture2D():
    """Create a simple 2x2 texture image with four different colors
    """

    # 2x2 Image, 3 bytes per pixel (R, G, B)
    pixels = (GLubyte * (2 * 2 * 3))(  
      255,   0,   0, # Red
        0, 255,   0, # Green
        0,   0, 255, # Blue
      255, 255,   0) # Yellow

    # Use tightly packed data
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    # Generate a texture object
    textureId = GLuint()
    glGenTextures(1, ctypes.byref(textureId))

    # Bind the texture object
    glBindTexture(GL_TEXTURE_2D, textureId)

    # Load the texture
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 2, 2, 0, GL_RGB, GL_UNSIGNED_BYTE, pixels)

    # Set the filtering mode
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    return textureId

def Init(esContext):
    """Initialize the shader and program object
    """
    userData = esContext.userData

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

    # Load the shaders and get a linked program object
    userData.programObject = esContext.LoadProgram(vShaderStr, fShaderStr)

    # Get the attribute locations
    userData.positionLoc = glGetAttribLocation(userData.programObject, "a_position")
    userData.texCoordLoc = glGetAttribLocation(userData.programObject, "a_texCoord")
   
    # Get the sampler location
    userData.samplerLoc = glGetUniformLocation(userData.programObject, "s_texture")

    # Load the texture
    userData.textureId = CreateSimpleTexture2D()

    glClearColor(0.0, 0.0, 0.0, 0.0)
    return True

def Draw(esContext):
    """Draw a triangle using the shader pair created in Init()
    """
    userData = esContext.userData
    vVertices = (-0.5,  0.5, 0.0, # Position 0
                 0.0,  0.0,       # TexCoord 0 
                 -0.5, -0.5, 0.0, # Position 1
                 0.0,  1.0,       # TexCoord 1
                 0.5, -0.5, 0.0,  # Position 2
                 1.0,  1.0,       # TexCoord 2
                 0.5,  0.5, 0.0,  # Position 3
                 1.0,  0.0)       # TexCoord 3
    indices = (GLushort * 6)(0, 1, 2, 0, 2, 3)

    # Set the viewport
    glViewport(0, 0, esContext.width, esContext.height)
   
    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)

    # Use the program object
    glUseProgram(userData.programObject)

    # Load the vertex position
    vpos = (GLfloat * len(vVertices))(*vVertices)
    glVertexAttribPointer(userData.positionLoc, 3, GL_FLOAT,
                          GL_FALSE, 5 * ctypes.sizeof(GLfloat), vpos)
    # Load the texture coordinate
    vcoord = (GLfloat * len(vVertices[3:]))(*(vVertices[3:]))
    glVertexAttribPointer(userData.texCoordLoc, 2, GL_FLOAT,
                          GL_FALSE, 5 * ctypes.sizeof(GLfloat), vcoord)

    glEnableVertexAttribArray(userData.positionLoc)
    glEnableVertexAttribArray(userData.texCoordLoc)

    # Bind the texture
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, userData.textureId)

    # Set the sampler texture unit to 0
    glUniform1i(userData.samplerLoc, 0)

    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, indices)

    eglSwapBuffers(esContext.eglDisplay, esContext.eglSurface)

def ShutDown(esContext):
    """Cleanup
    """
    userData = esContext.userData

    # Delete texture object
    glDeleteTextures(1, ctypes.byref(userData.textureId))

    # Delete program object
    glDeleteProgram(userData.programObject)

def Main():
    es = ESContext()

    es.InitContext();

    es.CreateWindow("Simple Texture 2D", 320, 240, ES_WINDOW_RGB)

    if not(Init(es)):
        return 0;

    es.RegisterDrawFunc(Draw)

    es.MainLoop()

    es.TerminateContext(ShutDown)

    exit()

if __name__ == '__main__':
    Main()
