Final Project CS515 Computer Graphics

Lakshya 2017eeb1149

To run the program:
	$ python Skeleton.py

The program is simply animation of a running character (also music in background)

My contribution has been creating all the code files:
	Skeleton.py
		The main file to handle the window, run the draw function and setup the different objects like camera.
	shader.py
		Initialize and handle the shaders
	camera3D.py
		Camera setup
	model_loader.py
		Most work went into this. This file includes the animation transforms and loading the entire model and animaiton from the collada file that can be generated using any modern 3d modelling software.
		Parse the collada file
		extract the vertex coordinates, texture mapping coordinates, bone structure and mapping, transformation matrices for all bones at different keyframes w.r.t parent bones.
		implemented keyframe interpolation using quaternions and weighted average
		implemented transformation generation and pose setter based on current timestep

	shader_robot.fg
	shader_robot.vs

	Getting the libraries to work together without OS issues ;_;


dependencies:
pycollada                 0.6
pyopengl-accelerate       3.1.5
pyopengl                  3.1.5
transformations           2020.1.1
glm                       0.9.9.4 
glfw                      1.12.0
numpy                     1.19.2
pillow                    8.0.0
python-vlc          3.0.11115

References:
	https://www.youtube.com/playlist?list=PLRIWtICgwaX2tKWCxdeB7Wv_rTET9JtWW