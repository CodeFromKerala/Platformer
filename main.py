# importing important modules
import pygame

# window rendering
display = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

# Image Libraries
player_imgs = ["./gfx/player1.png", "./gfx/player2.png", "./gfx/player3.png", "./gfx/player4.png"]
btn_imgs = ["./gfx/play_btn.png", "./gfx/", "./gfx/", "./gfx/"]
enemy_imgs = []

# Frames Per Second
FPS = 1

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
        self.MoveA = False
        self.MoveD = False
        self.jump = False
    def update(self):
        if self.MoveD == True:
            self.centerx += 1
        if self.MoveA == True:
            self.centerx -= 1
        if self.jump == True:
            self.move([0, 20])
            self.jump = False
        if self.y > 450:
            self.centery += 1
        display.blit(self.image, self)

# Button Class

class Btn(pygame.Rect):
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y
        self.image = pygame.image.load(btn_imgs[0])
    def update(self):
        display.blit(self.image, self)
    def m_pressed(self):
        pos = pygame.mouse.get_pos()
        m_x = pos[0]
        m_y = pos[1]
        if (m_x > self.x and m_x < self.x + 100) and (m_y > self.y and m_y < self.y + 50):
            main()

# Start Screen loop
def Start():
    run = True
    bg = Background()
    btn = Btn(330, 400)
    clock.tick(FPS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                btn.m_pressed()
        display.fill((255, 255, 255))
        bg.update()
        btn.update()
        pygame.display.update()

# Main Game Loop
def main():
    run = True
    player = Player(450, 450)
    clock.tick(FPS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.MoveA = True
                if event.key == pygame.K_RIGHT:
                    player.MoveD = True
                if event.key == pygame.K_SPACE:
                    player.jump = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.MoveA = False
                if event.key == pygame.K_RIGHT:
                    player.MoveD = False
        display.fill((255, 255, 255))
        player.update()
        pygame.display.update()

# Checking if file is not imported
if __name__ == "__main__":
    Start()