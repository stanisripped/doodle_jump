import sys, pygame, os
pygame.init()

width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("doodle jump")

WHITE = (255, 255, 255)

FPS = 60

CHAR = pygame.image.load(os.path.join('images', 'doodle_boi.png'))

def draw_window():
    win.fill(WHITE)
    win.blit(CHAR, (300, 100))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()
