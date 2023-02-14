import pygame
pygame.init()

gamewidth = 746
gameheight = 500

win = pygame.display.set_mode((gamewidth,gameheight))

pygame.display.set_caption("Learning Game")

flyRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png'),pygame.image.load('R10.png'),pygame.image.load('R11.png'),pygame.image.load('R12.png'),pygame.image.load('R13.png'),pygame.image.load('R14.png'),pygame.image.load('R15.png'),pygame.image.load('R16.png'),pygame.image.load('R17.png'),pygame.image.load('R18.png'),pygame.image.load('R19.png'),pygame.image.load('R20.png'),pygame.image.load('R21.png'),pygame.image.load('R22.png')]
flyLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png'),pygame.image.load('L10.png'),pygame.image.load('L11.png'),pygame.image.load('L12.png'),pygame.image.load('L13.png'),pygame.image.load('L14.png'),pygame.image.load('L15.png'),pygame.image.load('L16.png'),pygame.image.load('L17.png'),pygame.image.load('L18.png'),pygame.image.load('L19.png'),pygame.image.load('L20.png'),pygame.image.load('L21.png'),pygame.image.load('L22.png')]
bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = 85
        self.height = 50
        self.vel = 8
        self.flyCount = 0
        self.facing = -1
        self.hitbox = (self.x, self.y, self.width,self.height)
        

    def draw(self,win):
        if self.flyCount +1 >22:
            self.flyCount = 0
        if self.facing == -1:
            win.blit(flyLeft[self.flyCount//3],(self.x,self.y))
            self.flyCount += 1
        elif self.facing == 1:
            win.blit(flyRight[self.flyCount//3],(self.x,self.y))
            self.flyCount += 1
        self.hitbox = (self.x, self.y, self.width,self.height)
##        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

        
def redrawGameWindow():
    win.blit(bg, (0,0))
    bee.draw(win)
    pygame.display.update()
    

#mainloop
bee = player(50, 440, 20, 15)
run = True
while run:
    clock.tick(22)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and bee.x > bee.vel:
        bee.x -= bee.vel
        bee.facing = -1
    elif keys[pygame.K_RIGHT] and bee.x < gamewidth - bee.width - bee.vel:
        bee.x += bee.vel
        bee.facing = 1

    if keys[pygame.K_UP] and bee.y > bee.vel:
        bee.y -= bee.vel

    if keys[pygame.K_DOWN] and bee.y < gameheight - bee.height - bee.vel:
        bee.y += bee.vel
        
    redrawGameWindow()
pygame.quit()
