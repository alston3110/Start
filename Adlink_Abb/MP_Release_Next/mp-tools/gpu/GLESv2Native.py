# -*- coding: utf-8 -*-
from ctypes import *
import ctypes
import os

libName = 'libGLESv2.so'
glesdll = CDLL(libName)

#typedef void             GLvoid;
#typedef char             GLchar;
GLchar = ctypes.c_char
GLenum = ctypes.c_uint32
GLboolean = ctypes.c_uint8
GLbitfield = ctypes.c_uint32
GLbyte = ctypes.c_int8
GLshort = ctypes.c_int16
GLint = ctypes.c_int32
GLsizei = ctypes.c_int32
GLubyte = ctypes.c_uint8
GLushort = ctypes.c_uint16
GLuint = ctypes.c_uint32
GLfloat = ctypes.c_float
GLclampf = ctypes.c_float
GLfixed = ctypes.c_int32
GLintptr = ctypes.c_int32
GLsizeiptr = ctypes.c_int32


GL_ES_VERSION_2_0 = 1
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_FUNC_ADD = 0x8006
GL_BLEND_EQUATION = 0x8009
GL_BLEND_EQUATION_RGB = 0x8009
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
GL_BLEND_COLOR = 0x8005
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_STREAM_DRAW = 0x88E0
GL_STATIC_DRAW = 0x88E4
GL_DYNAMIC_DRAW = 0x88E8
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_FRONT_AND_BACK = 0x0408
GL_TEXTURE_2D = 0x0DE1
GL_CULL_FACE = 0x0B44
GL_BLEND = 0x0BE2
GL_DITHER = 0x0BD0
GL_STENCIL_TEST = 0x0B90
GL_DEPTH_TEST = 0x0B71
GL_SCISSOR_TEST = 0x0C11
GL_POLYGON_OFFSET_FILL = 0x8037
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_COVERAGE = 0x80A0
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_LINE_WIDTH = 0x0B21
GL_ALIASED_POINT_SIZE_RANGE = 0x846D
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_WRITEMASK = 0x0B98
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
GL_VIEWPORT = 0x0BA2
GL_SCISSOR_BOX = 0x0C10
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_RED_BITS = 0x0D52
GL_GREEN_BITS = 0x0D53
GL_BLUE_BITS = 0x0D54
GL_ALPHA_BITS = 0x0D55
GL_DEPTH_BITS = 0x0D56
GL_STENCIL_BITS = 0x0D57
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_2D = 0x8069
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_GENERATE_MIPMAP_HINT = 0x8192
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_FIXED = 0x140C
GL_DEPTH_COMPONENT = 0x1902
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_LUMINANCE = 0x1909
GL_LUMINANCE_ALPHA = 0x190A
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
GL_MAX_VARYING_VECTORS = 0x8DFC
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
GL_SHADER_TYPE = 0x8B4F
GL_DELETE_STATUS = 0x8B80
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_CURRENT_PROGRAM = 0x8B8D
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_INVERT = 0x150A
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_TEXTURE = 0x1702
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_REPEAT = 0x2901
GL_CLAMP_TO_EDGE = 0x812F
GL_MIRRORED_REPEAT = 0x8370
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_CUBE = 0x8B60
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
GL_COMPILE_STATUS = 0x8B81
GL_INFO_LOG_LENGTH = 0x8B84
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_SHADER_COMPILER = 0x8DFA
GL_SHADER_BINARY_FORMATS = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
GL_LOW_FLOAT = 0x8DF0
GL_MEDIUM_FLOAT = 0x8DF1
GL_HIGH_FLOAT = 0x8DF2
GL_LOW_INT = 0x8DF3
GL_MEDIUM_INT = 0x8DF4
GL_HIGH_INT = 0x8DF5
GL_FRAMEBUFFER = 0x8D40
GL_RENDERBUFFER = 0x8D41
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGB565 = 0x8D62
GL_DEPTH_COMPONENT16 = 0x81A5
GL_STENCIL_INDEX = 0x1901
GL_STENCIL_INDEX8 = 0x8D48
GL_RENDERBUFFER_WIDTH = 0x8D42
GL_RENDERBUFFER_HEIGHT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
GL_RENDERBUFFER_RED_SIZE = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_DEPTH_ATTACHMENT = 0x8D00
GL_STENCIL_ATTACHMENT = 0x8D20
GL_NONE = 0
GL_FRAMEBUFFER_COMPLETE = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x8CD9
GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
GL_FRAMEBUFFER_BINDING = 0x8CA6
GL_RENDERBUFFER_BINDING = 0x8CA7
GL_MAX_RENDERBUFFER_SIZE = 0x84E8
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506


#GL_APICALL void GL_APIENTRY glActiveTexture (GLenum texture);
glActiveTexture = glesdll.glActiveTexture
glActiveTexture.argtypes = (GLenum,)
glActiveTexture.restype = None

#GL_APICALL void GL_APIENTRY glAttachShader (GLuint program, GLuint shader);
glAttachShader = glesdll.glAttachShader
glAttachShader.argtypes = (GLuint, GLuint)
glAttachShader.restype = None

#GL_APICALL void GL_APIENTRY glBindAttribLocation (GLuint program, GLuint index, const GLchar* name);
glBindAttribLocation = glesdll.glBindAttribLocation
glBindAttribLocation.argtypes = (GLuint, GLuint, ctypes.c_char_p)
glBindAttribLocation.restype = None

