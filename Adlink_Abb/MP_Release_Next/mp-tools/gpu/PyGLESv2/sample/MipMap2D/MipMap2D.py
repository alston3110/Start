# -*- coding: utf-8 -*-

from PyGLESv2 import *
from PyGLESv2.ESUtil import *

def GenMipMap2D(src, srcWidth, srcHeight):
    """From an RGB8 source image, generate the next level mipmap
    """

    texelSize = 3

    dstWidth = srcWidth / 2
    if dstWidth <= 0:
        dstWidth = 1

    dstHeight = srcHeight / 2
    if dstHeight <= 0:
        dstHeight = 1

    dst = (GLubyte * (texelSize * dstWidth * dstHeight))()

    for y in range(dstHeight):
        for x in range(dstWidth):
            r = 0.0
            g = 0.0
            b = 0.0

            # Compute the offsets for 2x2 grid of pixels in previous
            # image to perform box filter
            srcIndex = ((((y * 2) * srcWidth) + (x * 2)) * texelSize,
                        (((y * 2) * srcWidth) + (x * 2 + 1)) * texelSize,
                        ((((y * 2) + 1) * srcWidth) + (x * 2)) * texelSize,
                        ((((y * 2) + 1) * srcWidth) + (x * 2 + 1)) * texelSize)

            # Sum all pixels
            for sample in range(4):
                r += src[srcIndex[sample]]
                g += src[srcIndex[sample] + 1]
                b += src[srcIndex[sample] + 2]

            # Average results
            r /= 4.0
            g /= 4.0
            b /= 4.0

            # Store resulting pixels
            dst[(y * dstWidth + x) * texelSize] = long(r)
            dst[(y * dstWidth + x) * texelSize + 1] = long(g)
            dst[(y * dstWidth + x) * texelSize + 2] = long(b)

    return (dst, dstWidth, dstHeight)

def GenCheckImage(width, height, checkSize):
    """Generate an RGB8 checkerboard image
    """

    pixels = (GLubyte * (width * height * 3))()
   
    for y in range(height):
        for x in range(width):
            if ( x / checkSize ) % 2 == 0:
                rColor = 255 * ( ( y / checkSize ) % 2 );
                bColor = 255 * ( 1 - ( ( y / checkSize ) % 2 ) );
            else:
                bColor = 255 * ( ( y / checkSize ) % 2 );
                rColor = 255 * ( 1 - ( ( y / checkSize ) % 2 ) );

            pixels[(y * height + x) * 3] = rColor
            pixels[(y * height + x) * 3 + 1] = 0
            pixels[(y * height + x) * 3 + 2] = bColor

    return pixels

def CreateMipMappedTexture2D():
    """Create a mipmapped 2D texture image
    """

    # Texture object handle
    width = 256
    height = 256

    pixels = GenCheckImage(width, height, 8)

    # Generate a texture object
    textureId = GLuint()
    glGenTextures(1, ctypes.byref(textureId))

    # Bind the texture object
    glBindTexture(GL_TEXTURE_2D, textureId)

    # Load mipmap level 0
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 
                  0, GL_RGB, GL_UNSIGNED_BYTE, pixels)

    level = 1
    prevImage = pixels
   
    while width > 1 and height > 1:
        # Generate the next mipmap level
        (newImage, newWidth, newHeight) = GenMipMap2D(prevImage, width, height)

        # Load the mipmap level
        glTexImage2D(GL_TEXTURE_2D, level, GL_RGB, 
                    newWidth, newHeight, 0, GL_RGB,
                    GL_UNSIGNED_BYTE, newImage)

        # Set the previous image for the next iteration
        prevImage = newImage;
        level += 1

        # Half the width and height
        width = newWidth
        height = newHeight

    # Set the filtering mode
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return textureId


def Init(esContext):
    """Initialize the shader and program object
    """

    userData = esContext.userData
    vShaderStr ="""
uniform float u_offset;
attribute vec4 a_position;
attribute vec2 a_texCoord;
varying vec2 v_texCoord;
void main()
{
    gl_Position = a_position;
    gl_Position.x += u_offset;
    v_texCoord = a_texCoord;
}
"""
   
    fShaderStr ="""
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

    # Get the offset location
    userData.offsetLoc = glGetUniformLocation(userData.programObject, "u_offset")

    # Load the texture
    userData.textureId = CreateMipMappedTexture2D()

    glClearColor(0.0, 0.0, 0.0, 0.0)
    return True

def Draw(esContext):
    """Draw a triangle using the shader pair created in Init()
    """

    userData = esContext.userData
    vVertices = (-0.5,  0.5, 0.0, 1.5,  # Position 0
                 0.0,  0.0,             # TexCoord 0 
                 -0.5, -0.5, 0.0, 0.75, # Position 1
                 0.0,  1.0,             # TexCoord 1
                 0.5, -0.5, 0.0, 0.75,  # Position 2
                 1.0,  1.0,             # TexCoord 2
                 0.5,  0.5, 0.0, 1.5,   # Position 3
                 1.0,  0.0              # TexCoord 3
                 )
    indices = (GLushort * 6)(0, 1, 2, 0, 2, 3)

    # Set the viewport
    glViewport(0, 0, esContext.width, esContext.height)
   
    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)

    # Use the program object
    glUseProgram(userData.programObject)

    # Load the vertex position
    vpos = (GLfloat * len(vVertices))(*vVertices)
    glVertexAttribPointer(userData.positionLoc, 4, GL_FLOAT, 
                           GL_FALSE, 6 * ctypes.sizeof(GLfloat), vpos)
    # Load the texture coordinate
    vcoord = (GLfloat * len(vVertices[4:]))(*(vVertices[4:]))
    glVertexAttribPointer(userData.texCoordLoc, 2, GL_FLOAT,
                           GL_FALSE, 6 * ctypes.sizeof(GLfloat), vcoord)

    glEnableVertexAttribArray(userData.positionLoc)
    glEnableVertexAttribArray(userData.texCoordLoc)

    # Bind the texture
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, userData.textureId)

    # Set the sampler texture unit to 0
    glUniform1i(userData.samplerLoc, 0)

    # Draw quad with nearest sampling
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glUniform1f(userData.offsetLoc, -0.6)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, indices)

    # Draw quad with trilinear filtering
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glUniform1f(userData.offsetLoc, 0.6)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, indices)

    eglSwapBuffers(esContext.eglDisplay, esContext.eglSurface)

def ShutDown(esContext):
    """Cleanup
    """
    userData = esContext.userData;

    # Delete texture object
    glDeleteTextures(1, ctypes.byref(userData.textureId))

    # Delete program object
    glDeleteProgram(userData.programObject)


def Main():
    es = ESContext()
    es.InitContext()

    es.CreateWindow("MipMap 2D", 640, 480, ES_WINDOW_RGB)

    if not(Init(es)):
        return 0

    es.RegisterDrawFunc(Draw)

    es.MainLoop()

    es.TerminateContext(ShutDown)

    exit()

if __name__ == '__main__':
    Main()
