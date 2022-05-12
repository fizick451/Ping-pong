from pygame import *
from pygame import Surface
from random import *

#создай окно игры
win_height = 500
win_width = 700

win = display.set_mode((win_width, win_height))

display.set_caption('ping-pong')

bg = transform.scale(image.load("pngtree-dark-blue-marble-agate-background-texture-picture-image_986749.jpg"),(700, 500))

#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()


font.init()
font1 = font.SysFont('Arial',25)
text_lose = font1.render(
    "Пропущено: " , 1, (255, 255, 255)
    )


class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y,size1,size2, player_speed):
                super().__init__()
                
                self.image = transform.scale(image.load(player_image),(size1, size2))
                self.speed = player_speed
                self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
        def reset(self):
                win.blit(self.image,(self.rect.x, self.rect.y))
        


class Player(GameSprite):
        def update(self):
                keys = key.get_pressed()
                if keys[K_LEFT] and self.rect.x > 5:
                        self.rect.x -= self.speed
                if keys[K_RIGHT] and self.rect.x < win_width - 80:
                        self.rect.x += self.speed
        #def fire(self):
                



clock = time.Clock()
FPS = 50       



finish = False
game = True
while game:
        
        for e in event.get():
                
                if e.type == QUIT:

                        game = False 
                #---------------------
                
        
        if finish != True:

                win.blit(bg,(0,0))
                
                
                #-----
                
                
                
                
                


        
        
        
        
        display.update()
        clock.tick(FPS)