#GL_APICALL void GL_APIENTRY glBindBuffer (GLenum target, GLuint buffer);
glBindBuffer = glesdll.glBindBuffer
glBindBuffer.argtypes = (GLenum, GLuint)
glBindBuffer.restype = None

#GL_APICALL void GL_APIENTRY glBindFramebuffer (GLenum target, GLuint framebuffer);
glBindFramebuffer = glesdll.glBindFramebuffer
glBindFramebuffer.argtypes = (GLenum, GLuint)
glBindFramebuffer.restype = None

#GL_APICALL void GL_APIENTRY glBindRenderbuffer (GLenum target, GLuint renderbuffer);
glBindRenderbuffer = glesdll.glBindRenderbuffer
glBindRenderbuffer.argtypes = (GLenum, GLuint)
glBindRenderbuffer.restype = None

#GL_APICALL void GL_APIENTRY glBindTexture (GLenum target, GLuint texture);
glBindTexture = glesdll.glBindTexture
glBindTexture.argtypes = (GLenum, GLuint)
glBindTexture.restype = None

#GL_APICALL void GL_APIENTRY glBlendColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha);
glBlendColor = glesdll.glBlendColor
glBlendColor.argtypes = (GLclampf, GLclampf, GLclampf, GLclampf)
glBlendColor.restype = None

#GL_APICALL void GL_APIENTRY glBlendEquation ( GLenum mode );
glBlendEquation = glesdll.glBlendEquation
glBlendEquation.argtypes = (GLenum,)
glBlendEquation.restype = None

#GL_APICALL void GL_APIENTRY glBlendEquationSeparate (GLenum modeRGB, GLenum modeAlpha);
glBlendEquationSeparate = glesdll.glBlendEquationSeparate
glBlendEquationSeparate.argtypes = (GLenum, GLenum)
glBlendEquationSeparate.restype = None

#GL_APICALL void GL_APIENTRY glBlendFunc (GLenum sfactor, GLenum dfactor);
glBlendFunc = glesdll.glBlendFunc
glBlendFunc.argtypes = (GLenum, GLenum)
glBlendFunc.restype = None

#GL_APICALL void GL_APIENTRY glBlendFuncSeparate (GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha);
glBlendFuncSeparate = glesdll.glBlendFuncSeparate
glBlendFuncSeparate.argtypes = (GLenum, GLenum, GLenum, GLenum)
glBlendFuncSeparate.restype = None

#GL_APICALL void GL_APIENTRY glBufferData (GLenum target, GLsizeiptr size, const GLvoid* data, GLenum usage);
glBufferData = glesdll.glBufferData
glBufferData.argtypes = (GLenum, GLsizeiptr, ctypes.c_void_p, GLenum)
glBufferData.restype = None

#GL_APICALL void GL_APIENTRY glBufferSubData (GLenum target, GLintptr offset, GLsizeiptr size, const GLvoid* data);
glBufferSubData = glesdll.glBufferSubData
glBufferSubData.argtypes = (GLenum, GLintptr, GLsizeiptr, ctypes.c_void_p)
glBufferSubData.restype = None

#GL_APICALL GLenum GL_APIENTRY glCheckFramebufferStatus (GLenum target);
glCheckFramebufferStatus = glesdll.glCheckFramebufferStatus
glCheckFramebufferStatus.argtypes = (GLenum,)
glCheckFramebufferStatus.restype = None

#GL_APICALL void GL_APIENTRY glClear (GLbitfield mask);
glClear = glesdll.glClear
glClear.argtypes = (GLbitfield,)
glClear.restype = None

#GL_APICALL void GL_APIENTRY glClearColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha);
glClearColor = glesdll.glClearColor
glClearColor.argtypes = (GLclampf, GLclampf, GLclampf, GLclampf)
glClearColor.restype = None

#GL_APICALL void GL_APIENTRY glClearDepthf (GLclampf depth);
glClearDepthf = glesdll.glClearDepthf
glClearDepthf.argtypes = (GLclampf,)
glClearDepthf.restype = None

#GL_APICALL void GL_APIENTRY glClearStencil (GLint s);
glClearStencil = glesdll.glClearStencil
glClearStencil.argtypes = (GLint,)
glClearStencil.restype = None

#GL_APICALL void GL_APIENTRY glColorMask (GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha);
glColorMask = glesdll.glColorMask
glColorMask.argtypes = (GLboolean, GLboolean, GLboolean, GLboolean)
glColorMask.restype = None

#GL_APICALL void GL_APIENTRY glCompileShader (GLuint shader);
glCompileShader = glesdll.glCompileShader
glCompileShader.argtypes = (GLuint,)
glCompileShader.restype = None

#GL_APICALL void GL_APIENTRY glCompressedTexImage2D (
#    GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid* data);
glCompressedTexImage2D = glesdll.glCompressedTexImage2D
glCompressedTexImage2D.argtypes = (GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p)
glCompressedTexImage2D.restype = None

#GL_APICALL void GL_APIENTRY glCompressedTexSubImage2D (
#    GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid* data);
glCompressedTexSubImage2D = glesdll.glCompressedTexSubImage2D
glCompressedTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p)
glCompressedTexSubImage2D.restype = None

