from pygame import *



fps = time.Clock()
Fps = 60



class Game(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(80,80))
        self.speed = p_s
        self.rect= self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y



    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Move(Game):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -=  self.speed
        if keys[K_RIGHT] and self.rect.x<620:
            self.rect.x +=  self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -=  self.speed
        if keys[K_DOWN] and self.rect.y<420:
            self.rect.y +=  self.speed


class Enemy(Game):
    gold = "left"
    def move2(self):
        if self.rect.x <=470:
            self.gold = "right"    
        if self.rect.x >=620:
            self.gold = "left"
        if self.gold == "left":
            self.rect.x -= self.speed
        else:
            if self.gold == "right":
                self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))




window = display.set_mode((700,500))
display.set_caption("levron mr olimpia )))")


backgroud = transform.scale(image.load("cl.jpeg"),(700,500))
levron = Move("levron.png",5,420,4)
coleman = Enemy("coleman.gif",550,280,2)
medal = Game("medal.png",550,400,0)
wl1 = Wall(154,205,50,100,20,450,10)
wl2 = Wall(154,205,50,100,20,10,380)
wl3 = Wall(154,205,50,100,20,10,380)

game = True

mixer.init()
mixer.music.load("cevin.mp3")
mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False





    window.blit(backgroud,(0,0))
    levron.move()
    coleman.move2()
    coleman.reset()
    levron.reset()
    medal.reset()
    wl1.draw_wall()
    wl2.draw_wall()
    wl3.draw_wall()


    display.update()
    fps.tick(Fps)













