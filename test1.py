import pygame
import os
import sys

if __name__ == '__main__':

    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)


    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    pos = 0, -600
    image = load_image('arrow.png')
    cursor_sprite = pygame.sprite.Group()
    cursor = pygame.sprite.Sprite(cursor_sprite)
    cursor.image = image
    cursor.rect = cursor.image.get_rect()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
                cursor.rect.x = pos[0]
                cursor.rect.y = pos[1]
            if not pygame.mouse.get_focused():
                cursor.rect.x = 0
                cursor.rect.y = -900
        cursor_sprite.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()