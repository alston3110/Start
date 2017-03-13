# -*- coding: utf-8 -*-

from distutils.core import setup
setup(name="PyGLESv2",
      version="0.1.0",
      description="PyGLESv2 is the Python bindings to OpenGL ES 2.0 and EGL.",
      author="Takahiro Okayama",
      author_email="okazoh.tk@gmail.com",
      license="New BSD license",
      packages=["PyGLESv2", "PyGLESv2.win32"],
      requires=["ctypes"])
