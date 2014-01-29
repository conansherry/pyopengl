'''OpenGL extension OES.compressed_ETC1_RGB8_texture

This module customises the behaviour of the 
OpenGL.raw.GL.OES.compressed_ETC1_RGB8_texture to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/compressed_ETC1_RGB8_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.OES.compressed_ETC1_RGB8_texture import *

def glInitCompressedEtc1Rgb8TextureOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION