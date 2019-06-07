import math
import random
import arcade

# Screen
WIDTH = 1300
HEIGHT = 710

# Asteroids

asteroid1_x_positions = []
asteroid1_y_positions = []

asteroid2_x_positions = []
asteroid2_y_positions = []

asteroid3_x_positions = []
asteroid3_y_positions = []

for _ in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    asteroid1_x_positions.append(x)
    asteroid1_y_positions.append(y)

for _ in range(2):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT * 2)
    asteroid2_x_positions.append(x)
    asteroid2_y_positions.append(y)

for _ in range(4):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT * 2)
    asteroid3_x_positions.append(x)
    asteroid3_y_positions.append(y)

large_asteroid = [x, y, 125, arcade.color.BROWN_NOSE]
Medium_asteroid = [x, y, 75, arcade.color.LIGHT_BROWN]
Small_asteroid = [x, y, 40, arcade.color.COCOA_BROWN]

# Ship
ship_x_position = WIDTH/2
ship_y_position = 75
ship = [ship_x_position, ship_y_position, 50, arcade.color.BLUE]

#controls
left_pressed = False
right_pressed = False
movement = 20

heart1_x = 50
heart1_y = 50
heart1 = [heart1_x, heart1_y, ]
# Health = [heart1, heart2, heart3]


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

    if ship_x_position > WIDTH - 50:
        ship_x_position = WIDTH - 50

    elif ship_x_position < 50:
        ship_x_position = 50

# Asteroids
    for index in range(1):
        asteroid1_y_positions[index] -= 1
        if asteroid1_y_positions[index] < -175:
            asteroid1_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
            asteroid1_x_positions[index] = random.randrange(200, 1000)

    for index in range(2):
        asteroid2_y_positions[index] -= 3
        if asteroid2_y_positions[index] < -175:
            asteroid2_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
            asteroid2_x_positions[index] = random.randrange(200, 1000)

    for index in range(4):
        asteroid3_y_positions[index] -= 5
        if asteroid3_y_positions[index] < -175:
            asteroid3_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
            asteroid3_x_positions[index] = random.randrange(200, 1000)

# Collision
    a = large_asteroid[0] - ship[0]
    b = large_asteroid[1] - ship[1]
    dist1 = math.sqrt(a ** 2 + b ** 2)

    if dist1 < large_asteroid[2] + ship[2]:
        print("they are touching")

    c = Medium_asteroid[0] - ship[0]
    d = Medium_asteroid[1] - ship[1]
    dist2 = math.sqrt(c ** 2 + d ** 2)

    if dist2 < Medium_asteroid[2] + ship[2]:
        print("they are touching")

    e = Small_asteroid[0] - ship[0]
    f = Small_asteroid[1] - ship[1]
    dist3 = math.sqrt(e ** 2 + f ** 2)

    if dist3 < Small_asteroid[2] + ship[2]:
        print("they are touching")

def on_draw():
    arcade.start_render()
    # Draw in here...

#Ship
    draw_ship(ship_x_position, ship_y_position)

# asteroids
    for x, y in zip(asteroid1_x_positions, asteroid1_y_positions):
        draw_meteor1(x, y)

    for x, y in zip(asteroid2_x_positions, asteroid2_y_positions):
        draw_meteor2(x, y)

    for x, y in zip(asteroid3_x_positions, asteroid3_y_positions):
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

# Screen Functions


# Play Functions
def draw_meteor1(x, y):
    arcade.draw_circle_filled(x, y, 125, arcade.color.BROWN_NOSE)

def draw_meteor2(x, y):
    arcade.draw_circle_filled(x, y, 75, arcade.color.LIGHT_BROWN)

def draw_meteor3(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.COCOA_BROWN)

def draw_ship(x, y):
    arcade.draw_circle_filled(ship[1], ship[2], ship[3], arcade.color.BLUE)
    arcade.draw_rectangle_filled(ship[1], ship[2], ship[3], 100, arcade.color.RED)

def draw_heart1(x,y):
    arcade.draw_circle_filled(heart1_x, heart1_y, 25, arcade.color.RED)

if __name__ == '__main__':
    setup()
