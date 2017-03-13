# -*- coding: utf-8 -*-

import ctypes
import GLESv2Native as gles

def _make_list(src_list, array_type = gles.GLuint):
    if len(src_list):
        TypeArray = array_type * len(src_list)
        new_list = TypeArray(*src_list)
    else:
        new_list = 0
    return new_list

_num_of_params_get_api = {
    gles.GL_ALIASED_LINE_WIDTH_RANGE: 2,
    gles.GL_ALIASED_POINT_SIZE_RANGE: 2,
    gles.GL_BLEND_COLOR: 4,
    gles.GL_COLOR_CLEAR_VALUE: 4,
    gles.GL_COLOR_WRITEMASK: 4,
    gles.GL_COMPRESSED_TEXTURE_FORMATS: 0,
    gles.GL_MAX_VIEWPORT_DIMS: 2,
    gles.GL_SCISSOR_BOX: 4,
    gles.GL_SHADER_BINARY_FORMATS: 0,
    gles.GL_VIEWPORT: 4
    }

def glBufferData(target, data, usage):
    gles.glBufferData(target, len(data), ctypes.cast(data, ctypes.c_void_p), usage)

def glBufferSubData(target, offset, data):
    gles.glBufferSubData(target, len(data), ctypes.cast(data, ctypes.c_void_p))

def glCompressedTexImage2D(target, level, internalformat, width, height, border, data):
    gles.glCompressedTexImage2D(target, level, internalformat, width, height, border, len(data), ctypes.cast(data, ctypes.c_void_p))

def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data):
    gles.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, len(data), ctypes.cast(data, ctypes.c_void_p))

def glDeleteBuffers(buffers):
    n = len(buffers)
    gles.glDeleteBuffers(n, _make_list(buffers, gles.GLuint))

def glDeleteFramebuffers(framebuffers):
    n = len(framebuffers)
    gles.glDeleteFramebuffers(n, _make_list(framebuffers, gles.GLuint))

def glDeleteRenderbuffers(renderbuffers):
    n = len(renderbuffers)
    gles.glDeleteRenderbuffers(n, _make_list(renderbuffers, gles.GLuint))

def glDeleteTextures(textures):
    n = len(textures)
    gles.glDeleteTextures(n, _make_list(textures, gles.GLuint))

def glDrawElementsub(mode, indices):
    count = len(indices)
    gles.glDrawElements(mode, count, gles.GL_UNSIGNED_BYTE, ctypes.cast((gles.GLubyte * count)(*indices), ctypes.c_void_p))

def glDrawElementsus(mode, indices):
    count = len(indices)
    gles.glDrawElements(mode, count, gles.GL_UNSIGNED_SHORT, ctypes.cast((gles.GLushort * count)(*indices), ctypes.c_void_p))

def glGenBuffers(n):
    buffers = (gles.GLuint * n)()
    gles.glGenBuffers(n, buffers)
    return [x for x in buffers]

def glGenFramebuffers(n):
    framebuffers = (gles.GLuint * n)()
    gles.glGenFramebuffers(n, framebuffers)
    return [x for x in framebuffers]

def glGenRenderbuffers(n):
    renderbuffers = (gles.GLuint * n)()
    gles.glGenRenderbuffers(n, renderbuffers)
    return [x for x in renderbuffers]

def glGenTextures(n):
    textures = (gles.GLuint * n)()
    gles.glGenTextures(n, textures)
    return [x for x in textures]

def glGetActiveAttrib(program, index, bufsize):
    length = gles.GLsizei()
    size = gles.GLint()
    type = gles.GLenum()
    name = ctypes.create_string_buffer(bufsize)
    gles.glGetActiveAttrib(program, index, bufsize, ctypes.byref(length), ctypes.byref(size), ctypes.byref(type), name)
    return (size.value, type.value, ctypes.cast(name, ctypes.c_char_p).value)

def glGetActiveUniform(program, index, bufsize):
    length = gles.GLsizei()
    size = gles.GLint()
    type = gles.GLenum()
    name = ctypes.create_string_buffer(bufsize)
    gles.glGetActiveUniform(program, index, bufsize, ctypes.byref(length), ctypes.byref(size), ctypes.byref(type), name)
    return (size.value, type.value, ctypes.cast(name, ctypes.c_char_p).value)

def glGetAttachedShaders(program, maxcount):
    count = gles.GLsizei()
    shaders = (gles.GLuint * maxcount)()
    gles.glGetAttachedShaders(program, maxcount, ctypes.byref(count), shaders)
    return [x for x in shaders[:count]]

def glGetAttribLocation(program, name):
    return gles.glGetAttribLocation(program, name)

def glGetBooleanv(pname):
    if _num_of_params_get_api.has_key(pname):
        count = _num_of_params_get_api[pname]
    else:
        count = 1
    if 0 == count:
        return False
    params = (gles.GLboolean * count)()
    gles.glGetBooleanv(pname, params)
    return [x for x in params]

