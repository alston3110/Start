# -*- coding: utf-8 -*-

from EGL import *
from GLESv2 import *
import win32 as system
import math

class _WindowProxy(system.Window):
    def __init__(self, esContext, title, width, height):
        system.Window.__init__(self, name=title, width=width, height=height)
        self.esContext = esContext
        self.lastTime = system.get_tick()
        self.lastDraw = self.lastTime
        self.frames = 0
        self.fps = 0.0
        self.interval = 500

    def onPaint(self):
        current = system.get_tick()
        self.frames += 1
        if self.interval <= current - self.lastDraw:
            self.fps = self.frames / ((current - self.lastDraw) / 1000.0)
            self.lastDraw = current
            self.frames = 0

        if self.esContext.drawFunc:
            self.esContext.drawFunc(self.esContext)

    def onIdle(self):
        current = system.get_tick()
        deltaTime = (current - self.lastTime) / 1000.0
        self.lastTime = current
        if self.esContext.updateFunc:
            self.esContext.updateFunc(self.esContext, deltaTime)

        self.onPaint()

    def onKeyEvent(self, key, x, y):
        if self.esContext.keyFunc:
            self.esContext.keyFunc(self.esContext, key, x, y)
            
def _assertEGLError(exp=True):
    retval = eglGetError()
    if EGL_SUCCESS != retval or False == exp:
        class EGLError(Exception):
            pass
        raise EGLError()

ES_WINDOW_RGB         = 0x00
ES_WINDOW_ALPHA       = 0x01 
ES_WINDOW_DEPTH       = 0x02 
ES_WINDOW_STENCIL     = 0x04
ES_WINDOW_MULTISAMPLE = 0x08