#GL_APICALL void GL_APIENTRY glCopyTexImage2D (
#    GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border);
glCopyTexImage2D = glesdll.glCopyTexImage2D
glCopyTexImage2D.argtypes = (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint)
glCopyTexImage2D.restype = None

#GL_APICALL void GL_APIENTRY glCopyTexSubImage2D (
#    GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);
glCopyTexSubImage2D = glesdll.glCopyTexSubImage2D
glCopyTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei)
glCopyTexSubImage2D.restype = None

#GL_APICALL GLuint GL_APIENTRY glCreateProgram (void);
glCreateProgram = glesdll.glCreateProgram
glCreateProgram.argtypes = None
glCreateProgram.restype = GLuint

#GL_APICALL GLuint GL_APIENTRY glCreateShader (GLenum type);
glCreateShader = glesdll.glCreateShader
glCreateShader.argtypes = (GLenum,)
glCreateShader.restype = GLuint

#GL_APICALL void GL_APIENTRY glCullFace (GLenum mode);
glCullFace = glesdll.glCullFace
glCullFace.argtypes = (GLenum,)
glCullFace.restype = None

#GL_APICALL void GL_APIENTRY glDeleteBuffers (GLsizei n, const GLuint* buffers);
glDeleteBuffers = glesdll.glDeleteBuffers
glDeleteBuffers.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glDeleteBuffers.restype = None

#GL_APICALL void GL_APIENTRY glDeleteFramebuffers (GLsizei n, const GLuint* framebuffers);
glDeleteFramebuffers = glesdll.glDeleteFramebuffers
glDeleteFramebuffers.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glDeleteFramebuffers.restype = None

#GL_APICALL void GL_APIENTRY glDeleteProgram (GLuint program);
glDeleteProgram = glesdll.glDeleteProgram
glDeleteProgram.argtypes = (GLuint,)
glDeleteProgram.restype = None

#GL_APICALL void GL_APIENTRY glDeleteRenderbuffers (GLsizei n, const GLuint* renderbuffers);
glDeleteRenderbuffers = glesdll.glDeleteRenderbuffers
glDeleteRenderbuffers.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glDeleteRenderbuffers.restype = None

#GL_APICALL void GL_APIENTRY glDeleteShader (GLuint shader);
glDeleteShader = glesdll.glDeleteShader
glDeleteShader.argtypes = (GLuint,)
glDeleteShader.restype = None

#GL_APICALL void GL_APIENTRY glDeleteTextures (GLsizei n, const GLuint* textures);
glDeleteTextures = glesdll.glDeleteTextures
glDeleteTextures.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glDeleteTextures.restype = None

#GL_APICALL void GL_APIENTRY glDepthFunc (GLenum func);
glDepthFunc = glesdll.glDepthFunc
glDepthFunc.argtypes = (GLenum,)
glDepthFunc.restype = None

#GL_APICALL void GL_APIENTRY glDepthMask (GLboolean flag);
glDepthMask = glesdll.glDepthMask
glDepthMask.argtypes = (GLboolean,)
glDepthMask.restype = None

#GL_APICALL void GL_APIENTRY glDepthRangef (GLclampf zNear, GLclampf zFar);
glDepthRangef = glesdll.glDepthRangef
glDepthRangef.argtypes = (GLclampf, GLclampf)
glDepthRangef.restype = None

#GL_APICALL void GL_APIENTRY glDetachShader (GLuint program, GLuint shader);
glDetachShader = glesdll.glDetachShader
glDetachShader.argtypes = (GLuint, GLuint)
glDetachShader.restype = None

#GL_APICALL void GL_APIENTRY glDisable (GLenum cap);
glDisable = glesdll.glDisable
glDisable.argtypes = (GLenum,)
glDisable.restype = None

#GL_APICALL void GL_APIENTRY glDisableVertexAttribArray (GLuint index);
glDisableVertexAttribArray = glesdll.glDisableVertexAttribArray
glDisableVertexAttribArray.argtypes = (GLuint,)
glDisableVertexAttribArray.restype = None

#GL_APICALL void GL_APIENTRY glDrawArrays (GLenum mode, GLint first, GLsizei count);
glDrawArrays = glesdll.glDrawArrays
glDrawArrays.argtypes = (GLenum, GLint, GLsizei)
glDrawArrays.restype = None

#GL_APICALL void GL_APIENTRY glDrawElements (GLenum mode, GLsizei count, GLenum type, const GLvoid* indices);
glDrawElements = glesdll.glDrawElements
glDrawElements.argtypes = (GLenum, GLsizei, GLenum, ctypes.c_void_p)
glDrawElements.restype = None

#GL_APICALL void GL_APIENTRY glEnable (GLenum cap);
glEnable = glesdll.glEnable
glEnable.argtypes = (GLenum,)
glEnable.restype = None

#GL_APICALL void GL_APIENTRY glEnableVertexAttribArray (GLuint index);
glEnableVertexAttribArray = glesdll.glEnableVertexAttribArray
glEnableVertexAttribArray.argtypes = (GLuint,)
glEnableVertexAttribArray.restype = None

#GL_APICALL void GL_APIENTRY glFinish (void);
glFinish = glesdll.glFinish
glFinish.argtypes = None
glFinish.restype = None

#GL_APICALL void GL_APIENTRY glFlush (void);
glFlush = glesdll.glFlush
glFlush.argtypes = None
glFlush.restype = None

