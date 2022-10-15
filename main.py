# importing important modules
import pygame

# window rendering
display = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

player_imgs = ["player1.png", "player2.png", "player3.png", "player4.png"]
enemy_imgs = []

FPS = 5

# Background Class
class Background(pygame.Rect):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./gfx/bg.png")
    def update(self):
        display.blit(self.image, self)

# Player Class
class Player(pygame.Rect):
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y
        self.image = pygame.image.load(player_imgs[0])
    def update(self):
        display.blit(self.image, self)

# main game loop
def main():
    run = True
    bg = Background()
    clock.tick(FPS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        display.fill((255, 255, 255))
        bg.update()
        pygame.display.update()

# Checking if file is not imported
if __name__ == "__main__":
    main()