import glm


class Camera3D():
    def __init__(self, position=glm.vec3(0.0, 0.0, 0.0), up=glm.vec3(0.0, 1.0, 0.0), yaw=-90, pitch=0,
                 front=glm.vec3(0.0, 0.0, -1.0), movement_speed=50, mouse_sensitivity=0.1, zoom=45.0):
        self.position = position
        self.world_up = up
        self.yaw = yaw
        self.pitch = pitch
        self.front = front
        self.movement_speed = movement_speed
        self.mouse_sensitivity = mouse_sensitivity
        self.zoom = zoom


    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.world_up)