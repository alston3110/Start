# -*- coding: utf-8 -*-
from ctypes import *
import ctypes
import os

libName = 'libEGL.so'
egldll = CDLL(libName)


EGLBoolean = ctypes.c_uint32
EGLenum = ctypes.c_uint32
EGLint = ctypes.c_int32
EGLuint = ctypes.c_uint32
EGLConfig = ctypes.c_void_p
EGLContext = ctypes.c_void_p
EGLDisplay = ctypes.c_void_p
EGLSurface = ctypes.c_void_p
EGLClientBuffer = ctypes.c_void_p
EGLNativeDisplayType = ctypes.c_void_p
EGLNativePixmapType = ctypes.c_void_p
EGLNativeWindowType = ctypes.c_void_p


EGL_VERSION_1_0 = 1
EGL_VERSION_1_1 = 1
EGL_VERSION_1_2 = 1
EGL_VERSION_1_3 = 1
EGL_VERSION_1_4 = 1
EGL_FALSE = 0
EGL_TRUE = 1
EGL_DEFAULT_DISPLAY = EGLDisplay(0)
EGL_NO_CONTEXT = EGLContext(0)
EGL_NO_DISPLAY = EGLDisplay(0)
EGL_NO_SURFACE = EGLSurface(0)
EGL_DONT_CARE = -1
EGL_SUCCESS = 0x3000
EGL_NOT_INITIALIZED = 0x3001
EGL_BAD_ACCESS = 0x3002
EGL_BAD_ALLOC = 0x3003
EGL_BAD_ATTRIBUTE = 0x3004
EGL_BAD_CONFIG = 0x3005
EGL_BAD_CONTEXT = 0x3006
EGL_BAD_CURRENT_SURFACE = 0x3007
EGL_BAD_DISPLAY = 0x3008
EGL_BAD_MATCH = 0x3009
EGL_BAD_NATIVE_PIXMAP = 0x300A
EGL_BAD_NATIVE_WINDOW = 0x300B
EGL_BAD_PARAMETER = 0x300C
EGL_BAD_SURFACE = 0x300D
EGL_CONTEXT_LOST = 0x300E
EGL_BUFFER_SIZE = 0x3020
EGL_ALPHA_SIZE = 0x3021
EGL_BLUE_SIZE = 0x3022
EGL_GREEN_SIZE = 0x3023
EGL_RED_SIZE = 0x3024
EGL_DEPTH_SIZE = 0x3025
EGL_STENCIL_SIZE = 0x3026
EGL_CONFIG_CAVEAT = 0x3027
EGL_CONFIG_ID = 0x3028
EGL_LEVEL = 0x3029
EGL_MAX_PBUFFER_HEIGHT = 0x302A
EGL_MAX_PBUFFER_PIXELS = 0x302B
EGL_MAX_PBUFFER_WIDTH = 0x302C
EGL_NATIVE_RENDERABLE = 0x302D
EGL_NATIVE_VISUAL_ID = 0x302E
EGL_NATIVE_VISUAL_TYPE = 0x302F
EGL_SAMPLES = 0x3031
EGL_SAMPLE_BUFFERS = 0x3032
EGL_SURFACE_TYPE = 0x3033
EGL_TRANSPARENT_TYPE = 0x3034
EGL_TRANSPARENT_BLUE_VALUE = 0x3035
EGL_TRANSPARENT_GREEN_VALUE = 0x3036
EGL_TRANSPARENT_RED_VALUE = 0x3037
EGL_NONE = 0x3038
EGL_BIND_TO_TEXTURE_RGB = 0x3039
EGL_BIND_TO_TEXTURE_RGBA = 0x303A
EGL_MIN_SWAP_INTERVAL = 0x303B
EGL_MAX_SWAP_INTERVAL = 0x303C
EGL_LUMINANCE_SIZE = 0x303D
EGL_ALPHA_MASK_SIZE = 0x303E
EGL_COLOR_BUFFER_TYPE = 0x303F
EGL_RENDERABLE_TYPE = 0x3040
EGL_MATCH_NATIVE_PIXMAP = 0x3041
EGL_CONFORMANT = 0x3042
EGL_SLOW_CONFIG = 0x3050
EGL_NON_CONFORMANT_CONFIG = 0x3051
EGL_TRANSPARENT_RGB = 0x3052
EGL_RGB_BUFFER = 0x308E
EGL_LUMINANCE_BUFFER = 0x308F
EGL_NO_TEXTURE = 0x305C
EGL_TEXTURE_RGB = 0x305D
EGL_TEXTURE_RGBA = 0x305E
EGL_TEXTURE_2D = 0x305F
EGL_PBUFFER_BIT = 0x0001
EGL_PIXMAP_BIT = 0x0002
EGL_WINDOW_BIT = 0x0004
EGL_VG_COLORSPACE_LINEAR_BIT = 0x0020
EGL_VG_ALPHA_FORMAT_PRE_BIT = 0x0040
EGL_MULTISAMPLE_RESOLVE_BOX_BIT = 0x0200
EGL_SWAP_BEHAVIOR_PRESERVED_BIT = 0x0400
EGL_OPENGL_ES_BIT = 0x0001
EGL_OPENVG_BIT = 0x0002
EGL_OPENGL_ES2_BIT = 0x0004
EGL_OPENGL_BIT = 0x0008
EGL_VENDOR = 0x3053
EGL_VERSION = 0x3054
EGL_EXTENSIONS = 0x3055
EGL_CLIENT_APIS = 0x308D
EGL_HEIGHT = 0x3056
EGL_WIDTH = 0x3057
EGL_LARGEST_PBUFFER = 0x3058
EGL_TEXTURE_FORMAT = 0x3080
EGL_TEXTURE_TARGET = 0x3081
EGL_MIPMAP_TEXTURE = 0x3082
EGL_MIPMAP_LEVEL = 0x3083
EGL_RENDER_BUFFER = 0x3086
EGL_VG_COLORSPACE = 0x3087
EGL_VG_ALPHA_FORMAT = 0x3088
EGL_HORIZONTAL_RESOLUTION = 0x3090
EGL_VERTICAL_RESOLUTION = 0x3091
EGL_PIXEL_ASPECT_RATIO = 0x3092
EGL_SWAP_BEHAVIOR = 0x3093
EGL_MULTISAMPLE_RESOLVE = 0x3099
EGL_BACK_BUFFER = 0x3084
EGL_SINGLE_BUFFER = 0x3085
EGL_VG_COLORSPACE_sRGB = 0x3089
EGL_VG_COLORSPACE_LINEAR = 0x308A
EGL_VG_ALPHA_FORMAT_NONPRE = 0x308B
EGL_VG_ALPHA_FORMAT_PRE = 0x308C
EGL_DISPLAY_SCALING = 10000
EGL_BUFFER_PRESERVED = 0x3094
EGL_BUFFER_DESTROYED = 0x3095
EGL_OPENVG_IMAGE = 0x3096
EGL_CONTEXT_CLIENT_TYPE = 0x3097
EGL_CONTEXT_CLIENT_VERSION = 0x3098
EGL_MULTISAMPLE_RESOLVE_DEFAULT = 0x309A
EGL_MULTISAMPLE_RESOLVE_BOX = 0x309B
EGL_OPENGL_ES_API = 0x30A0
EGL_OPENVG_API = 0x30A1
EGL_OPENGL_API = 0x30A2
EGL_DRAW = 0x3059
EGL_READ = 0x305A
EGL_CORE_NATIVE_ENGINE = 0x305B
EGL_COLORSPACE = EGL_VG_COLORSPACE
EGL_ALPHA_FORMAT = EGL_VG_ALPHA_FORMAT
EGL_COLORSPACE_sRGB = EGL_VG_COLORSPACE_sRGB
EGL_COLORSPACE_LINEAR = EGL_VG_COLORSPACE_LINEAR
EGL_ALPHA_FORMAT_NONPRE = EGL_VG_ALPHA_FORMAT_NONPRE
EGL_ALPHA_FORMAT_PRE = EGL_VG_ALPHA_FORMAT_PRE

