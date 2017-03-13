# -*- coding: utf-8 -*-

from PyGLESv2 import *
from PyGLESv2.ESUtil import *

def CreateSimpleTextureCubemap():
    """Create a simple cubemap with a 1x1 face with a different color for each face
    """

    # Six 1x1 RGB faces
    def cubePixels(idx):
        pixels = (
            # Face 0 - Red
            255, 0, 0,
            # Face 1 - Green,
            0, 255, 0, 
            # Face 3 - Blue
            0, 0, 255,
            # Face 4 - Yellow
            255, 255, 0,
            # Face 5 - Purple
            255, 0, 255,
            # Face 6 - White
            255, 255, 255)
        return (GLubyte * 3)(*pixels[idx * 3:idx * 3 + 3])
   
    # Generate a texture object
    textureId = GLuint()
    glGenTextures(1, ctypes.byref(textureId));

    # Bind the texture object
    glBindTexture(GL_TEXTURE_CUBE_MAP, textureId)
   
    # Load the cube face - Positive X
    glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X, 0, GL_RGB, 1, 1, 0, 
                 GL_RGB, GL_UNSIGNED_BYTE, cubePixels(0))

    # Load the cube face - Negative X
    glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_X, 0, GL_RGB, 1, 1, 0, 
                 GL_RGB, GL_UNSIGNED_BYTE, cubePixels(1))

    # Load the cube face - Positive Y
    glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Y, 0, GL_RGB, 1, 1, 0, 
                 GL_RGB, GL_UNSIGNED_BYTE, cubePixels(2))

    # Load the cube face - Negative Y
    glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, 0, GL_RGB, 1, 1, 0, 
                 GL_RGB, GL_UNSIGNED_BYTE, cubePixels(3))

    # Load the cube face - Positive Z
    glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, 1, 1, 0, 
                 GL_RGB, GL_UNSIGNED_BYTE, cubePixels(4))

    # Load the cube face - Negative Z
    glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, 0, GL_RGB, 1, 1, 0, 
                 GL_RGB, GL_UNSIGNED_BYTE, cubePixels(5))

    # Set the filtering mode
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    return textureId

def Init(esContext):
    """Initialize the shader and program object
    """
    userData = esContext.userData
    vShaderStr = """
attribute vec4 a_position;
attribute vec3 a_normal;
varying vec3 v_normal;
void main()
{
    gl_Position = a_position;
    v_normal = a_normal;
}
"""
   
    fShaderStr = """
precision mediump float;
varying vec3 v_normal;
uniform samplerCube s_texture;
void main()
{
    gl_FragColor = textureCube( s_texture, v_normal );
}
"""

    # Load the shaders and get a linked program object
    userData.programObject = esContext.LoadProgram(vShaderStr, fShaderStr)

    # Get the attribute locations
    userData.positionLoc = glGetAttribLocation(userData.programObject, "a_position")
    userData.normalLoc = glGetAttribLocation(userData.programObject, "a_normal")
   
    # Get the sampler locations
    userData.samplerLoc = glGetUniformLocation(userData.programObject, "s_texture")

    # Load the texture
    userData.textureId = CreateSimpleTextureCubemap()

    # Generate the vertex data
    (vertices, normals, texCoords, indices) = esContext.GenSphere(20, 0.75, True, True, False, True)
    userData.vertices = (GLfloat * len(vertices))(*vertices)
    userData.normals = (GLfloat * len(vertices))(*normals)
    userData.indices = (GLushort * len(indices))(*indices)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    return True

def Draw(esContext):
    """Draw a triangle using the shader pair created in Init()
    """
    userData = esContext.userData
      
    # Set the viewport
    glViewport(0, 0, esContext.width, esContext.height)
   
    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)

    glCullFace(GL_BACK)
    glEnable(GL_CULL_FACE)

    # Use the program object
    glUseProgram(userData.programObject)

    # Load the vertex position
    glVertexAttribPointer(userData.positionLoc, 3, GL_FLOAT,
                          GL_FALSE, 0, userData.vertices)
    # Load the normal
    glVertexAttribPointer(userData.normalLoc, 3, GL_FLOAT,
                          GL_FALSE, 0, userData.normals)

    glEnableVertexAttribArray(userData.positionLoc)
    glEnableVertexAttribArray(userData.normalLoc)

    # Bind the texture
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_CUBE_MAP, userData.textureId)

    # Set the sampler texture unit to 0
    glUniform1i(userData.samplerLoc, 0)

    glDrawElements(GL_TRIANGLES, len(userData.indices), 
                   GL_UNSIGNED_SHORT, userData.indices);

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

    es.InitContext()

    es.CreateWindow("Simple Texture Cubemap", 320, 240, ES_WINDOW_RGB)

    if not(Init(es)):
        return 0

    es.RegisterDrawFunc(Draw)

    es.MainLoop()

    es.TerminateContext(ShutDown)

    exit()

if __name__ == '__main__':
    Main()
