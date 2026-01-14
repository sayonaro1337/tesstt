import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class RecoveryGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Welcome Back!")
        arcade.set_background_color(arcade.color.BLACK)
        
        self.all_sprites = arcade.SpriteList()
        
        self.asteroid = arcade.Sprite(":resources:images/space/asteroid_1.png")
        self.asteroid.center_x = 100
        self.asteroid.center_y = 100
        self.asteroid.change_x = 2
        self.asteroid.change_y = 2
        self.all_sprites.append(self.asteroid)
        
        self.star = arcade.Sprite(":resources:images/items/star.png", scale=0.8)
        self.star.center_x = 400
        self.star.center_y = 300
        self.all_sprites.append(self.star)
        
        self.star_scale_step = 0.01
        self.star_angle_step = 3
        
        self.player = arcade.Sprite(":resources:/images/space_shooter/meteorGrey_big2.png", scale=0.5)
        self.player.center_x = 400
        self.player.center_y = 100
        self.all_sprites.append(self.player)

    def on_draw(self):
        self.clear() 
        self.all_sprites.draw()  

    def update(self, delta_time):
        for sprite in self.all_sprites:
            sprite.update()
        
        if self.asteroid.right > SCREEN_WIDTH or self.asteroid.left < 0:
            self.asteroid.center_x %= SCREEN_WIDTH
        if self.asteroid.top > SCREEN_HEIGHT or self.asteroid.bottom < 0:
            self.asteroid.center_y %= SCREEN_HEIGHT
        
        self.star.angle += self.star_angle_step
        
        new_scale = self.star.scale[0] + self.star_scale_step
        if new_scale > 1.2 or new_scale < 0.5:
            self.star_scale_step *= -1
        self.star.scale = (new_scale, new_scale)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -5
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5
        elif key == arcade.key.SPACE:
            self.player.scale = (1, 1) if self.player.scale != (1, 1) else (2, 2)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

if __name__ == "__main__":
    game = RecoveryGame()
    arcade.run()