#GL_APICALL void GL_APIENTRY glFramebufferRenderbuffer (GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer);
glFramebufferRenderbuffer = glesdll.glFramebufferRenderbuffer
glFramebufferRenderbuffer.argtypes = (GLenum, GLenum, GLenum, GLuint)
glFramebufferRenderbuffer.restype = None

#GL_APICALL void GL_APIENTRY glFramebufferTexture2D (GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);
glFramebufferTexture2D = glesdll.glFramebufferTexture2D
glFramebufferTexture2D.argtypes = (GLenum, GLenum, GLenum, GLuint, GLint)
glFramebufferTexture2D.restype = None

#GL_APICALL void GL_APIENTRY glFrontFace (GLenum mode);
glFrontFace = glesdll.glFrontFace
glFrontFace.argtypes = (GLenum,)
glFrontFace.restype = None

#GL_APICALL void GL_APIENTRY glGenBuffers (GLsizei n, GLuint* buffers);
glGenBuffers = glesdll.glGenBuffers
glGenBuffers.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glGenBuffers.restype = None

#GL_APICALL void GL_APIENTRY glGenerateMipmap (GLenum target);
glGenerateMipmap = glesdll.glGenerateMipmap
glGenerateMipmap.argtypes = (GLenum,)
glGenerateMipmap.restype = None

#GL_APICALL void GL_APIENTRY glGenFramebuffers (GLsizei n, GLuint* framebuffers);
glGenFramebuffers = glesdll.glGenFramebuffers
glGenFramebuffers.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glGenFramebuffers.restype = None

#GL_APICALL void GL_APIENTRY glGenRenderbuffers (GLsizei n, GLuint* renderbuffers);
glGenRenderbuffers = glesdll.glGenRenderbuffers
glGenRenderbuffers.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glGenRenderbuffers.restype = None

#GL_APICALL void GL_APIENTRY glGenTextures (GLsizei n, GLuint* textures);
glGenTextures = glesdll.glGenTextures
glGenTextures.argtypes = (GLsizei, ctypes.POINTER(GLuint))
glGenTextures.restype = None

#GL_APICALL void GL_APIENTRY glGetActiveAttrib (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name);
glGetActiveAttrib = glesdll.glGetActiveAttrib
glGetActiveAttrib.argtypes = (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ctypes.POINTER(GLenum), ctypes.c_void_p)
glGetActiveAttrib.restype = None

#GL_APICALL void GL_APIENTRY glGetActiveUniform (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name);
glGetActiveUniform = glesdll.glGetActiveUniform
glGetActiveUniform.argtypes = (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ctypes.POINTER(GLenum), ctypes.c_void_p)
glGetActiveUniform.restype = None

#GL_APICALL void GL_APIENTRY glGetAttachedShaders (GLuint program, GLsizei maxcount, GLsizei* count, GLuint* shaders);
glGetAttachedShaders = glesdll.glGetAttachedShaders
glGetAttachedShaders.argtypes = (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLuint))
glGetAttachedShaders.restype = None

#GL_APICALL int GL_APIENTRY glGetAttribLocation (GLuint program, const GLchar* name);
glGetAttribLocation = glesdll.glGetAttribLocation
glGetAttribLocation.argtypes = (GLuint, ctypes.c_char_p)
glGetAttribLocation.restype = ctypes.c_int32

#GL_APICALL void GL_APIENTRY glGetBooleanv (GLenum pname, GLboolean* params);
glGetBooleanv = glesdll.glGetBooleanv
glGetBooleanv.argtypes = (GLenum, ctypes.POINTER(GLboolean))
glGetBooleanv.restype = None

#GL_APICALL void GL_APIENTRY glGetBufferParameteriv (GLenum target, GLenum pname, GLint* params);
glGetBufferParameteriv = glesdll.glGetBufferParameteriv
glGetBufferParameteriv.argtypes = (GLenum, GLenum, ctypes.POINTER(GLint))
glGetBufferParameteriv.restype = None

#GL_APICALL GLenum GL_APIENTRY glGetError (void);
glGetError = glesdll.glGetError
glGetError.argtypes = None
glGetError.restype = GLenum

#GL_APICALL void GL_APIENTRY glGetFloatv (GLenum pname, GLfloat* params);
glGetFloatv = glesdll.glGetFloatv
glGetFloatv.argtypes = (GLenum, ctypes.POINTER(GLfloat))
glGetFloatv.restype = None

#GL_APICALL void GL_APIENTRY glGetFramebufferAttachmentParameteriv (GLenum target, GLenum attachment, GLenum pname, GLint* params);
glGetFramebufferAttachmentParameteriv = glesdll.glGetFramebufferAttachmentParameteriv
glGetFramebufferAttachmentParameteriv.argtypes = (GLenum, GLenum, GLenum, ctypes.POINTER(GLint))
glGetFramebufferAttachmentParameteriv.restype = None

#GL_APICALL void         GL_APIENTRY glGetIntegerv (GLenum pname, GLint* params);
glGetIntegerv = glesdll.glGetIntegerv
glGetIntegerv.argtypes = (GLenum, ctypes.POINTER(GLint))
glGetIntegerv.restype = None

