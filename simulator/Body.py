import numpy as np



class Body:

    def __init__(self, mass, color=(100, 100, 100), position=(0, 0), velocity=(0, 0), acceleration=(0, 0)):
        self.mass = mass
        self.color = color
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update_position(self):

        self.update_velocity()
        
        self.position = np.add(self.position, self.velocity)

    def update_velocity(self):

        self.velocity = np.add(self.velocity, self.acceleration)
    
    def set_acceleration(self, acceleration):
        self.acceleration = acceleration


    def get_position(self):
        return self.position