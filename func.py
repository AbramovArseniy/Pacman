import pygame


def update_screen(objects, screen):
    objects[0].change_direction(screen)
    objects[0].draw(objects)
    for ind, obj in enumerate(objects):
        if ind != 0:
            obj.draw()
    pygame.display.flip()
    screen.fill("Black")