#GL_APICALL void GL_APIENTRY glGetProgramiv (GLuint program, GLenum pname, GLint* params);
glGetProgramiv = glesdll.glGetProgramiv
glGetProgramiv.argtypes = (GLuint, GLenum, ctypes.POINTER(GLint))
glGetProgramiv.restype = None

#GL_APICALL void GL_APIENTRY glGetProgramInfoLog (GLuint program, GLsizei bufsize, GLsizei* length, GLchar* infolog);
glGetProgramInfoLog = glesdll.glGetProgramInfoLog
glGetProgramInfoLog.argtypes = (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.c_void_p)
glGetProgramInfoLog.restype = None

#GL_APICALL void GL_APIENTRY glGetRenderbufferParameteriv (GLenum target, GLenum pname, GLint* params);
glGetRenderbufferParameteriv = glesdll.glGetRenderbufferParameteriv
glGetRenderbufferParameteriv.argtypes = (GLuint, GLenum, ctypes.POINTER(GLint))
glGetRenderbufferParameteriv.restype = None

#GL_APICALL void GL_APIENTRY glGetShaderiv (GLuint shader, GLenum pname, GLint* params);
glGetShaderiv = glesdll.glGetShaderiv
glGetShaderiv.argtypes = (GLuint, GLenum, ctypes.POINTER(GLint))
glGetShaderiv.restype = None

#GL_APICALL void GL_APIENTRY glGetShaderInfoLog (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* infolog);
glGetShaderInfoLog = glesdll.glGetShaderInfoLog
glGetShaderInfoLog.argtypes = (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.c_void_p)
glGetShaderInfoLog.restype = None

#GL_APICALL void GL_APIENTRY glGetShaderPrecisionFormat (GLenum shadertype, GLenum precisiontype, GLint* range, GLint* precision);
glGetShaderPrecisionFormat = glesdll.glGetShaderPrecisionFormat
glGetShaderPrecisionFormat.argtypes = (GLenum, GLenum, ctypes.POINTER(GLint), ctypes.POINTER(GLint))
glGetShaderPrecisionFormat.restype = None

#GL_APICALL void GL_APIENTRY glGetShaderSource (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* source);
lGetShaderSource = glesdll.glGetShaderSource
lGetShaderSource.argtypes = (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.c_void_p)
lGetShaderSource.restype = None

#GL_APICALL const GLubyte* GL_APIENTRY glGetString (GLenum name);
glGetString = glesdll.glGetString
glGetString.argtypes = (GLenum,)
glGetString.restype = ctypes.c_char_p

#GL_APICALL void GL_APIENTRY glGetTexParameterfv (GLenum target, GLenum pname, GLfloat* params);
glGetTexParameterfv = glesdll.glGetTexParameterfv
glGetTexParameterfv.argtypes = (GLenum, GLenum, ctypes.POINTER(GLfloat))
glGetTexParameterfv.restype = None

#GL_APICALL void         GL_APIENTRY glGetTexParameteriv (GLenum target, GLenum pname, GLint* params);
glGetTexParameteriv = glesdll.glGetTexParameteriv
glGetTexParameteriv.argtypes = (GLenum, GLenum, ctypes.POINTER(GLint))
glGetTexParameteriv.restype = None

#GL_APICALL void GL_APIENTRY glGetUniformfv (GLuint program, GLint location, GLfloat* params);
glGetUniformfv = glesdll.glGetUniformfv
glGetUniformfv.argtypes = (GLuint, GLint, ctypes.POINTER(GLfloat))
glGetUniformfv.restype = None

#GL_APICALL void GL_APIENTRY glGetUniformiv (GLuint program, GLint location, GLint* params);
glGetUniformiv = glesdll.glGetUniformiv
glGetUniformiv.argtypes = (GLuint, GLint, ctypes.POINTER(GLint))
glGetUniformiv.restype = None

#GL_APICALL int GL_APIENTRY glGetUniformLocation (GLuint program, const GLchar* name);
glGetUniformLocation = glesdll.glGetUniformLocation
glGetUniformLocation.argtypes = (GLuint, ctypes.c_char_p)
glGetUniformLocation.restype = GLint

#GL_APICALL void GL_APIENTRY glGetVertexAttribfv (GLuint index, GLenum pname, GLfloat* params);
glGetVertexAttribfv = glesdll.glGetVertexAttribfv
glGetVertexAttribfv.argtypes = (GLuint, GLenum, ctypes.POINTER(GLfloat))
glGetVertexAttribfv.restype = None

#GL_APICALL void GL_APIENTRY glGetVertexAttribiv (GLuint index, GLenum pname, GLint* params);
glGetVertexAttribiv = glesdll.glGetVertexAttribiv
glGetVertexAttribiv.argtypes = (GLuint, GLenum, ctypes.POINTER(GLint))
glGetVertexAttribiv.restype = None

#GL_APICALL void GL_APIENTRY glGetVertexAttribPointerv (GLuint index, GLenum pname, GLvoid** pointer);
glGetVertexAttribPointerv = glesdll.glGetVertexAttribPointerv
glGetVertexAttribPointerv.argtypes = (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p))
glGetVertexAttribPointerv.restype = None

#GL_APICALL void GL_APIENTRY glHint (GLenum target, GLenum mode);
glHint = glesdll.glHint
glHint.argtypes = (GLuint, GLenum)
glHint.restype = None

