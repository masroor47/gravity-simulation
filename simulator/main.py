import pygame

from Body import Body


pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Gravity Simulator")






def main():

    x0, y0 = 200, 200
    vx0, vy0 = 3, 0
    ax0, ay0 = -0.1, 0


    moon = Body(10, (x0, y0), (vx0, vy0), (ax0, ay0))

    run = True

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        win.fill((0, 0, 0))

        moon.update_position()

        x, y = moon.get_position()

        pygame.draw.circle(win, (113, 113, 113), (x, y), 10)

        pygame.display.update()



main()