# EGLNativeDisplayType fbGetDisplay( void *context );
fbGetDisplay = egldll.fbGetDisplay
fbGetDisplay.argtypes = (EGLContext,)
fbGetDisplay.restype = EGLNativeDisplayType

# EGLNativeDisplayType fbGetDisplayByIndex( int DisplayIndex );
fbGetDisplayByIndex = egldll.fbGetDisplayByIndex
fbGetDisplayByIndex.argtypes = (EGLint,)
fbGetDisplayByIndex.restype = EGLNativeDisplayType

# void fbGetDisplayGeometry( EGLNativeDisplayType Display, int * Width, int * Height );
fbGetDisplayGeometry = egldll.fbGetDisplayGeometry
fbGetDisplayGeometry.argtypes = (EGLNativeDisplayType,ctypes.POINTER(EGLint), ctypes.POINTER(EGLint))
fbGetDisplayGeometry.restype = None

# void fbGetDisplayInfo(EGLNativeDisplayType Display, int * Width, int * Height, unsigned long * Physical, int * Stride, int * BitsPerPixel );
fbGetDisplayInfo = egldll.fbGetDisplayInfo
fbGetDisplayInfo.argtypes = (EGLNativeDisplayType,ctypes.POINTER(EGLint), ctypes.POINTER(EGLint),ctypes.POINTER(EGLuint),ctypes.POINTER(EGLint), ctypes.POINTER(EGLint))
fbGetDisplayInfo.restype = None

