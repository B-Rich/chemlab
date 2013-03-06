from OpenGL.GL import *
from OpenGL.raw import GL
from OpenGL.arrays import ArrayDatatype as ADT

class VertexBuffer(object):

  def __init__(self, data, usage):
    self.buffer = GL.GLuint(0)
    self.buffer = glGenBuffers(1)
    self.usage = usage
    self.data = data
    
    glBindBuffer(GL_ARRAY_BUFFER_ARB, self.buffer)
    glBufferData(GL_ARRAY_BUFFER_ARB, ADT.arrayByteCount(data), ADT.voidDataPointer(data), usage)
    

  def __del__(self):
    glDeleteBuffers(1, GL.GLuint(self.buffer))

  def bind(self):
    glBindBuffer(GL_ARRAY_BUFFER_ARB, self.buffer)

  def set_data(self, data):
    self.bind()
    glBufferData(GL_ARRAY_BUFFER_ARB, ADT.arrayByteCount(data), ADT.voidDataPointer(data), self.usage)
      
  def bind_colors(self, size, type, stride=0):
    self.bind()
    glColorPointer(size, type, stride, None)

  def bind_edgeflags(self, stride=0):
    self.bind()
    glEdgeFlagPointer(stride, None)

  def bind_indexes(self, type, stride=0):
    self.bind()
    glIndexPointer(type, stride, None)

  def bind_normals(self, type, stride=0):
    self.bind()
    glNormalPointer(type, stride, None)

  def bind_texcoords(self, size, type, stride=0):
    self.bind()
    glTexCoordPointer(size, type, stride, None)

  def bind_vertexes(self, size, type, stride=0):
    self.bind()
    glVertexPointer(size, type, stride, None)
    
  def bind_attrib(self, attribute, size, type, normalized=GL_FALSE, stride=0):
    self.bind()
    glVertexAttribPointer(attribute, size, type, normalized, stride, None)