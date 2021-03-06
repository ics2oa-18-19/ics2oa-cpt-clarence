import math
import random
import arcade
import os

# Screen
WIDTH = 1300
HEIGHT = 740
current_screen = "menu"

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
    large_asteroid = [x, y, 125, arcade.color.BROWN_NOSE]

for _ in range(2):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT * 2)
    asteroid2_x_positions.append(x)
    asteroid2_y_positions.append(y)
    medium_asteroid = [x, y, 75, arcade.color.LIGHT_BROWN]

for _ in range(4):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT * 2)
    asteroid3_x_positions.append(x)
    asteroid3_y_positions.append(y)
    small_asteroid = [x, y, 40, arcade.color.COCOA_BROWN]

# Ship
ship_x_position = WIDTH/2
ship_y_position = 75
ship = [ship_x_position, ship_y_position, 50, arcade.color.BLUE]

#controls
left_pressed = False
right_pressed = False
movement = 40

#Health
heart1_x = 0
heart1_y = 1
heart1 = [50, 50]

heart2_x = 0
heart2_y = 1
heart2 = [110, 50]

heart3_x = 0
heart3_y = 1
heart3 = [170, 50]

hearts_x = [heart1_x, heart2_x, heart3_x]
hearts_y = [heart1_y, heart2_y, heart3_y]
health = 3

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
    global left_pressed, right_pressed, ship_x_position, large_asteroid, Medium_asteroid, \
        Small_asteroid, current_screen, ship, health
    if current_screen == "play":
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
        dist = math.sqrt(a ** 2 + b ** 2)
        if dist < large_asteroid[2] + ship[2]:
            health -= 3

        a = medium_asteroid[0] - ship[0]
        b = medium_asteroid[1] - ship[1]
        dist = math.sqrt(a ** 2 + b ** 2)
        if dist < medium_asteroid[2] + ship[2]:
            health -= 2

        a = small_asteroid[0] - ship[0]
        b = small_asteroid[1] - ship[1]
        dist = math.sqrt(a ** 2 + b ** 2)
        if dist < small_asteroid[2] + ship[2]:
            health -= 1

        if health == 0:
            draw_gameover()

def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "play":
        arcade.set_background_color(arcade.color.BLACK)
#Ship
        draw_ship(ship_x_position, ship_y_position)

# asteroids
        for x, y in zip(asteroid1_x_positions, asteroid1_y_positions):
            draw_asteroid1(x, y)

        for x, y in zip(asteroid2_x_positions, asteroid2_y_positions):
            draw_asteroid2(x, y)

        for x, y in zip(asteroid3_x_positions, asteroid3_y_positions):
            draw_asteroid3(x, y)
#Hearts
        draw_hearts(hearts_x, hearts_y)
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "menu":
        draw_menu()
    elif current_screen == "gameover":
        draw_gameover()

def on_key_press(key, modifiers):
    global left_pressed, right_pressed, current_screen
    if current_screen == "play":
        if key == arcade.key.A:
                left_pressed = True

        elif key == arcade.key.D:
                right_pressed = True

def on_key_release(key, modifiers):
    global left_pressed, right_pressed, current_screen
    if current_screen == "menu":
        if key == arcade.key.I:
            current_screen = "instructions"
        elif key == arcade.key.P:
            current_screen = "play"
        elif key == arcade.key.ESCAPE:
            exit()
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    elif current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
        if key == arcade.key.A:
            left_pressed = False
        elif key == arcade.key.D:
            right_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass

# Screen Functions
def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("I for Instructions", WIDTH/2, HEIGHT/2-90,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text("P to Play", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")

def draw_instructions():
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("ESC to go back", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")

def draw_gameover():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.draw_text("Game Over", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")


# Play Functions
def draw_asteroid1(x, y):
    arcade.draw_circle_filled(x, y, 125, arcade.color.BROWN_NOSE)

def draw_asteroid2(x, y):
    arcade.draw_circle_filled(x, y, 75, arcade.color.LIGHT_BROWN)

def draw_asteroid3(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.COCOA_BROWN)

def draw_ship(x, y):
    arcade.draw_circle_filled(ship_x_position, ship_y_position, 50, arcade.color.BLUE)
    arcade.draw_rectangle_filled(x, y, 100, 40, arcade.color.BLUE)
    arcade.draw_rectangle_filled(x, y+20, 40, 100, arcade.color.BLUE)

def draw_hearts(hearts_x, hearts_y):
    arcade.draw_circle_filled(heart1[heart1_x], heart1[heart1_y], 25, arcade.color.RED)
    arcade.draw_circle_filled(heart2[heart2_x], heart2[heart2_y], 25, arcade.color.RED)
    arcade.draw_circle_filled(heart3[heart3_x], heart3[heart3_y], 25, arcade.color.RED)

if __name__ == '__main__':
    setup()
