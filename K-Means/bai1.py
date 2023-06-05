import pygame

pygame.init()

screen = pygame.display.set_mode((1000,700))

pygame.display.set_caption("kmeans visualization")

running = True 

clock =pygame.time.Clock()
BLACK = (0,0,0)
BACKGROUND_PANEL =(249, 255, 230)



BACKGROUND = (214,214,214)

while running : 
    clock.tick(60)
    screen.fill(BACKGROUND)
    # Draw interface 
    # Draw panel 

    pygame.draw.rect(screen, BLACK  , (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL  , (55,55,690,490))

    # K button +
    pygame.draw.rect(screen,BLACK,(850,50,50,50))
    # End draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        pygame.display.flip()
pygame.quit()