class ESContext(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.window = None
        self.drawFunc = None
        self.updateFunc = None
        self.keyFunc = None
        self.eglDisplay = None
        self.eglContext = None
        self.eglSurface = None
        self.width = 0
        self.height = 0
        class UserData: pass
        self.userData = UserData()

    def __del__(self):
        print "in destructor."

    def InitContext(self):
        """Initialize this context
        """
        # do nothing
        pass

    def TerminateContext(self, shutdown = None):
        if shutdown:
            shutdown(self)

        eglDestroyContext(self.eglDisplay, self.eglContext)
        eglDestroySurface(self.eglDisplay, self.eglSurface)
        eglTerminate(self.eglDisplay)


    def CreateWindow(self, title="", width=640, height=480, flags=ES_WINDOW_RGB):
        """Create a window with the specified parameters

        @param title: Name for title bar of window
        @param width: Width in pixels of window to create
        @param height: Height in pixels of window to create
        @param flags: Bitfield for the window creation flags
            ES_WINDOW_RGB     - specifies that the color buffer should have R,G,B channels
            ES_WINDOW_ALPHA   - specifies that the color buffer should have alpha
            ES_WINDOW_DEPTH   - specifies that a depth buffer should be created
            ES_WINDOW_STENCIL - specifies that a stencil buffer should be created
            ES_WINDOW_MULTISAMPLE - specifies that a multi-sample buffer should be created
        """
        self.window = _WindowProxy(self, title, width, height)

        display = eglGetDisplay(self.window.getDisplayId());
        if display == EGL_NO_DISPLAY:
            display = eglGetDisplay(EGL_DEFAULT_DISPLAY);

        _assertEGLError(display != EGL_NO_DISPLAY)

        self.eglDisplay = display
        self.width = width
        self.height = height

        major = EGLint()
        minor = EGLint()
        eglInitialize(self.eglDisplay, ctypes.byref(major), ctypes.byref(minor));
        self.eglVersion = (major.value, minor.value)

        attrs = (EGL_RED_SIZE, 5,
                 EGL_GREEN_SIZE, 6,
                 EGL_BLUE_SIZE, 5,
                 EGL_ALPHA_SIZE, 8 if (flags & ES_WINDOW_ALPHA) else EGL_DONT_CARE,
                 EGL_DEPTH_SIZE, 8 if (flags & ES_WINDOW_DEPTH) else EGL_DONT_CARE,
                 EGL_STENCIL_SIZE, 8 if (flags & ES_WINDOW_STENCIL) else EGL_DONT_CARE,
                 EGL_SAMPLE_BUFFERS, 1 if (flags & ES_WINDOW_MULTISAMPLE) else 0,
                 EGL_NONE)
        config = EGLConfig()
        num = EGLint()
        _assertEGLError(eglChooseConfig(self.eglDisplay, (EGLint * len(attrs))(*attrs), ctypes.byref(config), 1, ctypes.byref(num)))

        self.eglSurface = eglCreateWindowSurface(self.eglDisplay, config, self.window.getHandle(), ctypes.cast(ctypes.c_void_p(0), ctypes.POINTER(EGLint)));
        _assertEGLError(self.eglSurface != EGL_NO_SURFACE)

        eglBindAPI(EGL_OPENGL_ES_API);
        _assertEGLError()

        ctx_attrs = (EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE)
        self.eglContext = eglCreateContext(self.eglDisplay, config, ctypes.c_void_p(0), (EGLint * len(ctx_attrs))(*ctx_attrs));
        _assertEGLError(self.eglContext != EGL_NO_CONTEXT)

        eglMakeCurrent(self.eglDisplay, self.eglSurface, self.eglSurface, self.eglContext);
        _assertEGLError()

    def MainLoop(self):
        """Start the main loop for the application
        """
        self.window.run()

    def RegisterDrawFunc(self, drawFunc):
        """Register a draw callback function to be used to render each frame
        @param drawFunc: Draw callback function that will be used to render the scene
        """
        self.drawFunc = drawFunc

    def RegisterUpdateFunc(self, updateFunc):
        """Register an update callback function to be used to update on each time step
        @param updateFunc: Update callback function that will be used to render the scene
        """
        self.updateFunc = updateFunc

    def RegisterKeyFunc(self, keyFunc):
        """Register an keyboard input processing callback function
        @param keyFunc: Key callback function for application processing of keyboard input
        """
        self.keyFunc = keyFunc

    def LoadShader(self, type, shaderSrc):
        """Load a shader, check for compile errors, print error messages to output log
        @param type: Type of shader (GL_VERTEX_SHADER or GL_FRAGMENT_SHADER)
        @param shaderSrc: Shader source string
        @return: A new shader object on success, 0 on failure
        """
    
        # Create the shader object
        shader = glCreateShader(type)
        if shader == 0:
            return 0
    
        # Load the shader source
        src = ctypes.c_char_p(shaderSrc)
        glShaderSource(shader, 1, ctypes.byref(src), ctypes.cast(ctypes.c_void_p(0), ctypes.POINTER(GLint)))
    
        # Compile the shader
        glCompileShader(shader)
    
        # Check the compile status
        compiled = gleshelper.glGetShaderiv(shader, GL_COMPILE_STATUS)

        if not(compiled):

            infoLen = gleshelper.glGetShaderiv(shader, GL_INFO_LOG_LENGTH) 
    
            if infoLen >= 1:
                infoLog = gleshelper.glGetShaderInfoLog(shader, infoLen)
                print "Error compiling shader:\n%s\n", infoLog
    
            glDeleteShader(shader)
    
            return 0;
    
        return shader

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

    def GenSphere(self, numSlices, radius, vertices, normals, texCoords, indices):
        numParallels = numSlices / 2
        numVertices = (numParallels + 1) * (numSlices + 1)
        numIndices = numParallels * numSlices * 6
        angleStep = (2.0 * math.pi) / numSlices
    
        if vertices:
            vertices = [0.0] * (3 * numVertices)
        if normals:
            normals = [0.0] * (3 * numVertices)
        if texCoords:
            texCoords = [0.0] * (2 * numVertices)
        if indices:
            indices = [0] * numIndices

        for i in range(numParallels + 1):
            for j in range(numSlices + 1):
                vertex = ( i * (numSlices + 1) + j ) * 3 
    
                if vertices:
                    vertices[vertex + 0] = radius * math.sin(angleStep * i) * math.sin(angleStep * j)
                    vertices[vertex + 1] = radius * math.cos(angleStep * i)
                    vertices[vertex + 2] = radius * math.sin(angleStep * i) * math.cos(angleStep * j)
    
                if normals:
                    normals[vertex + 0] = vertices[vertex + 0] / radius
                    normals[vertex + 1] = vertices[vertex + 1] / radius
                    normals[vertex + 2] = vertices[vertex + 2] / radius
    
                if texCoords:
                    texIndex = ( i * (numSlices + 1) + j ) * 2
                    texCoords[texIndex + 0] = float(j / numSlices)
                    texCoords[texIndex + 1] = (1.0 - i) / (numParallels - 1)
    
        # Generate the indices
        if indices:
            x = 0
            for i in range(numParallels):
                for j in range(numSlices):
                    indices[x  ] = i * (numSlices + 1) + j;
                    indices[x+1] = (i + 1) * (numSlices + 1) + j;
                    indices[x+2] = (i + 1) * (numSlices + 1) + (j + 1);
    
                    indices[x+3] = i * (numSlices + 1) + j;
                    indices[x+4] = (i + 1) * (numSlices + 1) + (j + 1);
                    indices[x+5] = i * (numSlices + 1) + (j + 1);
                    x += 6

        return (vertices, normals, texCoords, indices);

    def GenCube(self, scale, vertices, normals, texCoords, indices):

        cubeVerts = (
           -0.5, -0.5, -0.5,
           -0.5, -0.5,  0.5,
           0.5, -0.5,  0.5,
           0.5, -0.5, -0.5,
           -0.5,  0.5, -0.5,
           -0.5,  0.5,  0.5,
           0.5,  0.5,  0.5,
           0.5,  0.5, -0.5,
           -0.5, -0.5, -0.5,
           -0.5,  0.5, -0.5,
           0.5,  0.5, -0.5,
           0.5, -0.5, -0.5,
           -0.5, -0.5, 0.5,
           -0.5,  0.5, 0.5,
           0.5,  0.5, 0.5, 
           0.5, -0.5, 0.5,
           -0.5, -0.5, -0.5,
           -0.5, -0.5,  0.5,
           -0.5,  0.5,  0.5,
           -0.5,  0.5, -0.5,
           0.5, -0.5, -0.5,
           0.5, -0.5,  0.5,
           0.5,  0.5,  0.5,
           0.5,  0.5, -0.5,
        )

        cubeNormals = (
           0.0, -1.0, 0.0,
           0.0, -1.0, 0.0,
           0.0, -1.0, 0.0,
           0.0, -1.0, 0.0,
           0.0, 1.0, 0.0,
           0.0, 1.0, 0.0,
           0.0, 1.0, 0.0,
           0.0, 1.0, 0.0,
           0.0, 0.0, -1.0,
           0.0, 0.0, -1.0,
           0.0, 0.0, -1.0,
           0.0, 0.0, -1.0,
           0.0, 0.0, 1.0,
           0.0, 0.0, 1.0,
           0.0, 0.0, 1.0,
           0.0, 0.0, 1.0,
           -1.0, 0.0, 0.0,
           -1.0, 0.0, 0.0,
           -1.0, 0.0, 0.0,
           -1.0, 0.0, 0.0,
           1.0, 0.0, 0.0,
           1.0, 0.0, 0.0,
           1.0, 0.0, 0.0,
           1.0, 0.0, 0.0,
        )

        cubeTex = (
           0.0, 0.0,
           0.0, 1.0,
           1.0, 1.0,
           1.0, 0.0,
           1.0, 0.0,
           1.0, 1.0,
           0.0, 1.0,
           0.0, 0.0,
           0.0, 0.0,
           0.0, 1.0,
           1.0, 1.0,
           1.0, 0.0,
           0.0, 0.0,
           0.0, 1.0,
           1.0, 1.0,
           1.0, 0.0,
           0.0, 0.0,
           0.0, 1.0,
           1.0, 1.0,
           1.0, 0.0,
           0.0, 0.0,
           0.0, 1.0,
           1.0, 1.0,
           1.0, 0.0
        )

        cubeIndices = (
           0, 2, 1,
           0, 3, 2, 
           4, 5, 6,
           4, 6, 7,
           8, 9, 10,
           8, 10, 11, 
           12, 15, 14,
           12, 14, 13, 
           16, 17, 18,
           16, 18, 19, 
           20, 23, 22,
           20, 22, 21
        )

        return (tuple([x * scale for x in cubeVerts]) if vertices else None,
                cubeNormals if normals else None,
                cubeTex if texCoords else None, 
                cubeIndices if indices else None)

    def GetFps(self):
        """Get fps value
        @return: fps
        """
        return self.window.fps
    
    def SetFpsInterval(self, interval):
        """Set interval time to calculate fps
        @param interval: Interval time (millisecond)
        """
        if interval < 500:
            interval = 500

        self.window.interval = interval

class ESMatrix():
    def __init__(self, m=None):
        if not(m):
            self.m = [[0.0 for x in range(4)] for y in range(4)]
        else:
            self.m = m

    def LoadIdentity(self):
        self.m = [[0.0 for x in range(4)] for y in range(4)]
        for i in range(4):
            self.m[i][i] = 1.0

    def Frustum(self, left, right, bottom, top, nearZ, farZ):
        deltaX = right - left
        deltaY = top - bottom
        deltaZ = farZ - nearZ
        frust = ESMatrix()
    
        if nearZ <= 0.0 or farZ <= 0.0 or \
           deltaX <= 0.0 or deltaY <= 0.0 or deltaZ <= 0.0:
            return
    
        frust.m[0][0] = 2.0 * nearZ / deltaX
        frust.m[0][1] = 0.0
        frust.m[0][2] = 0.0
        frust.m[0][3] = 0.0

        frust.m[1][1] = 2.0 * nearZ / deltaY
        frust.m[1][0] = 0.0
        frust.m[1][2] = 0.0
        frust.m[1][3] = 0.0

        frust.m[2][0] = (right + left) / deltaX
        frust.m[2][1] = (top + bottom) / deltaY
        frust.m[2][2] = -(nearZ + farZ) / deltaZ
        frust.m[2][3] = -1.0

        frust.m[3][2] = -2.0 * nearZ * farZ / deltaZ
        frust.m[3][0] = 0.0
        frust.m[3][1] = 0.0
        frust.m[3][3] = 0.0

        self.m = frust.Multiply(self).m

    def Perspective(self, fovy, aspect, nearZ, farZ):
        frustumH = math.tan(fovy / 360.0 * math.pi) * nearZ;
        frustumW = frustumH * aspect;

        self.Frustum(-frustumW, frustumW, -frustumH, frustumH, nearZ, farZ)

    def Ortho(self, left, right, bottom, top, nearZ, farZ):
        pass
    
    def Scale(self, sx, sy, sz):
        self.m[0][0] *= sx
        self.m[0][1] *= sx
        self.m[0][2] *= sx
        self.m[0][3] *= sx
    
        self.m[1][0] *= sy
        self.m[1][1] *= sy
        self.m[1][2] *= sy
        self.m[1][3] *= sy
    
        self.m[2][0] *= sz
        self.m[2][1] *= sz
        self.m[2][2] *= sz
        self.m[2][3] *= sz

    def Translate(self, tx, ty, tz):
        self.m[3][0] += (self.m[0][0] * tx + self.m[1][0] * ty + self.m[2][0] * tz)
        self.m[3][1] += (self.m[0][1] * tx + self.m[1][1] * ty + self.m[2][1] * tz)
        self.m[3][2] += (self.m[0][2] * tx + self.m[1][2] * ty + self.m[2][2] * tz)
        self.m[3][3] += (self.m[0][3] * tx + self.m[1][3] * ty + self.m[2][3] * tz)

    def Rotate(self, angle, x, y, z):
        mag = math.sqrt(x * x + y * y + z * z)
           
        sinAngle = math.sin(angle * math.pi / 180.0)
        cosAngle = math.cos(angle * math.pi / 180.0)
        if mag > 0.0:
            rotMat = ESMatrix()
            
            x /= mag;
            y /= mag;
            z /= mag;
            
            xx = x * x;
            yy = y * y;
            zz = z * z;
            xy = x * y;
            yz = y * z;
            zx = z * x;
            xs = x * sinAngle;
            ys = y * sinAngle;
            zs = z * sinAngle;
            oneMinusCos = 1.0 - cosAngle;

            rotMat.m[0][0] = (oneMinusCos * xx) + cosAngle;
            rotMat.m[0][1] = (oneMinusCos * xy) - zs;
            rotMat.m[0][2] = (oneMinusCos * zx) + ys;
            rotMat.m[0][3] = 0.0; 
            
            rotMat.m[1][0] = (oneMinusCos * xy) + zs;
            rotMat.m[1][1] = (oneMinusCos * yy) + cosAngle;
            rotMat.m[1][2] = (oneMinusCos * yz) - xs;
            rotMat.m[1][3] = 0.0;
            
            rotMat.m[2][0] = (oneMinusCos * zx) - ys;
            rotMat.m[2][1] = (oneMinusCos * yz) + xs;
            rotMat.m[2][2] = (oneMinusCos * zz) + cosAngle;
            rotMat.m[2][3] = 0.0; 
            
            rotMat.m[3][0] = 0.0;
            rotMat.m[3][1] = 0.0;
            rotMat.m[3][2] = 0.0;
            rotMat.m[3][3] = 1.0;

            self.m = rotMat.Multiply(self).m

    def Multiply(self, rh):
        tmp = ESMatrix()
        for i in range(4):
            tmp.m[i][0] =   (self.m[i][0] * rh.m[0][0]) + \
                            (self.m[i][1] * rh.m[1][0]) + \
                            (self.m[i][2] * rh.m[2][0]) + \
                            (self.m[i][3] * rh.m[3][0])

            tmp.m[i][1] =   (self.m[i][0] * rh.m[0][1]) + \
                            (self.m[i][1] * rh.m[1][1]) + \
                            (self.m[i][2] * rh.m[2][1]) + \
                            (self.m[i][3] * rh.m[3][1])

            tmp.m[i][2] =   (self.m[i][0] * rh.m[0][2]) + \
                            (self.m[i][1] * rh.m[1][2]) + \
                            (self.m[i][2] * rh.m[2][2]) + \
                            (self.m[i][3] * rh.m[3][2])

            tmp.m[i][3] =   (self.m[i][0] * rh.m[0][3]) + \
                            (self.m[i][1] * rh.m[1][3]) + \
                            (self.m[i][2] * rh.m[2][3]) + \
                            (self.m[i][3] * rh.m[3][3])

        return tmp

    def pointer(self):
        arrays = (ctypes.c_float * (4 * 4))(*(self.m[0] + self.m[1] + self.m[2] + self.m[3]))
        return arrays
