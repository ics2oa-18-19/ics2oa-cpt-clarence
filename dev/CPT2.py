import math
import random
import arcade
import os

#Screen
WIDTH = 1300
HEIGHT = 740
current_screen = "menu"

#Buttons
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6
BTN_OUTLINE_COLOR = 7
button_instructions = [WIDTH/2 - 150, HEIGHT/2 - 60, 300, 50, False, arcade.color.BLUE,
                       arcade.color.GREEN, arcade.color.BLACK]
button_play = [WIDTH/2 - 150, HEIGHT/2, 300, 50, False, arcade.color.BLUE,
                       arcade.color.GREEN, arcade.color.BLACK]
button_back_menu = [WIDTH/2 - 150, HEIGHT/2 - 100, 300, 50, False, arcade.color.RED,
                       arcade.color.GREEN, arcade.color.BLACK]
button_pause = [20, HEIGHT-60, 50, 50, False, arcade.color.RED,
                       arcade.color.GREEN, arcade.color.ASH_GREY]
button_exit = [WIDTH/2 - 150, HEIGHT/2 - 100, 300, 50, False, arcade.color.RED,
                       arcade.color.GREEN, arcade.color.ASH_GREY]
button_resume = [WIDTH/2 - 150, HEIGHT/2, 300, 50, False, arcade.color.BLUE,
                       arcade.color.GREEN, arcade.color.ASH_GREY]
#Ship
ship_x_position = 0
ship_y_position = 1
ship_color = arcade.color.BATTLESHIP_GREY
ship = [WIDTH/2, 75]

#Controls
left_pressed = False
right_pressed = False
movement = 20

#Asteroids
asteroid1_x_positions = []
asteroid1_y_positions = []


for _ in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    asteroid1_x_positions.append(x)
    asteroid1_y_positions.append(y)
    large_asteroid = [x, y, 125]

#Hitboxes
HIT_BOX_X = 0
HIT_BOX_Y = 1
HIT_BOX_R = 2
HIT_BOX_CLR = 3
ship_hitbox = [ship[ship_x_position], ship[ship_y_position], 100, arcade.color.RED]

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    global left_pressed, right_pressed, ship_x_position, current_screen, ship
    if current_screen == "play":
        if left_pressed:
            ship[ship_x_position] -= movement
            ship_hitbox[HIT_BOX_X] -= movement
        elif right_pressed:
            ship[ship_x_position] += movement
            ship_hitbox[HIT_BOX_X] += movement
        if ship[ship_x_position] > WIDTH - 50:
            ship[ship_x_position] = WIDTH - 50
            ship_hitbox[HIT_BOX_X] = WIDTH - 50
        elif ship[ship_x_position] < 50:
            ship[ship_x_position] = 50
            ship_hitbox[HIT_BOX_X] = 50

        if button_play[BTN_IS_CLICKED] == True:
            for index in range (1):
                asteroid1_y_positions[index] -= 1
                if asteroid1_y_positions[index] < -175:
                    asteroid1_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
                    asteroid1_x_positions[index] = random.randrange(200, 1000)

                a = asteroid1_x_positions[index] - ship_hitbox[HIT_BOX_X]
                b = asteroid1_y_positions[index] - ship_hitbox[HIT_BOX_Y]
                dist = math.sqrt(a ** 2 + b ** 2)
                if dist < large_asteroid[2] + ship_hitbox[HIT_BOX_R]:
                    asteroid1_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 300)
                    asteroid1_x_positions[index] = random.randrange(250, 800)

def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        for x, y in zip(asteroid1_x_positions, asteroid1_y_positions):
            draw_asteroid1(x, y)
        draw_ship(ship_x_position, ship_y_position)
        draw_ship_hitbox(ship_hitbox[HIT_BOX_X], ship_hitbox[HIT_BOX_Y])
        draw_play()
    elif current_screen == "pause":
        draw_ship(ship_x_position, ship_y_position)
        draw_pause()

def on_key_press(key, modifiers):
    global left_pressed, right_pressed, current_screen
    if current_screen == "play":
        if key == arcade.key.A:
                left_pressed = True
        elif key == arcade.key.D:
                right_pressed = True


