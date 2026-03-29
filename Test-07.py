from core.base import Base # base game loop init 
from core.openGLUtils import OpenGLUtils # decorators compiling shaders and creating ready compilated program
from core.attribute import Attribute # we give instructions on how shader should read data 
from core.uniform import Uniform # here we have uniforms
from OpenGL.GL import * 

# Render Multiple Traingles

class Test(Base):

    def initialize(self):
        print("Initializing Program")

        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
             vec3 newPos = position + translation;
             gl_Position = vec4(newPos, 1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        void main()
        {
            gl_FragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef) 

        # set up attributes

        positionData = [[0.0,   0.2, 0.0], # 1
                        [0.2,  -0.2, 0.0], # 2
                        [-0.2, -0.2, 0.0]] # 3
        
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        self.vertexCount = len(positionData)

        # setting up position uniforms 

        self.translation1 = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation1.locateVariable(self.programRef, "translation")


        self.translation2 = Uniform("vec3", [0.5, 0.0, 0.0 ])
        self.translation2.locateVariable(self.programRef, "translation")

        # setting up color uniforms 
        self.baseColor1 = Uniform("vec3", [0.5, 0.6, 0.0])
        self.baseColor1.locateVariable(self.programRef, "baseColor")

        self.baseColor2 = Uniform("vec3", [0.0, 0.0, 1.0])
        self.baseColor2.locateVariable(self.programRef, "baseColor")



    def update(self):
        glUseProgram(self.programRef)
        # clearing screen before rendering next 
        glClear(GL_COLOR_BUFFER_BIT)
        # draw first triangle
        self.translation1.uploadData()
        self.baseColor1.uploadData()
        glDrawArrays(GL_TRIANGLES, 0 , self.vertexCount)

        # second triangle 
        self.translation2.uploadData()
        self.baseColor2.uploadData()
        glDrawArrays(GL_TRIANGLES,0 , self.vertexCount)

# running program

Test().run()
