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
button_exit = [20, HEIGHT-60, 50, 50, False, arcade.color.RED,
                       arcade.color.GREEN, arcade.color.BLACK]
#Ship
ship_x_position = 0
ship_y_position = 1
ship_speed = 2
ship_color = 3
ship = [WIDTH/2, 75, 30, arcade.color.BLUE]

#Controls
left_pressed = False
right_pressed = False
movement = 20

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
            ship_x_position -= movement
        elif right_pressed:
            ship_x_position += movement
        if ship_x_position > WIDTH - 50:
            ship_x_position = WIDTH - 50
        elif ship_x_position < 50:
            ship_x_position = 50

def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()
        draw_ship(ship_x_position, ship_y_position)

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
        if (x > button_exit[BTN_X] and x < button_exit[BTN_X] + button_exit[BTN_WIDTH] and
                y > button_exit[BTN_Y] and y < button_exit[BTN_Y] + button_exit[BTN_HEIGHT]):
            button_exit[BTN_IS_CLICKED] = True
            current_screen = "menu"

def on_mouse_release(x, y, button, modifiers):
    global current_screen
    if current_screen == "menu":
        button_instructions[BTN_IS_CLICKED] = False
        button_play[BTN_IS_CLICKED] = False
    elif current_screen == "instructions":
        button_back_menu[BTN_IS_CLICKED] = False
    elif current_screen == "play":
        button_exit[BTN_IS_CLICKED] = False


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
    if button_exit[BTN_IS_CLICKED]:
        color3 = button_exit[BTN_CLICKED_COLOR]
    else:
        color3 = button_exit[BTN_COLOR]
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
    arcade.draw_text("=", button_exit[BTN_X]+15,
                 button_exit[BTN_Y] + 15, arcade.color.WHITE, font_size=20)

def draw_ship(x, y):
    arcade.draw_circle_filled(ship_x_position, ship_y_position, 50, arcade.color.BLUE)
    arcade.draw_rectangle_filled(x, y, 100, 40, arcade.color.BLUE)
    arcade.draw_rectangle_filled(x, y+20, 40, 100, arcade.color.BLUE)

if __name__ == '__main__':
    setup()