def on_key_release(key, modifiers):
    global left_pressed, right_pressed, current_screen
    if current_screen == "play":
        if key == arcade.key.A:
            left_pressed = False
        elif key == arcade.key.D:
            right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    global current_screen
    if current_screen == "menu":
        if (x > button_instructions[BTN_X] and x < button_instructions[BTN_X] + button_instructions[BTN_WIDTH] and
                y > button_instructions[BTN_Y] and y < button_instructions[BTN_Y] + button_instructions[BTN_HEIGHT]):
            button_instructions[BTN_IS_CLICKED] = True

            current_screen = "instructions"
        elif (x > button_play[BTN_X] and x < button_play[BTN_X] + button_play[BTN_WIDTH] and
                y > button_play[BTN_Y] and y < button_play[BTN_Y] + button_play[BTN_HEIGHT]):
            button_play[BTN_IS_CLICKED] = True
            current_screen = "play"

        if (x > button_play[BTN_X] and x < button_play[BTN_X] + button_play[BTN_WIDTH] and
                y > button_play[BTN_Y] and y < button_play[BTN_Y] + button_play[BTN_HEIGHT]):
            button_play[BTN_IS_CLICKED] = True

    elif current_screen == "instructions":
        if (x > button_back_menu[BTN_X] and x < button_back_menu[BTN_X] + button_back_menu[BTN_WIDTH] and
                y > button_back_menu[BTN_Y] and y < button_back_menu[BTN_Y] + button_back_menu[BTN_HEIGHT]):
            button_back_menu[BTN_IS_CLICKED] = True
            current_screen = "menu"

    elif current_screen == "play":
        if (x > button_pause[BTN_X] and x < button_pause[BTN_X] + button_pause[BTN_WIDTH] and
                y > button_pause[BTN_Y] and y < button_pause[BTN_Y] + button_pause[BTN_HEIGHT]):
            button_pause[BTN_IS_CLICKED] = True
            current_screen = "pause"

    elif current_screen == "pause":
        if (x > button_exit[BTN_X] and x < button_exit[BTN_X] + button_exit[BTN_WIDTH] and
                y > button_exit[BTN_Y] and y < button_exit[BTN_Y] + button_exit[BTN_HEIGHT]):
            button_exit[BTN_IS_CLICKED] = True
            current_screen = "menu"
        elif (x > button_resume[BTN_X] and x < button_resume[BTN_X] + button_resume[BTN_WIDTH] and
                y > button_resume[BTN_Y] and y < button_resume[BTN_Y] + button_resume[BTN_HEIGHT]):
            button_resume[BTN_IS_CLICKED] = True
            current_screen = "play"

def on_mouse_release(x, y, button, modifiers):
    global current_screen
    if current_screen == "menu":
        button_instructions[BTN_IS_CLICKED] = False
        button_play[BTN_IS_CLICKED] = False
    elif current_screen == "instructions":
        button_back_menu[BTN_IS_CLICKED] = False
    elif current_screen == "play":
        button_pause[BTN_IS_CLICKED] = False
    elif current_screen == "pause":
        button_exit[BTN_IS_CLICKED] = False
        button_resume[BTN_IS_CLICKED] = False

