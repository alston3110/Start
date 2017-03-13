# -*- coding: utf-8 -*-

import ctypes
import EGLNative as egl

def _RaiseError(value):
    if value == egl.EGL_FALSE:
        raise

def _make_list(src_list, array_type = egl.EGLint):
    if len(src_list):
        TypeArray = array_type * len(src_list)
        new_list = TypeArray(*src_list)
    else:
        new_list = 0
    return new_list

def eglInitialize(dpy):
    """eglInitialize(dpy) -> (major, minor)

    Initialize an EGL display connection.
    eglInitialize() returns a tuple of version. If error occured, raise exception.

    This function is different from native EGL.
    """
    major = egl.EGLint()
    minor = egl.EGLint()

    ret = egl.eglInitialize(dpy, ctypes.byref(major), ctypes.byref(minor))
    _RaiseError(ret)
    return (major.value, minor.value)

def eglGetConfigs(dpy, config_size):
    """eglGetConfigs(dpy, config_size) -> [config]

    Return a list of all EGL frame buffer configurations for a display.
    eglGetConfigs() returns a list of config. If error occured, raise exception.

    This function is different from native EGL.
    """
    EGLConfigArray = egl.EGLConfig * config_size
    configs = EGLConfigArray()
    num_config = egl.EGLint()
    ret = egl.eglGetConfigs(dpy, configs, config_size, ctypes.byref(num_config))
    _RaiseError(ret)
    return [x.value for x in configs[:num_config]]

def eglChooseConfig(dpy, attrib_list, config_size):
    """eglGetConfigs(dpy, config_size) -> [config]

    Return a list of EGL frame buffer configurations that match specified attributes.
    eglChooseConfig() returns a list of config. If error occured, raise exception.

    This function is different from native EGL.
    """
    new_attrib_list = _make_list(attrib_list)
    EGLConfigArray = egl.EGLConfig * config_size
    configs = EGLConfigArray()
    num_config = egl.EGLint()
    ret = egl.eglChooseConfig(dpy, new_attrib_list, configs, config_size, ctypes.byref(num_config))
    _RaiseError(ret)
    return [x.value for x in configs]

def eglGetConfigAttrib(dpy, config, attribute):
    """eglGetConfigAttrib(dpy, config, attribute) -> value

    Return information about an EGL frame buffer configuration.
    If error occured, raise exception.

    This function is different from native EGL.
    """
    value = egl.EGLint()
    ret = egl.eglGetConfigAttrib(dpy, config, attribute, ctypes.byref(value))
    _RaiseError(ret)
    return value.value

def eglCreateWindowSurface(dpy, config, win, attrib_list):
    return egl.eglCreateWindowSurface(dpy, config, win, _make_list(attrib_list))

def eglCreatePbufferSurface(dpy, config, attrib_list):
    return egl.eglCreatePbufferSurface(dpy, config, _make_list(attrib_list))

def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list):
    return egl.eglCreatePixmapSurface(dpy, config, _make_list(attrib_list))

def eglQuerySurface(dpy, surface, attribute):
    """eglQuerySurface(dpy, surface, attribute) -> value

    Return EGL surface information.
    If error occured, raise exception.

    This function is different from native EGL.
    """
    value = egl.EGLint()
    ret = egl.eglQuerySurface(dpy, surface, attribute, ctypes.byref(value))
    _RaiseError(ret)
    return ret

def eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attrib_list):
    return egl.eglCreatePbufferFromClientBuffer(dpy, buffer, config, _make_list(attrib_list))

def eglCreateContext(dpy, config, share_context, attrib_list):
    return egl.eglCreateContext(dpy, buffer, config, _make_list(attrib_list))

#eglQueryContext = _eglQueryContext
def eglQueryContext(dpy, ctx, attribute):
    """eglQueryContext(dpy, ctx, attribute) -> value

    Return EGL rendering context information.
    If error occured, raise exception.

    This function is different from native EGL.
    """
    value = egl.EGLint()
    ret = egl.eglQueryContext(dpy, ctx, attribute, ctypes.byref(value))
    _RaiseError(ret)
    return value.value
