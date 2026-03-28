from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL import GL


# render a single point 

class Test(Base):

    def initialize(self):
        print("Initializing program... ")

        ## create GPU program ## 

        # vertex shader code 
        vsCode = """
        void main()
        {
            gl_Position = vec4(0.5, 0.7, 0.0, 1.0);
        }
        """
        # fragment shader code
        fsCode = """
        void main()
        {
            gl_FragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        # send coode to GPU, compile , store program reference
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings  (optional)
        GL.glPointSize( 32 ) # in pixels 16

    def update(self):

         # select program to use when rendering
        GL.glUseProgram(self.programRef)

        # rendering geometrical objects
        GL.glDrawArrays(GL.GL_POINTS, 0, 1 ) # Draw mode constant, index of 1st , how many points to render 


#create instance and run it

Test().run()