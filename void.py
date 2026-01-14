import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

MOVEMENT_SPEED = 5

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Космическая игра")
        arcade.set_background_color(arcade.color.BLACK)
        
        self.sprites = arcade.SpriteList()
        
        meteorite_image_path = ":resources:images/space_shooter/meteorGrey_big1.png"
        self.meteorite_sprite = arcade.Sprite(meteorite_image_path, scale=0.8)
        self.meteorite_sprite.position = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        self.meteorite_sprite.angle = 0
        self.meteorite_sprite.change_angle = 2
        self.scale_speed = 0.005
        self.max_scale = 1
        self.min_scale = 0.5
        self.meteorite_sprite.change_x = 2.6
        self.meteorite_sprite.change_y = 2
        self.sprites.append(self.meteorite_sprite)
        
        ship_image_path = ":resources:images/space_shooter/playerShip2_orange.png"
        self.player_ship = arcade.Sprite(ship_image_path, scale=0.8)
        self.player_ship.position = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        self.sprites.append(self.player_ship)
    
    def on_draw(self):
        self.clear()
        self.sprites.draw()
    
    def update_meteorite(self, dt):
        self.meteorite_sprite.angle += self.meteorite_sprite.change_angle
        
        current_scale = self.meteorite_sprite.scale[0]  
        new_scale = current_scale + self.scale_speed
        
        if new_scale >= self.max_scale or new_scale <= self.min_scale:
            self.scale_speed *= -1
        
        self.meteorite_sprite.scale = (new_scale, new_scale)
        
        self.meteorite_sprite.center_x += self.meteorite_sprite.change_x
        self.meteorite_sprite.center_y += self.meteorite_sprite.change_y
        
        if self.meteorite_sprite.left > WINDOW_WIDTH:
            self.meteorite_sprite.right = 0
        elif self.meteorite_sprite.right < 0:
            self.meteorite_sprite.left = WINDOW_WIDTH
        if self.meteorite_sprite.bottom > WINDOW_HEIGHT:
            self.meteorite_sprite.top = 0
        elif self.meteorite_sprite.top < 0:
            self.meteorite_sprite.bottom = WINDOW_HEIGHT
    
    def update_player(self, dt):
        self.player_ship.center_x += self.player_ship.change_x
        self.player_ship.center_y += self.player_ship.change_y
    
    def on_update(self, delta_time):
        self.update_meteorite(delta_time)
        self.update_player(delta_time)
    
    def on_key_press(self, key, modifiers):
        match key:
            case arcade.key.LEFT:
                self.player_ship.change_x = -MOVEMENT_SPEED
            case arcade.key.RIGHT:
                self.player_ship.change_x = MOVEMENT_SPEED
            case arcade.key.UP:
                self.player_ship.change_y = MOVEMENT_SPEED
            case arcade.key.DOWN:
                self.player_ship.change_y = -MOVEMENT_SPEED
            case arcade.key.SPACE:
                self.player_ship.scale = (1.5, 1.5)
    
    def on_key_release(self, key, modifiers):
        match key:
            case arcade.key.LEFT | arcade.key.RIGHT:
                self.player_ship.change_x = 0
            case arcade.key.UP | arcade.key.DOWN:
                self.player_ship.change_y = 0
            case arcade.key.SPACE:
                self.player_ship.scale = (1, 1)

if __name__ == "__main__":
    game_window = GameWindow()
    arcade.run()
