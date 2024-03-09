import pygame


pygame.init()

logo = 'logo.bmp'

surface = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
pygame.display.set_caption('Tic Tac Toe')
pygame.display.set_icon(pygame.image.load(logo))


clock = pygame.time.Clock()
FPS = 30

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

    clock.tick(FPS)