def glGetBufferParameteriv(target, pname):
    params = gles.GLint()
    gles.glGetBufferParameteriv(target, pname, ctypes.byref(params))
    return params.value

def glGetFloatv(pname):
    if _num_of_params_get_api.has_key(pname):
        count = _num_of_params_get_api[pname]
    else:
        count = 1
    if 0 == count:
        return 0.0
    params = (gles.GLfloat * count)()
    gles.glGetFloatv(pname, params)
    return [x for x in params]

def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
    params = gles.GLint()
    gles.glGetFramebufferAttachmentParameteriv(target, attachment, pname, ctypes.byref(params))
    return params.value

def glGetIntegerv(pname):
    if _num_of_params_get_api.has_key(pname):
        count = _num_of_params_get_api[pname]
    else:
        count = 1
    if 0 == count:
        return 0
    params = (gles.GLint * count)()
    gles.glGetIntegerv(pname, params)
    return [x for x in params]

def glGetProgramiv(target, pname):
    params = gles.GLint()
    gles.glGetProgramiv(target,  pname, ctypes.byref(params))
    return params.value

def glGetProgramInfoLog(program, bufsize):
    length = gles.GLsizei()
    infolog = ctypes.create_string_buffer(bufsize)
    gles.glGetProgramInfoLog(program, bufsize, ctypes.byref(length), infolog)
    return ctypes.cast(infolog, ctypes.c_char_p).value

def glGetRenderbufferParameteriv(target, pname):
    params = gles.GLint()
    gles.glGetRenderbufferParameteriv(target,  pname, ctypes.byref(params))
    return params.value

def glGetShaderiv(target, pname):
    params = gles.GLint()
    gles.glGetShaderiv(target,  pname, ctypes.byref(params))
    return params.value

def glGetShaderInfoLog(shader, bufsize):
    length = gles.GLsizei()
    infolog = ctypes.create_string_buffer(bufsize)
    gles.glGetShaderInfoLog(shader, bufsize, ctypes.byref(length), infolog)
    return ctypes.cast(infolog, ctypes.c_char_p).value

def glGetShaderPrecisionFormat(shadertype, precisiontype):
    range = (gles.GLint * 2)()
    precision = gles.GLint()
    gles.glGetShaderPrecisionFormat(shadertype,  precisiontype, range, ctypes.byref(precision))
    return (range.value[0], range.value[1], precision)

def glGetShaderSource(shader, bufsize):
    length = gles.GLsizei()
    source = ctypes.create_string_buffer(bufsize)
    gles.glGetShaderInfoLog(shader, bufsize, ctypes.byref(length), source)
    return ctypes.cast(source, ctypes.c_char_p).value

def glGetTexParameterfv(target, pname):
    params = gles.GLfloat()
    gles.glGetTexParameterfv(target,  pname, ctypes.byref(params))
    return params.value

def glGetTexParameteriv(target, pname):
    params = gles.GLint()
    gles.glGetTexParameteriv(target,  pname, ctypes.byref(params))
    return params.value

def glGetVertexAttribfv(target, pname):
    params = gles.GLfloat()
    gles.glGetVertexAttribfv(target,  pname, ctypes.byref(params))
    return params.value

def glGetVertexAttribiv(target, pname):
    params = gles.GLint()
    gles.glGetVertexAttribiv(target,  pname, ctypes.byref(params))
    return params.value

def glGetVertexAttribPointerv(index, pname):
    pointer = ctypes.c_void_p()
    gles.glGetVertexAttribPointerv(index, pname, ctypes.byref(pointer))
    return pointer.value

_byte_per_pixel = {
    gles.GL_UNSIGNED_BYTE: 0,
    gles.GL_UNSIGNED_SHORT_5_6_5: 2,
    gles.GL_UNSIGNED_SHORT_4_4_4_4: 2,
    gles.GL_UNSIGNED_SHORT_5_5_5_1: 2
}
_byte_per_pixel_2 = {
    gles.GL_ALPHA: 1,
    gles.GL_RGB: 3,
    gles.GL_RGBA: 4,
}

def glReadPixels(x, y, width, height, format, type):
    bpp = _byte_per_pixel[type]
    if bpp == 0:
        bpp = _byte_per_pixel_2[format]
    count = width * height * bpp
    pixels = ctypes.create_string_buffer(count)
    gles.glReadPixels(x, y, width, height, format, type, pixels)
    return pixels.value

# initializer
_num_of_params_get_api[gles.GL_COMPRESSED_TEXTURE_FORMATS] = glGetIntegerv(gles.GL_NUM_COMPRESSED_TEXTURE_FORMATS)
_num_of_params_get_api[gles.GL_NUM_SHADER_BINARY_FORMATS] = glGetIntegerv(gles.GL_NUM_SHADER_BINARY_FORMATS)