#GL_APICALL GLboolean GL_APIENTRY glIsBuffer (GLuint buffer);
glIsBuffer = glesdll.glIsBuffer
glIsBuffer.argtypes = (GLuint,)
glIsBuffer.restype = GLboolean

#GL_APICALL GLboolean GL_APIENTRY glIsEnabled (GLenum cap);
glIsEnabled = glesdll.glIsEnabled
glIsEnabled.argtypes = (GLenum,)
glIsEnabled.restype = GLboolean

#GL_APICALL GLboolean GL_APIENTRY glIsFramebuffer (GLuint framebuffer);
glIsFramebuffer = glesdll.glIsFramebuffer
glIsFramebuffer.argtypes = (GLuint,)
glIsFramebuffer.restype = GLboolean

#GL_APICALL GLboolean GL_APIENTRY glIsProgram (GLuint program);
glIsProgram = glesdll.glIsProgram
glIsProgram.argtypes = (GLuint,)
glIsProgram.restype = GLboolean

#GL_APICALL GLboolean GL_APIENTRY glIsRenderbuffer (GLuint renderbuffer);
glIsRenderbuffer = glesdll.glIsRenderbuffer
glIsRenderbuffer.argtypes = (GLuint,)
glIsRenderbuffer.restype = GLboolean

#GL_APICALL GLboolean    GL_APIENTRY glIsShader (GLuint shader);
glIsShader = glesdll.glIsShader
glIsShader.argtypes = (GLuint,)
glIsShader.restype = GLboolean

#GL_APICALL GLboolean GL_APIENTRY glIsTexture (GLuint texture);
glIsTexture = glesdll.glIsTexture
glIsTexture.argtypes = (GLuint,)
glIsTexture.restype = GLboolean

#GL_APICALL void GL_APIENTRY glLineWidth (GLfloat width);
glLineWidth = glesdll.glLineWidth
glLineWidth.argtypes = (GLfloat,)
glLineWidth.restype = None

#GL_APICALL void GL_APIENTRY glLinkProgram (GLuint program);
glLinkProgram = glesdll.glLinkProgram
glLinkProgram.argtypes = (GLuint,)
glLinkProgram.restype = None

#GL_APICALL void GL_APIENTRY glPixelStorei (GLenum pname, GLint param);
glPixelStorei = glesdll.glPixelStorei
glPixelStorei.argtypes = (GLenum, GLint)
glPixelStorei.restype = None

#GL_APICALL void GL_APIENTRY glPolygonOffset (GLfloat factor, GLfloat units);
glPolygonOffset = glesdll.glPolygonOffset
glPolygonOffset.argtypes = (GLfloat, GLfloat)
glPolygonOffset.restype = None

#GL_APICALL void GL_APIENTRY glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels);
glReadPixels = glesdll.glReadPixels
glReadPixels.argtypes = (GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p)
glReadPixels.restype = None

#GL_APICALL void GL_APIENTRY glReleaseShaderCompiler (void);
glReleaseShaderCompiler = glesdll.glReleaseShaderCompiler
glReleaseShaderCompiler.argtypes = None
glReleaseShaderCompiler.restype = None

#GL_APICALL void GL_APIENTRY glRenderbufferStorage (GLenum target, GLenum internalformat, GLsizei width, GLsizei height);
glRenderbufferStorage = glesdll.glRenderbufferStorage
glRenderbufferStorage.argtypes = (GLenum, GLenum, GLsizei, GLsizei)
glRenderbufferStorage.restype = None

#GL_APICALL void GL_APIENTRY glSampleCoverage (GLclampf value, GLboolean invert);
glSampleCoverage = glesdll.glSampleCoverage
glSampleCoverage.argtypes = (GLclampf, GLboolean)
glSampleCoverage.restype = None

#GL_APICALL void GL_APIENTRY glScissor (GLint x, GLint y, GLsizei width, GLsizei height);
glScissor = glesdll.glScissor
glScissor.argtypes = (GLint, GLint, GLsizei, GLsizei)
glScissor.restype = None

#GL_APICALL void GL_APIENTRY glShaderBinary (GLsizei n, const GLuint* shaders, GLenum binaryformat, const GLvoid* binary, GLsizei length);
glShaderBinary = glesdll.glShaderBinary
glShaderBinary.argtypes = (GLsizei, ctypes.POINTER(GLuint), GLenum, ctypes.c_void_p, GLsizei)
glShaderBinary.restype = None

#GL_APICALL void GL_APIENTRY glShaderSource (GLuint shader, GLsizei count, const GLchar** string, const GLint* length);
glShaderSource = glesdll.glShaderSource
glShaderSource.argtypes = (GLuint, GLsizei, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(GLint))
glShaderSource.restype = None

#GL_APICALL void GL_APIENTRY glStencilFunc (GLenum func, GLint ref, GLuint mask);
glStencilFunc = glesdll.glStencilFunc
glStencilFunc.argtypes = (GLenum, GLint, GLuint)
glStencilFunc.restype = None

#GL_APICALL void GL_APIENTRY glStencilFuncSeparate (GLenum face, GLenum func, GLint ref, GLuint mask);
glStencilFuncSeparate = glesdll.glStencilFuncSeparate
glStencilFuncSeparate.argtypes = (GLenum, GLenum, GLint, GLuint)
glStencilFuncSeparate.restype = None

