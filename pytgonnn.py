import arcade 
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CRYST = "Кристалы и препятсвия"
PLAYER_SPEED = 5
ENEMY_SPEED = 2

WALLS_POSITIONS = [
    (SCREEN_WIDTH / 2 - 110, 10.5),
    (SCREEN_WIDTH / 2 - 220, 10.5),
    (25, 10.5),
    (SCRENN_WIDTH / 2, 10.5),
    (SCREEN_WIDTH / 2 + 110, 10.5),
    (SCREEN_WIDTH / 2 + 220, 10.5),
    (SCREEN_WIDTH - 25, 10.5),
    
    (SCRENN_WIDTH / 2 - 110,
SCREEN_HEIGHT - 10.5),
    (SCREEN_WIDTH / 2 - 220,
SCREEN_HEIGHT - 10.5),
    (25, SCREEN_HEIGHT - 10.5),
    (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10.5),
    (SCREEN_WIDTH / 2 + 110, 
SCREEN_HEIGHT - 10.5),
    (SCREEN_WIDTH - 25,
SCREEN_HEIGHT - 10.5),
    
    (10.5, SCREEN_HEIGHT / 2 - 110),
    (10.5, SCREEN_HEIGHT / 2 - 220),
    (10.5, SCREEN_HEIGHT / 2),
    (10.5, SCREEN_HEIGHT / 2 + 110),
    (10.5, SCREEN_HEIGHT / 2 + 220),
    
    (SCREEN_WIDTH - 10.5,
SCREEN_HEIGHT / 2 - 110),
    (SCREEN_WIDTH - 10.5,
SCREEN_HEIGHT / 2 - 200),
    (SCREEN_WIDTH - 10.5,
SCREEN_HEIGHT / 2),
    (SCREEN_WIDTH - 10.5,
SCREEN_HEIGHT / 2 + 110),
    (SCRENN_WIDTH - 10.5,
SCREEN_HEIGHT / 2 + 220),
]

COINS_POSITIONS = [(40, 375),
                   (375,100),
                   (200,300)]
    

    
    
    

PLAYER_TEXTURE =
ENEMY_TEXTURE = 
CRYST_TEXTURE = 
STY_TEXTURE = 

class Plaer(arcade.Sprite):
    def __init__(self):
        super().__init__(PLAYER_TEXTURE)
        self.center_x = 100
        self.center_y = 100
        self.speed = PLAYER_SPEED

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(ENEMY_TEXTURE)
        self.center_x = x
        self.cenetr_y = y
        self.min_x = min_x
        self.min_x = min_x
        self.change_x = 2 
        
    def update(self):
        self.center_x+=self.change_x
        if self.center_x < self.min_x or self.center_x > self.max_x:
            self.change_x *= -1
            
class CRYST(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(CRYST_TEXTURE)
        self.center_x = x
        self.center_y = y
        
class STY(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(STY_TEXTURE)
        self.center_x = x
        self.center_y = y
        
class MyGame(arcade.Window):
    def__init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT, TITLE)
        self.player = Player()
        self.enemies = arcade.SpriteList()
        self.crysts = arcade.SpriteList()
        self.stys = arcade.SrpiteList()
        self.setup()
        
    def setup(self):
        for i in range(3):
            enemy = Enemy