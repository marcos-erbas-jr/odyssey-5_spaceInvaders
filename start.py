import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Space Invaders')
#icon = pygame.image.load('spaceInvaders.png')
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#desenho do player
    pygame.draw.rect(screen, (255, 255, 255), ((20, 10), (10, 10)))
    pygame.draw.rect(screen, (255,255,255), ((10,20), (30,10)))



    pygame.display.flip()
    pygame.time.Clock().tick()

pygame.quit()