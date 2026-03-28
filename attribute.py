import numpy
from OpenGL.GL import *

class Attribute(self):

    def __init__(self, dataType, data):

        # type of elements in the data array 
        # int | float | vec2 |vec3 | vec4 | 
        self.dataType = dataType

        # array of data to be stored in a buffer
        self.data = data

        # reference to avalible buffer in GPU 
        self.bufferRef = glGenBuffers(1)

        # upload data
        self.uploadData()       
    # upload data to GPU buffer
    def uploadData(self):

        # convert data to numpy array format; convert to float
        data = numpy.array(self.data).astype(numpy.float32)

        # select buffer used by following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

def associateVariable(self, programRef, variableName):

    # get reference for program variable with given name
    variableRef = glGetAttribLocation(programRef, variableName)

    # if program not referencing variable exit

    if variableRef == -1:
        return 

    # select buffer used by following functions
    glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
    
    # specify how data will be read
    #    from the buffer currently bound to GL_ARRAY_BUFFER

    if self.dataType == "int":
        glVertexAttribPoint(variableRef, 1, GL_INT, False, 0, None)
    elif self.dataType == "float":
        glVertexAttribPoint(variableRef, 1, GL_FLOAT, False, 0 None)