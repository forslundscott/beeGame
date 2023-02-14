import pygame
import random
#import hashlib

#def hashing_method():

pygame.init()

ans = []

for i in range(0,10):
    ans.append(i)

map("unicode",ans)

gamewidth = 746
gameheight = 500

firstNumber = 0
lastNumber = 10

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

class number(object):
    def __init__(self, x, y, width, height,val):
        self.x = x
        self.y = y
        self.width = 85
        self.height = 50
        self.size = 5
        self.val = val
    def draw (self,win):
        text = font.render(str(ans[i]), 1, (255,255,0))
        win.blit(text,(200,150))
        
def redrawGameWindow():
    win.blit(bg, (0,0))
    bee.draw(win)
    for item in ans:
        ans[i].draw(win)
##    number1.draw(win)
##    number2.draw(win)
##    number3.draw(win)
##    number4.draw(win)
##    number5.draw(win)
##    number6.draw(win)
##    number7.draw(win)
##    number8.draw(win)
##    number9.draw(win)
##    number10.draw(win)
##    number11.draw(win)
    
    pygame.display.update()
    


#mainloop

font = pygame.font.SysFont('comicsans',30,True,True)
bee = player(300, 440, 20, 15)
##ans = [1,2,3,4,5,6,7,8,9,0,10]
##random.shuffle(ans)
for i in range(0,10):
    ans[i] = number(400,150,20,15,0)

##number1 = number(400,150,20,15,0)
##number2 = number(300,150,20,15,1)
##number3 = number(200,150,20,15,2)
##number4 = number(100,150,20,15,3)
##number5 = number(100,350,20,15,4)
##number6 = number(100,350,20,15,5)
##number7 = number(200,350,20,15,6)
##number8 = number(300,350,20,15,7)
##number9 = number(400,350,20,15,8)
##number10 = number(200,250,20,15,9)
##number11 = number(200,50,20,15,10)
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
