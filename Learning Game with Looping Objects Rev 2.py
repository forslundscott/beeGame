import pygame
import random
#import hashlib

#def hashing_method():

pygame.init()

#count_sound = [pygame.mixer.Sound('N1.m4a'),pygame.mixer.Sound('N2.m4a'),pygame.mixer.Sound('N3.m4a'),pygame.mixer.Sound('N4.m4a'),pygame.mixer.Sound('N5.m4a')]
#next_sound = [pygame.mixer.Sound('W1.m4a'),pygame.mixer.Sound('W2.m4a'),pygame.mixer.Sound('W3.m4a'),pygame.mixer.Sound('W4.m4a'),pygame.mixer.Sound('W5.m4a')]

numbers = []
rndNumbers = []

firstNumber = 1
lastNumber = 5

for i in range(firstNumber,lastNumber+1):
    rndNumbers.append(i)
    print(lastNumber)

random.shuffle(rndNumbers)    

##print(rndNumbers)

gamewidth = 746
gameheight = 500



win = pygame.display.set_mode((gamewidth,gameheight))

pygame.display.set_caption("Learning Game")

hiveExit = pygame.image.load('Hive_Exit.png')
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
        self.width = 35
        self.height = 50
        self.size = 5
        self.val = val
        self.hitbox = (self.x-15, self.y-15, self.width+30,self.height+30)
        self.visible = True
    def draw (self,win, i):
        text = font.render(str(self.val), 1, (255,255,0))
        win.blit(text,(self.x,150))
##        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    def hit(self):
        self.visible = False
        
def redrawGameWindow():
    win.blit(bg, (0,0))
    bee.draw(win)
    i = 0
    for item in numbers:
        item.draw(win, i)
        i +=1
    if curNum == lastNumber + 1:
        textWin = font.render("You Win!", 1, (255,255,0))
        win.blit(textWin, (150,200))
        win.blit(hiveExit, (100,100))
    pygame.display.update()
    


#mainloop

font = pygame.font.SysFont('comicsans',70,True,True)
bee = player(300, 440, 20, 15)
##ans = [1,2,3,4,5,6,7,8,9,0,10]
##random.shuffle(ans)
x = 0
for i in rndNumbers:
    numberi = number(15 + (x*(680/(lastNumber-1))),150,20,15,i)
    numbers.append(numberi)
    x+=1

curNum = firstNumber
run = True
while run:
    clock.tick(22)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for number in numbers:
        if number.hitbox[1] < bee.hitbox[1] + bee.hitbox[3] and number.hitbox[1]+number.hitbox[3] > bee.hitbox[1]:
            if number.hitbox[0] + number.hitbox[2] > bee.hitbox[0] and number.hitbox[0] < bee.hitbox[0] + bee.hitbox[2] and curNum == number.val:
                number.hit()
                numbers.pop(numbers.index(number))
                curNum += 1

    
            
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
    if curNum == lastNumber + 1:
        textWin = font.render("You Win!", 1, (255,255,0))
##        run = False
        
    redrawGameWindow()
pygame.quit()
