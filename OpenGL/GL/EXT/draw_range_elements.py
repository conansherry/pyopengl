'''OpenGL extension EXT.draw_range_elements

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.draw_range_elements to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.draw_range_elements import *
### END AUTOGENERATED SECTION

glDrawRangeElementsEXT = wrapper.wrapper( glDrawRangeElementsEXT ).setPyConverter(
	'indices', arrays.AsArrayOfType( 'indices', 'type' ),
).setCResolver( 
	'indices', arrays.ArrayDatatype.voidDataPointer ,
).setReturnValues( 
	wrapper.returnPyArgument( 'indices' ) 
)