def draw_menu():
    arcade.set_background_color(arcade.color.ORANGE)
    arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2 + 100,
                     arcade.color.BLACK, font_size=100, anchor_x="center")
    if button_instructions[BTN_IS_CLICKED]:
        color = button_instructions[BTN_CLICKED_COLOR]
    else:
        color = button_instructions[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_instructions[BTN_X]-1,
                                      button_instructions[BTN_Y]-1,
                                      button_instructions[BTN_WIDTH]+3,
                                      button_instructions[BTN_HEIGHT]+3,
                                      button_instructions[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_instructions[BTN_X],
                                      button_instructions[BTN_Y],
                                      button_instructions[BTN_WIDTH],
                                      button_instructions[BTN_HEIGHT],
                                      color)

    arcade.draw_text("Instructions", button_instructions[BTN_X] + 85,
                        button_instructions[BTN_Y] + 15, arcade.color.WHITE, font_size=20)

    if button_play[BTN_IS_CLICKED]:
        color2 = button_play[BTN_CLICKED_COLOR]
    else:
        color2 = button_play[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_play[BTN_X]-1,
                                      button_play[BTN_Y]-2,
                                      button_play[BTN_WIDTH]+3,
                                      button_play[BTN_HEIGHT]+3,
                                      button_play[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_play[BTN_X],
                                      button_play[BTN_Y],
                                      button_play[BTN_WIDTH],
                                      button_play[BTN_HEIGHT],
                                      color2)
    arcade.draw_text("Play", button_play[BTN_X] + 125, button_play[BTN_Y] + 15,
                        arcade.color.WHITE, font_size=20)

def draw_instructions():
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.draw_text("Instructions", WIDTH / 2, HEIGHT - 200,
                arcade.color.BLACK, font_size=100, anchor_x="center")
    arcade.draw_text("A to go left, B to go right", WIDTH / 2, HEIGHT / 2,
                arcade.color.BLACK, font_size=30, anchor_x="center")
    if button_back_menu[BTN_IS_CLICKED]:
        color3 = button_back_menu[BTN_CLICKED_COLOR]
    else:
        color3 = button_back_menu[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_back_menu[BTN_X]-1,
                                      button_back_menu[BTN_Y]-1,
                                      button_back_menu[BTN_WIDTH]+3,
                                      button_back_menu[BTN_HEIGHT]+3,
                                      button_back_menu[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_back_menu[BTN_X],
                                      button_back_menu[BTN_Y],
                                      button_back_menu[BTN_WIDTH],
                                      button_back_menu[BTN_HEIGHT],
                                      color3)

    arcade.draw_text("Go Back", button_back_menu[BTN_X] + 100,
                 button_back_menu[BTN_Y] + 15, arcade.color.WHITE, font_size=20)

def draw_play():
    arcade.set_background_color(arcade.color.BLACK)
    if button_pause[BTN_IS_CLICKED]:
        color3 = button_pause[BTN_CLICKED_COLOR]
    else:
        color3 = button_pause[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_pause[BTN_X]-1,
                                      button_pause[BTN_Y]-1,
                                      button_pause[BTN_WIDTH]+3,
                                      button_pause[BTN_HEIGHT]+3,
                                      button_pause[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_pause[BTN_X],
                                      button_pause[BTN_Y],
                                      button_pause[BTN_WIDTH],
                                      button_pause[BTN_HEIGHT],
                                      color3)
    arcade.draw_text("=", button_pause[BTN_X]+12,
                 button_pause[BTN_Y] + 7, arcade.color.WHITE, font_size=40)

def draw_pause():
    arcade.draw_text("Menu", WIDTH / 2, HEIGHT - 200,
                     arcade.color.ASH_GREY, font_size=100, anchor_x="center")
    if button_exit[BTN_IS_CLICKED]:
        color3 = button_exit[BTN_CLICKED_COLOR]
    else:
        color3 = button_exit[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(WIDTH/2-255,
                                      HEIGHT/2-180,
                                      505,
                                      305,
                                      arcade.color.ASH_GREY)
    arcade.draw_xywh_rectangle_filled(WIDTH/2-255,
                                      HEIGHT/2-180,
                                      500,
                                      300,
                                      arcade.color.YELLOW)
    arcade.draw_xywh_rectangle_filled(button_exit[BTN_X]-1,
                                      button_exit[BTN_Y]-1,
                                      button_exit[BTN_WIDTH]+3,
                                      button_exit[BTN_HEIGHT]+3,
                                      button_exit[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_exit[BTN_X],
                                      button_exit[BTN_Y],
                                      button_exit[BTN_WIDTH],
                                      button_exit[BTN_HEIGHT],
                                      color3)
    arcade.draw_text("Exit To Main Menu", button_exit[BTN_X] + 60,
                 button_exit[BTN_Y] + 15, arcade.color.WHITE, font_size=20)
#Resume Button
    arcade.draw_xywh_rectangle_filled(button_resume[BTN_X]-1,
                                      button_resume[BTN_Y]-1,
                                      button_resume[BTN_WIDTH]+3,
                                      button_resume[BTN_HEIGHT]+3,
                                      button_resume[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_resume[BTN_X],
                                      button_resume[BTN_Y],
                                      button_resume[BTN_WIDTH],
                                      button_resume[BTN_HEIGHT],
                                      button_resume[BTN_COLOR])
    arcade.draw_text("Resume", button_resume[BTN_X] + 100,
                 button_resume[BTN_Y] + 15, arcade.color.WHITE, font_size=20)


def draw_ship(x, y):
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_circle_filled(ship[ship_x_position], ship[ship_y_position], 50, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position], 100, 40, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]+50, 40, 100, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position]-50, ship[ship_y_position]+20, 20, 100, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position]+50, ship[ship_y_position]+20, 20, 100, ship_color)


def draw_asteroid1(x, y):
    arcade.draw_circle_filled(x, y, 125, arcade.color.BROWN_NOSE)

def draw_ship_hitbox(x, y):
    arcade.draw_circle_outline(ship_hitbox[HIT_BOX_X], ship_hitbox[HIT_BOX_Y],
                                       ship_hitbox[HIT_BOX_R], ship_hitbox[HIT_BOX_CLR])


if __name__ == '__main__':
    setup()
