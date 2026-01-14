import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

class RecoveryGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Welcome Back!")
        arcade.set_background_color(arcade.color.BLACK)

        self.all_sprites = arcade.SpriteList()

        self.star = arcade.Sprite(":resources:images/items/star.png", scale=0.8)
        self.star.center_x = 400
        self.star.center_y = 300
        self.star.angle = 0
        self.star.change_angle = 2
        self.scale_speed = 0.005
        self.max_scale = 1
        self.min_scale = 0.5
        self.star.change_x = 2.6
        self.star.change_y = 2
        self.all_sprites.append(self.star)

        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite(":resources:/images/space_shooter/playerShip2_orange.png", scale=0.8)
        self.player.center_x = 400
        self.player.center_y = 300
        self.player_list.append(self.player)
        self.scale_speed = 0.01

    def on_draw(self):
        self.clear()
        self.all_sprites.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update_animation(delta_time)
        # 1. Вращение
        self.star.angle += self.star.change_angle

        current_s = self.star.scale[0]
        new_scale = current_s + self.scale_speed

        if new_scale >= self.max_scale or new_scale <= self.min_scale:
            self.scale_speed *= -1
        self.star.scale = new_scale

        self.star.center_x += self.star.change_x
        self.star.center_y += self.star.change_y
        if self.star.left > SCREEN_WIDTH:
            self.star.right = 0
        if self.star.bottom > SCREEN_HEIGHT:
            self.star.top = 0

        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y


    def on_key_press(self, key, modifiers):
        match key:
            case arcade.key.A:
                self.player.change_x = -MOVEMENT_SPEED
            case arcade.key.D:
                self.player.change_x = MOVEMENT_SPEED
            case arcade.key.W:
                self.player.change_y = MOVEMENT_SPEED
            case arcade.key.S:
                self.player.change_y = -MOVEMENT_SPEED
            case arcade.key.SPACE:
                self.player.scale = (1.5,1.5)

    def on_key_release(self, key, modifiers):
        match key:
            case arcade.key.A | arcade.key.D:
                self.player.change_x = 0
            case arcade.key.W | arcade.key.S:
                self.player.change_y = 0
            case arcade.key.SPACE:
                self.player.scale = (1,1)

if __name__ == "__main__":
    game = RecoveryGame()
    arcade.run()