# void fbDestroyDisplay( EGLNativeDisplayType Display );
fbDestroyDisplay = egldll.fbDestroyDisplay
fbDestroyDisplay.argtypes = (EGLNativeDisplayType,)
fbDestroyDisplay.restype = None

# EGLNativeWindowType fbCreateWindow( EGLNativeDisplayType Display, int X, int Y, int Width, int Height );
fbCreateWindow = egldll.fbCreateWindow
fbCreateWindow.argtypes = (EGLNativeDisplayType, EGLint, EGLint, EGLint, EGLint)
fbCreateWindow.restype = EGLNativeWindowType

# void fbGetWindowGeometry( EGLNativeWindowType Window, int * X, int * Y, int * Width, int * Height );
fbGetWindowGeometry = egldll.fbGetWindowGeometry
fbGetWindowGeometry.argtypes = (EGLNativeWindowType,ctypes.POINTER(EGLint), ctypes.POINTER(EGLint), ctypes.POINTER(EGLint), ctypes.POINTER(EGLint))
fbGetWindowGeometry.restype = None

# void fbGetWindowInfo( EGLNativeWindowType Window, int * X, int * Y, int * Width, int * Height, int * BitsPerPixel, unsigned int * Offset );
fbGetWindowInfo = egldll.fbGetWindowInfo
fbGetWindowInfo.argtypes = (EGLNativeWindowType,ctypes.POINTER(EGLint), ctypes.POINTER(EGLint),ctypes.POINTER(EGLint), ctypes.POINTER(EGLint), ctypes.POINTER(EGLint),ctypes.POINTER(EGLuint))
fbGetWindowInfo.restype = None

# void fbDestroyWindow( EGLNativeWindowType Window );
fbDestroyWindow = egldll.fbDestroyWindow
fbDestroyWindow.argtypes = (EGLNativeWindowType,)
fbDestroyWindow.restype = None

# EGLNativePixmapType fbCreatePixmap( EGLNativeDisplayType Display, int Width, int Height);
#fbCreatePixmapWithBpp = egldll.fbCreatePixmapWithBpp

