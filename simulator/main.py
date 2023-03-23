import pygame
import numpy as np

from Body import Body


pygame.init()

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Gravity Simulator")

# G_const = 

def gravity(one: Body, two: Body):
    # distance vector from body 2 to body 1
    distance = np.subtract(one.position, two.position)
    # scalar magnitude of distance
    distance_mag =  np.linalg.norm(distance)
    # unit vector in the direction of body 1 from body 2
    direction_unit = distance / distance_mag

    # Newton G force magnitude
    force = one.mass * two.mass / (distance_mag ** 2)

    # vector of magnitude force in the direction of body 2 from body 1
    return force * direction_unit

def accel_due_gravity(gravity, mass: float):
    # good old second law of Newton
    return np.array(gravity) / mass

def display_bodies(bodies):
    for body in bodies:
        pygame.draw.circle(win, body.color, body.get_position(), body.radius)


def dynamics(bodies: list[Body]):
    # set accelerations to 0 in order to resum them
    for body in bodies:
        body.acceleration = (0, 0)

    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies[i+1:]):
            current_force = gravity(body1, body2)

            body2.acceleration = np.add(body2.acceleration, accel_due_gravity(current_force, body2.mass))
            body1.acceleration = np.add(body1.acceleration, -accel_due_gravity(current_force, body1.mass))
        
        body1.update_velocity()
        body1.update_position()

def get_bodies():
    sun = Body(3500, 15, (250, 250, 0), (400, 415.47), (0, 0), (0, 0))

    mercury = Body(50, 5, (100, 100, 100), (400, 350), (-8, 0))

    earth = Body(50, 8, (100, 130, 200), (300, 473.20508), (4, 6.92820323), (0, 0))

    mars = Body(50, 7, (200, 100, 100), (600, 600), (3, -4), (0, 0))
    phobos = Body(1, 3, (100, 100, 100), (620, 620), (4.2, -5.3), (0, 0))

    return [sun, mercury, earth, mars, phobos]



def main():

    # getting list of Body objects
    bodies = get_bodies()

    run = True

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Recalculates new accelerations for each body
        dynamics(bodies)

        win.fill((0, 0, 0))

        display_bodies(bodies)

        pygame.display.update()


main()