#GL_APICALL void GL_APIENTRY glStencilMask (GLuint mask);
glStencilMask = glesdll.glStencilMask
glStencilMask.argtypes = (GLuint,)
glStencilMask.restype = None

#GL_APICALL void GL_APIENTRY glStencilMaskSeparate (GLenum face, GLuint mask);
glStencilMaskSeparate = glesdll.glStencilMaskSeparate
glStencilMaskSeparate.argtypes = (GLenum, GLuint)
glStencilMaskSeparate.restype = None

#GL_APICALL void GL_APIENTRY glStencilOp (GLenum fail, GLenum zfail, GLenum zpass);
glStencilOp = glesdll.glStencilOp
glStencilOp.argtypes = (GLenum, GLenum, GLenum)
glStencilOp.restype = None

#GL_APICALL void GL_APIENTRY glStencilOpSeparate (GLenum face, GLenum fail, GLenum zfail, GLenum zpass);
glStencilOpSeparate = glesdll.glStencilOpSeparate
glStencilOpSeparate.argtypes = (GLenum, GLenum, GLenum, GLenum)
glStencilOpSeparate.restype = None

#GL_APICALL void GL_APIENTRY glTexImage2D (
#    GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid* pixels);
glTexImage2D = glesdll.glTexImage2D
glTexImage2D.argtypes = (GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p)
glTexImage2D.restype = None

#GL_APICALL void GL_APIENTRY glTexParameterf (GLenum target, GLenum pname, GLfloat param);
glTexParameterf = glesdll.glTexParameterf
glTexParameterf.argtypes = (GLenum, GLenum, GLfloat)
glTexParameterf.restype = None

#GL_APICALL void GL_APIENTRY glTexParameterfv (GLenum target, GLenum pname, const GLfloat* params);
glTexParameterfv = glesdll.glTexParameterfv
glTexParameterfv.argtypes = (GLenum, GLenum, ctypes.POINTER(GLfloat))
glTexParameterfv.restype = None

#GL_APICALL void GL_APIENTRY glTexParameteri (GLenum target, GLenum pname, GLint param);
glTexParameteri = glesdll.glTexParameteri
glTexParameteri.argtypes = (GLenum, GLenum, GLint)
glTexParameteri.restype = None

#GL_APICALL void GL_APIENTRY glTexParameteriv (GLenum target, GLenum pname, const GLint* params);
glTexParameteriv = glesdll.glTexParameteriv
glTexParameteriv.argtypes = (GLenum, GLenum, ctypes.POINTER(GLint))
glTexParameteriv.restype = None

#GL_APICALL void GL_APIENTRY glTexSubImage2D (
#    GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* pixels);
glTexSubImage2D = glesdll.glTexSubImage2D
glTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p)
glTexSubImage2D.restype = None

#GL_APICALL void GL_APIENTRY glUniform1f (GLint location, GLfloat x);
glUniform1f = glesdll.glUniform1f
glUniform1f.argtypes = (GLint, GLfloat)
glUniform1f.restype = None

#GL_APICALL void GL_APIENTRY glUniform1fv (GLint location, GLsizei count, const GLfloat* v);
glUniform1fv = glesdll.glUniform1fv
glUniform1fv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLfloat))
glUniform1fv.restype = None

#GL_APICALL void GL_APIENTRY glUniform1i (GLint location, GLint x);
glUniform1i = glesdll.glUniform1i
glUniform1i.argtypes = (GLint, GLint)
glUniform1i.restype = None

#GL_APICALL void GL_APIENTRY glUniform1iv (GLint location, GLsizei count, const GLint* v);
glUniform1iv = glesdll.glUniform1iv
glUniform1iv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLint))
glUniform1iv.restype = None

#GL_APICALL void GL_APIENTRY glUniform2f (GLint location, GLfloat x, GLfloat y);
glUniform2f = glesdll.glUniform2f
glUniform2f.argtypes = (GLint, GLfloat, GLfloat)
glUniform2f.restype = None

#GL_APICALL void GL_APIENTRY glUniform2fv (GLint location, GLsizei count, const GLfloat* v);
glUniform2fv = glesdll.glUniform2fv
glUniform2fv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLfloat))
glUniform2fv.restype = None

#GL_APICALL void GL_APIENTRY glUniform2i (GLint location, GLint x, GLint y);
glUniform2i = glesdll.glUniform2i
glUniform2i.argtypes = (GLint, GLint, GLint)
glUniform2i.restype = None

#GL_APICALL void GL_APIENTRY glUniform2iv (GLint location, GLsizei count, const GLint* v);
glUniform2iv = glesdll.glUniform2iv
glUniform2iv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLint))
glUniform2iv.restype = None

#GL_APICALL void GL_APIENTRY glUniform3f (GLint location, GLfloat x, GLfloat y, GLfloat z);
glUniform3f = glesdll.glUniform3f
glUniform3f.argtypes = (GLint, GLfloat, GLfloat, GLfloat)
glUniform3f.restype = None

#GL_APICALL void GL_APIENTRY glUniform3fv (GLint location, GLsizei count, const GLfloat* v);
glUniform3fv = glesdll.glUniform3fv
glUniform3fv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLfloat))
glUniform3fv.restype = None