# EGLNativePixmapType fbCreatePixmapWithBpp( EGLNativeDisplayType Display, int Width, int Height, int BitsPerPixel );
#fbGetPixmapGeometry = egldll.fbGetPixmapGeometry

# void fbGetPixmapGeometry( EGLNativePixmapType Pixmap, int * Width, int * Height );
#fbGetPixmapInfo = egldll.fbGetPixmapInfo

# void fbGetPixmapInfo( EGLNativePixmapType Pixmap, int * Width, int * Height, int * BitsPerPixel, int * Stride, void ** Bits );

# void fbDestroyPixmap( EGLNativePixmapType Pixmap );
#fbDestroyPixmap = egldll.fbDestroyPixmap

# EGLAPI EGLint EGLAPIENTRY eglGetError(void);
eglGetError = egldll.eglGetError
eglGetError.argtypes = None
eglGetError.restype = EGLint

# EGLAPI EGLDisplay EGLAPIENTRY eglGetDisplay(EGLNativeDisplayType display_id);
eglGetDisplay = egldll.eglGetDisplay
eglGetDisplay.argtypes = (EGLNativeDisplayType,)
eglGetDisplay.restype = EGLDisplay

# EGLAPI EGLBoolean EGLAPIENTRY eglInitialize(EGLDisplay dpy, EGLint *major, EGLint *minor);
eglInitialize = egldll.eglInitialize
eglInitialize.argtypes = (EGLDisplay, ctypes.POINTER(EGLint), ctypes.POINTER(EGLint))
eglInitialize.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglTerminate(EGLDisplay dpy);
eglTerminate = egldll.eglTerminate
eglTerminate.argtypes = (EGLDisplay,)
eglTerminate.restype = EGLBoolean

# EGLAPI const char * EGLAPIENTRY eglQueryString(EGLDisplay dpy, EGLint name);
eglQueryString = egldll.eglQueryString
eglQueryString.argtypes = (EGLDisplay, EGLint)
eglQueryString.restype = ctypes.c_char_p

