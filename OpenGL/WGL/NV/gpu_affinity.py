'''OpenGL extension NV.gpu_affinity

This module customises the behaviour of the 
OpenGL.raw.WGL.NV.gpu_affinity to provide a more 
Python-friendly API

Overview (from the spec)
	
	On systems with more than one GPU it is desirable to be able to
	select which GPU(s) in the system become the target for OpenGL
	rendering commands. This extension introduces the concept of a GPU
	affinity mask. OpenGL rendering commands are directed to the
	GPU(s) specified by the affinity mask. GPU affinity is immutable.
	Once set, it cannot be changed.
	
	This extension also introduces the concept called affinity-DC. An
	affinity-DC is a device context with a GPU affinity mask embedded
	in it. This restricts the device context to only allow OpenGL
	commands to be sent to the GPU(s) in the affinity mask.
	
	Handles for the GPUs present in a system are enumerated with the
	command wglEnumGpusNV. An affinity-DC is created by calling
	wglCreateAffinityDCNV. This function takes a list of GPU handles,
	which make up the affinity mask. An affinity-DC can also
	indirectly be created by obtaining a DC from a pBuffer handle, by
	calling wglGetPbufferDC, which in turn was created from an
	affinity-DC by calling wglCreatePbuffer.
	
	A context created from an affinity DC will inherit the GPU
	affinity mask from the DC. Once inherited, it cannot be changed.
	Such a context is called an affinity-context. This restricts the
	affinity-context to only allow OpenGL commands to be sent to those
	GPU(s) in its affinity mask. Once created, this context can be
	used in two ways:
	
	  1. Make the affinity-context current to an affinity-DC. This
	     will only succeed if the context's affinity mask is the same
	     as the affinity mask in the DC. There is no window
	     associated with an affinity DC, therefore this is a way to
	     achieve off-screen rendering to an OpenGL context. This can
	     either be rendering to a pBuffer, or an application created
	     framebuffer object. In the former case, the affinity-mask of
	     the pBuffer DC, which is obtained from a pBuffer handle,
	     will be the same affinity-mask as the DC used to created the
	     pBuffer handle.  In the latter case, the default framebuffer
	     object will be incomplete because there is no window-system
	     created framebuffer. Therefore, the application will have to
	     create and bind a framebuffer object as the target for
	     rendering.
	  2. Make the affinity-context current to a DC obtained from a
	     window. Rendering only happens to the sub rectangles(s) of
	     the window that overlap the parts of the desktop that are
	     displayed by the GPU(s) in the affinity mask of the context.
	
	Sharing OpenGL objects between affinity-contexts, by calling
	wglShareLists, will only succeed if the contexts have identical
	affinity masks.
	
	It is not possible to make a regular context (one without an
	affinity mask) current to an affinity-DC. This would mean a way
	for a context to inherit affinity information, which makes the
	context affinity mutable, which is counter to the premise of this
	extension.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/gpu_affinity.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.WGL import _types, _glgets
from OpenGL.raw.WGL.NV.gpu_affinity import *
from OpenGL.raw.WGL.NV.gpu_affinity import _EXTENSION_NAME

def glInitGpuAffinityNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION