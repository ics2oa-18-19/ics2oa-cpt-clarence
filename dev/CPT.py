import random
import arcade

WIDTH = 1200
HEIGHT = 670

meteor_x_positions = []
meteor_y_positions = []

for _ in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    meteor_x_positions.append(x)
    meteor_y_positions.append(y)

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    for index in range(1):
        meteor_y_positions[index] -= 1
        if meteor_y_positions[index] < -175:
            meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT+300)
            meteor_x_positions[index] = random.randrange(200, 1000)


def on_draw():
    arcade.start_render()
    # Draw in here...
    for x, y in zip(meteor_x_positions, meteor_y_positions):
        draw_meteors(x, y)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_meteors(x, y):
    arcade.draw_circle_filled(x, y, 125, arcade.color.BROWN_NOSE)

if __name__ == '__main__':
    setup()