# EGLAPI EGLBoolean EGLAPIENTRY eglGetConfigs(EGLDisplay dpy, EGLConfig *configs,
#              EGLint config_size, EGLint *num_config);
eglGetConfigs = egldll.eglGetConfigs
eglGetConfigs.argtypes = (EGLDisplay, ctypes.POINTER(EGLConfig), EGLint, ctypes.POINTER(EGLint))
eglGetConfigs.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglChooseConfig(EGLDisplay dpy, const EGLint *attrib_list,
#                EGLConfig *configs, EGLint config_size,
#                EGLint *num_config);
eglChooseConfig = egldll.eglChooseConfig
eglChooseConfig.argtypes = (EGLDisplay, ctypes.POINTER(EGLint), ctypes.POINTER(EGLConfig), EGLint, ctypes.POINTER(EGLint))
eglChooseConfig.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglGetConfigAttrib(EGLDisplay dpy, EGLConfig config,
#                   EGLint attribute, EGLint *value);
eglGetConfigAttrib = egldll.eglGetConfigAttrib
eglGetConfigAttrib.argtypes = (EGLDisplay, EGLConfig, EGLint, ctypes.POINTER(EGLint))
eglGetConfigAttrib.restype = EGLBoolean

# EGLAPI EGLSurface EGLAPIENTRY eglCreateWindowSurface(EGLDisplay dpy, EGLConfig config,
#                   EGLNativeWindowType win,
#                   const EGLint *attrib_list);
eglCreateWindowSurface = egldll.eglCreateWindowSurface
eglCreateWindowSurface.argtypes = (EGLDisplay, EGLConfig, EGLNativeWindowType, ctypes.POINTER(EGLint))
eglCreateWindowSurface.restype = EGLSurface

# EGLAPI EGLSurface EGLAPIENTRY eglCreatePbufferSurface(EGLDisplay dpy, EGLConfig config,
#                    const EGLint *attrib_list);
eglCreatePbufferSurface = egldll.eglCreatePbufferSurface
eglCreatePbufferSurface.argtypes = (EGLDisplay, EGLConfig, ctypes.POINTER(EGLint))
eglCreatePbufferSurface.restype = EGLSurface

# EGLAPI EGLSurface EGLAPIENTRY eglCreatePixmapSurface(EGLDisplay dpy, EGLConfig config,
#                   EGLNativePixmapType pixmap,
#                   const EGLint *attrib_list);
eglCreatePixmapSurface = egldll.eglCreatePixmapSurface
eglCreatePixmapSurface.argtypes = (EGLDisplay, EGLConfig, EGLNativePixmapType, ctypes.POINTER(EGLint))
eglCreatePixmapSurface.restype = EGLSurface

# EGLAPI EGLBoolean EGLAPIENTRY eglDestroySurface(EGLDisplay dpy, EGLSurface surface);
eglDestroySurface = egldll.eglDestroySurface
eglDestroySurface.argtypes = (EGLDisplay, EGLSurface)
eglDestroySurface.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglQuerySurface(EGLDisplay dpy, EGLSurface surface,
#                EGLint attribute, EGLint *value);
eglQuerySurface = egldll.eglQuerySurface
eglQuerySurface.argtypes = (EGLDisplay, EGLSurface, EGLint, ctypes.POINTER(EGLint))
eglQuerySurface.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglBindAPI(EGLenum api);
eglBindAPI = egldll.eglBindAPI
eglBindAPI.argtypes = (EGLenum,)
eglBindAPI.restype = EGLBoolean

# EGLAPI EGLenum EGLAPIENTRY eglQueryAPI(void);
eglQueryAPI = egldll.eglQueryAPI
eglQueryAPI.argtypes = None
eglQueryAPI.restype = EGLenum

# EGLAPI EGLBoolean EGLAPIENTRY eglWaitClient(void);
eglWaitClient = egldll.eglWaitClient
eglWaitClient.argtypes = None
eglWaitClient.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglReleaseThread(void);
eglReleaseThread = egldll.eglReleaseThread
eglReleaseThread.argtypes = None
eglReleaseThread.restype = EGLBoolean

# EGLAPI EGLSurface EGLAPIENTRY eglCreatePbufferFromClientBuffer(
#           EGLDisplay dpy, EGLenum buftype, EGLClientBuffer buffer,
#           EGLConfig config, const EGLint *attrib_list);
eglCreatePbufferFromClientBuffer = egldll.eglCreatePbufferFromClientBuffer
eglCreatePbufferFromClientBuffer.argtypes = (EGLDisplay, EGLenum, EGLClientBuffer, EGLConfig, ctypes.POINTER(EGLint))
eglCreatePbufferFromClientBuffer.restype = EGLSurface

# EGLAPI EGLBoolean EGLAPIENTRY eglSurfaceAttrib(EGLDisplay dpy, EGLSurface surface,
#                EGLint attribute, EGLint value);
eglSurfaceAttrib = egldll.eglSurfaceAttrib
eglSurfaceAttrib.argtypes = (EGLDisplay, EGLSurface, EGLint, EGLint)
eglSurfaceAttrib.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglBindTexImage(EGLDisplay dpy, EGLSurface surface, EGLint buffer);
eglBindTexImage = egldll.eglBindTexImage
eglBindTexImage.argtypes = (EGLDisplay, EGLSurface, EGLint)
eglBindTexImage.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglReleaseTexImage(EGLDisplay dpy, EGLSurface surface, EGLint buffer);
eglReleaseTexImage = egldll.eglReleaseTexImage
eglReleaseTexImage.argtypes = (EGLDisplay, EGLSurface, EGLint)
eglReleaseTexImage.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglSwapInterval(EGLDisplay dpy, EGLint interval);
eglSwapInterval = egldll.eglSwapInterval
eglSwapInterval.argtypes = (EGLDisplay, EGLint)
eglSwapInterval.restype = EGLBoolean

# EGLAPI EGLContext EGLAPIENTRY eglCreateContext(EGLDisplay dpy, EGLConfig config,
#                 EGLContext share_context,
#                 const EGLint *attrib_list);
eglCreateContext = egldll.eglCreateContext
eglCreateContext.argtypes = (EGLDisplay, EGLConfig, EGLContext, ctypes.POINTER(EGLint))
eglCreateContext.restype = EGLContext

# EGLAPI EGLBoolean EGLAPIENTRY eglDestroyContext(EGLDisplay dpy, EGLContext ctx);
eglDestroyContext = egldll.eglDestroyContext
eglDestroyContext.argtypes = (EGLDisplay, EGLContext)
eglDestroyContext.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglMakeCurrent(EGLDisplay dpy, EGLSurface draw,
#               EGLSurface read, EGLContext ctx);
eglMakeCurrent = egldll.eglMakeCurrent
eglMakeCurrent.argtypes = (EGLDisplay, EGLSurface, EGLSurface, EGLContext)
eglMakeCurrent.restype = EGLBoolean

# EGLAPI EGLContext EGLAPIENTRY eglGetCurrentContext(void);
eglGetCurrentContext = egldll.eglGetCurrentContext
eglGetCurrentContext.argtypes = None
eglGetCurrentContext.restype = EGLContext

# EGLAPI EGLSurface EGLAPIENTRY eglGetCurrentSurface(EGLint readdraw);
eglGetCurrentSurface = egldll.eglGetCurrentSurface
eglGetCurrentSurface.argtypes = (EGLint,)
eglGetCurrentSurface.restype = EGLSurface

# EGLAPI EGLDisplay EGLAPIENTRY eglGetCurrentDisplay(void);
eglGetCurrentDisplay = egldll.eglGetCurrentDisplay
eglGetCurrentDisplay.argtypes = None
eglGetCurrentDisplay.restype = EGLDisplay

# EGLAPI EGLBoolean EGLAPIENTRY eglQueryContext(EGLDisplay dpy, EGLContext ctx,
#                EGLint attribute, EGLint *value);
eglQueryContext = egldll.eglQueryContext
eglQueryContext.argtypes = (EGLDisplay, EGLContext, EGLint, ctypes.POINTER(EGLint))
eglQueryContext.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglWaitGL(void);
eglWaitGL = egldll.eglWaitGL
eglWaitGL.argtypes = None
eglWaitGL.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglWaitNative(EGLint engine);
eglWaitNative = egldll.eglWaitNative
eglWaitNative.argtypes = (EGLint,)
eglWaitNative.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglSwapBuffers(EGLDisplay dpy, EGLSurface surface);
eglSwapBuffers = egldll.eglSwapBuffers
eglSwapBuffers.argtypes = (EGLDisplay, EGLSurface)
eglSwapBuffers.restype = EGLBoolean

# EGLAPI EGLBoolean EGLAPIENTRY eglCopyBuffers(EGLDisplay dpy, EGLSurface surface,
#               EGLNativePixmapType target);
eglCopyBuffers = egldll.eglCopyBuffers
eglCopyBuffers.argtypes = (EGLDisplay, EGLSurface, EGLNativePixmapType)
eglCopyBuffers.restype = EGLBoolean

#typedef void (*__eglMustCastToProperFunctionPointerType)(void);
#
#/* Now, define eglGetProcAddress using the generic function ptr. type */
#EGLAPI __eglMustCastToProperFunctionPointerType EGLAPIENTRY
#       eglGetProcAddress(const char *procname);
eglGetProcAddress = egldll.eglGetProcAddress
eglGetProcAddress.argtypes = (ctypes.c_char_p,)
eglGetProcAddress.restype = ctypes.c_void_p
