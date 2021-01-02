from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import numpy as np
from shader import ShaderProgram
import glm
import time
from camera3D import Camera3D
from collada_loader.model_loader import ColladaModel
import vlc

SCR_WIDTH = 720
SCR_HEIGHT = 500

camera = Camera3D(glm.vec3(0.0, 5.0, 30.0))

robot_program = None
human_model = None
speed = 1.0

def initp():
    global robot_program
    # Load shaders
    robot_program = ShaderProgram("resources/shaders/shader_robot.vs", "resources/shaders/shader_robot.fg")
    robot_program.init()

    global human_model
    # Load dae file
    human_model = ColladaModel("resources/human.dae")
    # Enable depth test
    glEnable(GL_DEPTH_TEST)

def drawFunc():
    # Gets called in a loop
    glClearColor(1.0, 1.0, 1.0, 0.0)
    # Set clear color to white
    glClearDepth(1.0)

    glPointSize(5)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # FOV, AspectRatio, near, far
    projection = glm.perspective(glm.radians(camera.zoom), SCR_WIDTH * 1.0 / SCR_HEIGHT, 0.1, 200)

    view = camera.get_view_matrix()

    robot_program.use()
    # Load matrices in shader through set_matrix function
    robot_program.set_matrix("projection", glm.value_ptr(projection))
    robot_program.set_matrix("view", glm.value_ptr(view))

    m = glm.mat4(1.0)
    m = glm.rotate(m, glm.radians(-90), glm.vec3(1, 0, 0))
    m = glm.rotate(m, glm.radians(30), glm.vec3(0, 0, 1))
    robot_program.set_matrix("model", glm.value_ptr(m))

    robot_program.un_use()

    time0 = glfw.get_time()
    human_model.animation(robot_program, speed)
    time1 = glfw.get_time()
    
    delta_time = (time1 - time0)
    if delta_time < 16:
        time.sleep((16 - delta_time) / 1000)

def main():
    p = vlc.MediaPlayer("muse.mp3")
    p.play()
    glfw.init()
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3);
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3);
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE);
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE);
    glfw.window_hint(glfw.RESIZABLE, GL_FALSE)
    window = glfw.create_window(SCR_WIDTH, SCR_HEIGHT, "AHOY MATE", None, None)
    glfw.make_context_current(window)

    initp()
 
    while not glfw.window_should_close(window):
        drawFunc()
        glfw.poll_events()
        glfw.swap_buffers(window)
        glfw.swap_interval(1)
 
    glfw.terminate()

if __name__ == "__main__":
    main()
