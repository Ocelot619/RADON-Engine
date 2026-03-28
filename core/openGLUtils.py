from OpenGL import GL

# static methods to load/compile opengl shaders
#    and link to create gpu programs

class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType)
        # OpenGL Version Specification and requirements
        extension = "#extension GL_ARB_shading_language_420pack: require \n"
        shaderCode = "#version 130 \n + extension + shaderCode"

        # create empty shader object and return reference value
        shaderRef = GL.glCreateShader(shaderType)
        # store source code in shader
        GL.glShaderSource(shaderRef, shaderCode) 
        # compile source code stored in shader
        GL.glCompileShader(shaderRef)

        # query whether compilation was succesful
        compileSuccess = Gl.glGetShaderiv(shaderRef, GL.GL_COMPILE_STATUS)

        if not compileSuccess:
            # retreive error mesage
            errorMessage = GL.glGetShaderInfoLog(shaderRef, GL.GL_COMPILE_STATUS)
            # free memory 
            GL.glDeleteShader(shaderRef)
            # convert byte stream to str message
            errorMessage = "\n" + errorMessage.decode("utf-8")
            #raise exception
            raise Exception(errorMessage)

        return shaderRef



    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        # compile shaders and store references 
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL.GL_VERTEX_SHADER)
        
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL.GL_FRAGMENT_SHADER)

        # create program object and store reference
        programRef = GL.glCreateProgram()
        GL.glAttachShader(programRef, vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)
        # link vertex shader to fragment shader
        GL.glLinkProgram(programRef)
        # query if linking was succesful 
        linkinSucces = GL.glGetProgramiv(programRef, GL.GL_LINK_STATUS)

        if not linkinSucces: 
            # retreive error message 
            errorMessage = GL.glGetProgramInfoLog(programRef)
            #convert byte to utf 
            errorMessage = "\n" + errorMessag.decode("utf-8")
            raiseException(errorMessage)
            #free memory 
            GL.glDeleteProgram(programRef)

        # linking was succesful
        return programRef