#GL_APICALL void GL_APIENTRY glUniform3i (GLint location, GLint x, GLint y, GLint z);
glUniform3i = glesdll.glUniform3i
glUniform3i.argtypes = (GLint, GLint, GLint, GLint)
glUniform3i.restype = None

#GL_APICALL void GL_APIENTRY glUniform3iv (GLint location, GLsizei count, const GLint* v);
glUniform3iv = glesdll.glUniform3iv
glUniform3iv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLint))
glUniform3iv.restype = None

#GL_APICALL void GL_APIENTRY glUniform4f (GLint location, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
glUniform4f = glesdll.glUniform4f
glUniform4f.argtypes = (GLint, GLfloat, GLfloat, GLfloat, GLfloat)
glUniform4f.restype = None

#GL_APICALL void GL_APIENTRY glUniform4fv (GLint location, GLsizei count, const GLfloat* v);
glUniform4fv = glesdll.glUniform4fv
glUniform4fv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLfloat))
glUniform4fv.restype = None

#GL_APICALL void GL_APIENTRY glUniform4i (GLint location, GLint x, GLint y, GLint z, GLint w);
glUniform4i = glesdll.glUniform4i
glUniform4i.argtypes = (GLint, GLint, GLint, GLint)
glUniform4i.restype = None

#GL_APICALL void GL_APIENTRY glUniform4iv (GLint location, GLsizei count, const GLint* v);
glUniform4iv = glesdll.glUniform4iv
glUniform4iv.argtypes = (GLint, GLsizei, ctypes.POINTER(GLint))
glUniform4iv.restype = None

#GL_APICALL void GL_APIENTRY glUniformMatrix2fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);
glUniformMatrix2fv = glesdll.glUniformMatrix2fv
glUniformMatrix2fv.argtypes = (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat))
glUniformMatrix2fv.restype = None

#GL_APICALL void GL_APIENTRY glUniformMatrix3fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);
glUniformMatrix3fv = glesdll.glUniformMatrix3fv
glUniformMatrix3fv.argtypes = (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat))
glUniformMatrix3fv.restype = None

#GL_APICALL void GL_APIENTRY glUniformMatrix4fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);
glUniformMatrix4fv = glesdll.glUniformMatrix4fv
glUniformMatrix4fv.argtypes = (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat))
glUniformMatrix4fv.restype = None

#GL_APICALL void GL_APIENTRY glUseProgram (GLuint program);
glUseProgram = glesdll.glUseProgram
glUseProgram.argtypes = (GLuint,)
glUseProgram.restype = None

#GL_APICALL void GL_APIENTRY glValidateProgram (GLuint program);
glValidateProgram = glesdll.glValidateProgram
glValidateProgram.argtypes = (GLuint,)
glValidateProgram.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib1f (GLuint indx, GLfloat x);
glVertexAttrib1f = glesdll.glVertexAttrib1f
glVertexAttrib1f.argtypes = (GLuint, GLfloat)
glVertexAttrib1f.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib1fv (GLuint indx, const GLfloat* values);
glVertexAttrib1fv = glesdll.glVertexAttrib1fv
glVertexAttrib1fv.argtypes = (GLuint, ctypes.POINTER(GLfloat))
glVertexAttrib1fv.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib2f (GLuint indx, GLfloat x, GLfloat y);
glVertexAttrib2f = glesdll.glVertexAttrib2f
glVertexAttrib2f.argtypes = (GLuint, GLfloat, GLfloat)
glVertexAttrib2f.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib2fv (GLuint indx, const GLfloat* values);
glVertexAttrib2fv = glesdll.glVertexAttrib2fv
glVertexAttrib2fv.argtypes = (GLuint, ctypes.POINTER(GLfloat))
glVertexAttrib2fv.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib3f (GLuint indx, GLfloat x, GLfloat y, GLfloat z);
glVertexAttrib3f = glesdll.glVertexAttrib3f
glVertexAttrib3f.argtypes = (GLuint, GLfloat, GLfloat, GLfloat)
glVertexAttrib3f.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib3fv (GLuint indx, const GLfloat* values);
glVertexAttrib3fv = glesdll.glVertexAttrib3fv
glVertexAttrib3fv.argtypes = (GLuint, ctypes.POINTER(GLfloat))
glVertexAttrib3fv.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib4f (GLuint indx, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
glVertexAttrib4f = glesdll.glVertexAttrib4f
glVertexAttrib4f.argtypes = (GLuint, GLfloat, GLfloat, GLfloat, GLfloat)
glVertexAttrib4f.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttrib4fv (GLuint indx, const GLfloat* values);
glVertexAttrib4fv = glesdll.glVertexAttrib4fv
glVertexAttrib4fv.argtypes = (GLuint, ctypes.POINTER(GLfloat))
glVertexAttrib4fv.restype = None

#GL_APICALL void GL_APIENTRY glVertexAttribPointer (GLuint indx, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid* ptr);
glVertexAttribPointer = glesdll.glVertexAttribPointer
glVertexAttribPointer.argtypes = (GLuint, GLint, GLenum, GLboolean, GLsizei, ctypes.c_void_p)
glVertexAttribPointer.restype = None

#GL_APICALL void GL_APIENTRY glViewport (GLint x, GLint y, GLsizei width, GLsizei height);
glViewport = glesdll.glViewport
glViewport.argtypes = (GLint, GLint, GLsizei, GLsizei)
glViewport.restype = None
