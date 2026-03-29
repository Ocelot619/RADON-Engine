from core.base import Base # base game loop init 
from core.openGLUtils import OpenGLUtils # decorators compiling shaders and creating ready compilated program
from core.attribute import Attribute # we give instructions on how shader should read data 
from core.uniform import Uniform # here we have uniforms
from OpenGL.GL import * 

# Render Multiple Traingles

class Test(Base):

    def initialize(self):
        print("Initializing Program")

    def update(self):
        










# running program

Test().run()
