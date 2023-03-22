



class Body:

    def __init__(self, mass, position=(0, 0), velocity=(0, 0), acceleration=(0, 0)):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update_position(self):
        x, y = self.position

        self.update_velocity()
        
        vx, vy = self.velocity

        x += vx
        y += vy

        self.position = (x, y)

    def update_velocity(self):

        vx, vy = self.velocity
        ax, ay = self.acceleration

        vx += ax
        vy += ay

        self.velocity = (vx, vy)


    def get_position(self):
        return self.position