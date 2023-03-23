import pygame
import numpy as np

from Body import Body


pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Gravity Simulator")

# G_const = 


def gravity(one: Body, two: Body):
    
    distance = np.subtract(one.position, two.position)

    distance_mag =  np.linalg.norm(distance)

    direction_unit = distance / distance_mag

    # print(f"unit: {distance / distance_mag}")

    force = one.mass * two.mass / (distance_mag ** 2)

    return force * direction_unit


def accel_due_gravity(gravity, mass: float):

    return np.array(gravity) / mass



def display_bodies(bodies):

    for body in bodies:
        pygame.draw.circle(win, body.color, body.get_position(), 10)

        


def main():

    x0, y0 = 300, 200
    vx0, vy0 = -2, 0
    ax0, ay0 = 0, 0


    moon = Body(400, position=(x0, y0), velocity=(vx0, vy0), acceleration=(ax0, ay0))

    earth = Body(400, (100, 200, 100), (200, 373.20508), (1, 1.720508), (0, 0))

    mars = Body(400, (200, 100, 100), (400, 373.20508), (1, -1.720508), (0, 0))

    bodies = [moon, earth, mars]




    run = True

    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        win.fill((0, 0, 0))

        moon_earth_gravity = gravity(moon, earth)

        moon_mars_gravity = gravity(moon, mars)

        mars_earth_gravity = gravity(mars, earth)

        moon_acceleraton = accel_due_gravity(-moon_earth_gravity, moon.mass) + accel_due_gravity(-moon_mars_gravity, moon.mass)
        earth_acceleration = accel_due_gravity(moon_earth_gravity, earth.mass) + accel_due_gravity(mars_earth_gravity, earth.mass)
        mars_acceleration = accel_due_gravity(moon_mars_gravity, mars.mass) + accel_due_gravity(-mars_earth_gravity, mars.mass)


        moon.set_acceleration(moon_acceleraton)
        earth.set_acceleration(earth_acceleration)
        mars.set_acceleration(mars_acceleration)

        earth.update_velocity()
        earth.update_position()

        moon.update_velocity()
        moon.update_position()

        mars.update_velocity()
        mars.update_position()

        # x, y = 

        # ex, ey = 

        # print(gravity(moon, earth))



        # pygame.draw.circle(win, (113, 113, 113), moon.get_position(), 10)

        # pygame.draw.circle(win, (113, 200, 113), earth.get_position(), 20)

        # pygame.draw.circle(win, (200, 100, 100), mars.get_position(), 15)

        display_bodies(bodies)

        pygame.display.update()



main()
