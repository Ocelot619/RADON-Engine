from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# render traiangle and square 

class Test(Base):

    def initialize(self):
        print("Initializing program...")
        
        vsCode = """
        in vec3 position;
        void main()
        {
        gl_Position = vec4(position.x, position.y, position.    z, 1.0);
        }
        """

        fsCode = """ 
        void main()
        {
            gl_FragColor = vec4(0.0, 1.0, 1.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glPointSize(16)
        glLineWidth(5)

        # set of triangle
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)
        positionDataTri = [[-0.5, 0.8, 0.0],
                           [-0.2, 0.2, 0.0],
                           [-0.8, 0.2, 0.0]]

        positionAttributeTri = Attribute("vec3", positionDataTri)
        positionAttributeTri.associateVariable(self.programRef, "position")
        self.vertexCountTri = len(positionDataTri)

# set of triangle
        self.vaoSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSquare)
        positionDataSquare = [[0.8,0.8,0.0],
                           [0.8,0.2,0.0],
                           [0.2,0.2,0.0],
                           [0.2, 0.8, 0.1]]

        positionAttributeSquare = Attribute("vec3", positionDataSquare)
        positionAttributeSquare.associateVariable(self.programRef, "position")
        self.vertexCountSquare = len(positionDataSquare)

    def update(self):

        glUseProgram(self.programRef)

        glBindVertexArray(self.vaoTri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri)

        glBindVertexArray(self.vaoSquare)
        glDrawArrays(GL_LINE_LOOP, 0 , self.vertexCountSquare)




# create instance and run 

Test().run()