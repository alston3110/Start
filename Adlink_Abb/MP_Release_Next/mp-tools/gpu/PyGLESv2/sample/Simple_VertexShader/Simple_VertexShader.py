# -*- coding: utf-8 -*-

from PyGLESv2 import *
from PyGLESv2.ESUtil import *

def Init(esContext):
    """Initialize the shader and program object
    """

    vShaderStr = """
uniform mat4 u_mvpMatrix;
attribute vec4 a_position;
void main()
{
    gl_Position = u_mvpMatrix * a_position;
}
"""

    fShaderStr = """
precision mediump float;
void main()
{
    gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}
"""

    # Load the shaders and get a linked program object
    esContext.userData.programObject = esContext.LoadProgram(vShaderStr, fShaderStr)

    # Get the attribute locations
    esContext.userData.positionLoc = glGetAttribLocation(esContext.userData.programObject, "a_position")

    # Get the uniform locations
    esContext.userData.mvpLoc = glGetUniformLocation(esContext.userData.programObject, "u_mvpMatrix")

    # Generate the vertex data
    cube = esContext.GenCube(1.0, True, False, False, True)
    esContext.userData.vertices = (GLfloat * len(cube[0]))(*cube[0])
    esContext.userData.indices = (GLushort * len(cube[3]))(*cube[3])

    # Starting rotation angle for the cube
    esContext.userData.angle = 45.0

    glClearColor(0.0, 0.0, 0.0, 0.0)

    return True;

def Update(esContext, deltaTime):
    """Update MVP matrix based on time
    """

    # Compute a rotation angle based on time to rotate the cube
    esContext.userData.angle += ( deltaTime * 40.0 )
    if esContext.userData.angle >= 360.0:
        esContext.userData.angle -= 360.0

    # Compute the window aspect ratio
    aspect = esContext.width / esContext.height


    # Generate a perspective matrix with a 60 degree FOV
    perspective = ESMatrix()
    perspective.LoadIdentity()
    perspective.Perspective(60.0, aspect, 1.0, 20.0)

    # Generate a model view matrix to rotate/translate the cube
    modelview = ESMatrix()
    modelview.LoadIdentity()

    # Translate away from the viewer
    modelview.Translate(0.0, 0.0, -2.0)
    
    # Rotate the cube
    modelview.Rotate(esContext.userData.angle, 1.0, 0.0, 1.0)
    
    # Compute the final MVP by multiplying the 
    # modevleiw and perspective matrices together
    esContext.userData.mvpMatrix = modelview.Multiply(perspective)


def Draw(esContext):
    """Draw a triangle using the shader pair created in Init()
    """
    
    # Set the viewport
    glViewport(0, 0, esContext.width, esContext.height)


    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Use the program object
    glUseProgram(esContext.userData.programObject)
    
    # Load the vertex position
    glVertexAttribPointer(esContext.userData.positionLoc,
                          3,
                          GL_FLOAT, 
                          GL_FALSE,
                          3 * ctypes.sizeof(GLfloat),
                          esContext.userData.vertices)

    glEnableVertexAttribArray(esContext.userData.positionLoc)
    
    
    # Load the MVP matrix
    glUniformMatrix4fv(esContext.userData.mvpLoc, 1, GL_FALSE, esContext.userData.mvpMatrix.pointer())
    
    # Draw the cube
    glDrawElements(GL_TRIANGLES, len(esContext.userData.indices), GL_UNSIGNED_SHORT, esContext.userData.indices)
    
    eglSwapBuffers(esContext.eglDisplay, esContext.eglSurface)

def ShutDown(esContext):
    """Cleanup
    """
    # Delete program object
    glDeleteProgram(esContext.userData.programObject)

def Main():
    es = ESContext()
    es.InitContext()

    es.CreateWindow("Simple Texture 2D", 640, 480, ES_WINDOW_RGB)
    if not(Init(es)):
        return

    es.RegisterDrawFunc(Draw)
    es.RegisterUpdateFunc(Update)
   
    es.MainLoop()

    es.TerminateContext(ShutDown)

    exit()

if __name__ == '__main__':
    Main()
