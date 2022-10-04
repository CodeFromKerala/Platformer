# importing important modules
import pygame

# window rendering
display = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

FPS = 60

# main game loop
def main():
    run = True
    clock.tick(FPS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        display.fill((255, 255, 255))
        pygame.display.update()

# Checking if file is not imported
if __name__ == "__main__":
    main()