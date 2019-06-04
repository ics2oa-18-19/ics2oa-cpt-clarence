import math
import random
import arcade

# Screen
WIDTH = 1365
HEIGHT = 710

# Astroids
meteor1_x_positions = []
meteor1_y_positions = []

meteor2_x_positions = []
meteor2_y_positions = []

meteor3_x_positions = []
meteor3_y_positions = []


for _ in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    meteor1_x_positions.append(x)
    meteor1_y_positions.append(y)

for _ in range(2):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT * 2)
    meteor2_x_positions.append(x)
    meteor2_y_positions.append(y)

for _ in range(4):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT * 2)
    meteor3_x_positions.append(x)
    meteor3_y_positions.append(y)

# Ship
ship_x_position = WIDTH/2
ship_y_position = 75

left_pressed = False
right_pressed = False
movement = 15


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
# ship
    global left_pressed, right_pressed, ship_x_position
    if left_pressed:
        ship_x_position -= movement

    elif right_pressed:
        ship_x_position += movement


# Asteroids
    for index in range(1):
        meteor1_y_positions[index] -= 1
        if meteor1_y_positions[index] < -175:
            meteor1_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
            meteor1_x_positions[index] = random.randrange(200, 1000)

    for index in range(2):
        meteor2_y_positions[index] -= 3
        if meteor2_y_positions[index] < -175:
            meteor2_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
            meteor2_x_positions[index] = random.randrange(200, 1000)

    for index in range(4):
        meteor3_y_positions[index] -= 5
        if meteor3_y_positions[index] < -175:
            meteor3_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
            meteor3_x_positions[index] = random.randrange(200, 1000)


def on_draw():
    arcade.start_render()
    # Draw in here...
#Ship
    draw_ship(ship_x_position, ship_y_position)

# asteroids
    for x, y in zip(meteor1_x_positions, meteor1_y_positions):
        draw_meteor1(x, y)

    for x, y in zip(meteor2_x_positions, meteor2_y_positions):
        draw_meteor2(x, y)

    for x, y in zip(meteor3_x_positions, meteor3_y_positions):
        draw_meteor3(x, y)

def on_key_press(key, modifiers):
    global left_pressed, right_pressed
    if key == arcade.key.A:
        left_pressed = True

    elif key == arcade.key.D:
        right_pressed = True

def on_key_release(key, modifiers):
    global left_pressed, right_pressed
    if key == arcade.key.A:
        left_pressed = False

    elif key == arcade.key.D:
        right_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass

def draw_meteor1(x, y):
    arcade.draw_circle_filled(x, y, 125, arcade.color.BROWN_NOSE)

def draw_meteor2(x, y):
    arcade.draw_circle_filled(x, y, 75, arcade.color.LIGHT_BROWN)

def draw_meteor3(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.COCOA_BROWN)

def draw_ship(x, y):
    arcade.draw_circle_filled(ship_x_position, ship_y_position, 50, arcade.color.BLUE)


if __name__ == '__main__':
    setup()
