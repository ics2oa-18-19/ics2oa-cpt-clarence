import math
import random
import arcade

"""
Screen
"""
WIDTH = 1300
HEIGHT = 740
current_screen = "menu"

"""
Buttons
"""
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6
BTN_OUTLINE_COLOR = 7
button_instructions = [WIDTH/2 - 150, HEIGHT/2 - 60, 300, 50, False, arcade.color.PURPLE,
                       arcade.color.GREEN, arcade.color.WHITE]
button_play = [WIDTH/2 - 75, HEIGHT/2, 150, 50, False, arcade.color.DARK_BLUE,
                       arcade.color.GREEN, arcade.color.WHITE]
button_controls = [WIDTH/2 - 150, HEIGHT/2 - 120, 300, 50, False, arcade.color.BLACK,
                       arcade.color.GREEN, arcade.color.WHITE]
button_back_menu = [WIDTH/2 - 150, HEIGHT/2 - 100, 300, 50, False, arcade.color.RED,
                       arcade.color.GREEN, arcade.color.WHITE]
button_pause = [20, HEIGHT-60, 50, 50, False, arcade.color.RED,
                       arcade.color.GREEN, arcade.color.WHITE]
button_exit = [WIDTH/2 - 150, HEIGHT/2 - 100, 300, 50, False, arcade.color.DARK_RED,
                       arcade.color.GREEN, arcade.color.WHITE]
button_resume = [WIDTH/2 - 150, HEIGHT/2, 300, 50, False, arcade.color.DARK_BLUE,
                       arcade.color.GREEN, arcade.color.WHITE]
button_quit = [WIDTH/2 - 150, HEIGHT/2 - 60, 300, 50, False, arcade.color.DARK_RED,
                       arcade.color.GREEN, arcade.color.WHITE]
button_restart = [WIDTH/2 - 150, HEIGHT/2, 300, 50, False, arcade.color.DARK_BLUE,
                       arcade.color.GREEN, arcade.color.WHITE]
button_grey = [50, 50, 50, 50, False, arcade.color.BATTLESHIP_GREY,
                       arcade.color.GREEN, arcade.color.WHITE]
button_red = [50, 110, 50, 50, False, arcade.color.DARK_RED,
                       arcade.color.GREEN, arcade.color.WHITE]
button_blue = [50, 170, 50, 50, False, arcade.color.BLUE_SAPPHIRE,
                       arcade.color.GREEN, arcade.color.WHITE]
"""
Ship
"""
ship_x_position = 0
ship_y_position = 1
ship_color = arcade.color.BATTLESHIP_GREY
ship = [WIDTH/2, 75]

"""
Health
"""
health = 3

"""
Controls
"""
left_pressed = False
right_pressed = False
movement = 15

"""
Asteroids
"""
#Large
Large_ast_x = []
Large_ast_y = []

for _ in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    Large_ast_x.append(x)
    Large_ast_y.append(y)
    large_asteroid = [x, y, 125]

#Medium
Medium_ast_x = []
Medium_ast_y = []

for _ in range(3):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    Medium_ast_x.append(x)
    Medium_ast_y.append(y)
    medium_asteroid = [x, y, 75]

#Small
Small_ast_x = []
Small_ast_y = []

for _ in range(5):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    Small_ast_x.append(x)
    Small_ast_y.append(y)
    small_asteroid = [x, y, 50]

"""
Cores
"""
cores_x = []
cores_y = []

for _ in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT, HEIGHT*2)
    cores_x.append(x)
    cores_y.append(y)
    cores = [x, y, 30]

"""
Score
"""
score = 0

"""
Hitbox
"""
HIT_BOX_X = 0
HIT_BOX_Y = 1
HIT_BOX_R = 2
HIT_BOX_CLR = 3
ship_hitbox = [ship[ship_x_position], ship[ship_y_position]+20, 75, arcade.color.BLACK]

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release
    arcade.run()

def update(delta_time):
    update_play(delta_time)
    update_gameover(delta_time)

def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "controls":
        draw_controls()
    elif current_screen == "play":
        draw_ship_hitbox(ship_hitbox[HIT_BOX_X], ship_hitbox[HIT_BOX_Y])
        for x, y in zip(Large_ast_x, Large_ast_y):
            draw_large_asteroid(x, y)
        for x, y in zip(Medium_ast_x, Medium_ast_y):
            draw_medium_asteroid(x, y)
        for x, y in zip(Small_ast_x, Small_ast_y):
            draw_small_asteroid(x, y)
        for x, y in zip(cores_x, cores_y):
            draw_cores(x, y)
        draw_ship(ship_x_position, ship_y_position)
        draw_play()
    elif current_screen == "pause":
        draw_ship(ship_x_position, ship_y_position)
        draw_pause()
    elif current_screen == "gameover":
        draw_gameover()

def on_key_press(key, modifiers):
    global left_pressed, right_pressed, space_pressed, current_screen
    if current_screen == "play":
        if key == arcade.key.A:
                left_pressed = True
        elif key == arcade.key.D:
                right_pressed = True
        elif key == arcade.key.SPACE:
                space_pressed = True

def on_key_release(key, modifiers):
    global left_pressed, right_pressed, space_pressed, current_screen
    if current_screen == "play":
        if key == arcade.key.A:
            left_pressed = False
        elif key == arcade.key.D:
            right_pressed = False
        elif key == arcade.key.SPACE:
            space_pressed = False

def on_mouse_press(x, y, button, modifiers):
    button_collision(x, y, button, modifiers)

def on_mouse_release(x, y, button, modifiers):
    global current_screen
    if current_screen == "menu":
        button_instructions[BTN_IS_CLICKED] = False
        button_play[BTN_IS_CLICKED] = False
        button_controls[BTN_IS_CLICKED] = False
        button_grey[BTN_IS_CLICKED] = False
        button_red[BTN_IS_CLICKED] = False
        button_blue[BTN_IS_CLICKED] = False
    elif current_screen == "instructions":
        button_back_menu[BTN_IS_CLICKED] = False
    elif current_screen == "controls":
        button_back_menu[BTN_IS_CLICKED] = False
    elif current_screen == "play":
        button_pause[BTN_IS_CLICKED] = False
    elif current_screen == "pause":
        button_exit[BTN_IS_CLICKED] = False
        button_resume[BTN_IS_CLICKED] = False
    elif current_screen == "gameover":
        button_quit[BTN_IS_CLICKED] = False
        button_restart[BTN_IS_CLICKED] = False

def button_collision(x, y, button, modifiers):
    global current_screen, health, MAX_HEALTH, left_pressed, right_pressed, ship_color
    if current_screen == "menu":
        if (x > button_instructions[BTN_X] and x < button_instructions[BTN_X] + button_instructions[BTN_WIDTH] and
                y > button_instructions[BTN_Y] and y < button_instructions[BTN_Y] + button_instructions[BTN_HEIGHT]):
            button_instructions[BTN_IS_CLICKED] = True
            current_screen = "instructions"
        elif (x > button_play[BTN_X] and x < button_play[BTN_X] + button_play[BTN_WIDTH] and
                y > button_play[BTN_Y] and y < button_play[BTN_Y] + button_play[BTN_HEIGHT]):
            button_play[BTN_IS_CLICKED] = True
            current_screen = "play"
        elif (x > button_controls[BTN_X] and x < button_controls[BTN_X] + button_controls[BTN_WIDTH] and
                y > button_controls[BTN_Y] and y < button_controls[BTN_Y] + button_controls[BTN_HEIGHT]):
            button_controls[BTN_IS_CLICKED] = True
            current_screen = "controls"
        elif (x > button_grey[BTN_X] and x < button_grey[BTN_X] + button_grey[BTN_WIDTH] and
                y > button_grey[BTN_Y] and y < button_grey[BTN_Y] + button_grey[BTN_HEIGHT]):
            button_grey[BTN_IS_CLICKED] = True
            ship_color = button_grey[BTN_COLOR]
        elif (x > button_red[BTN_X] and x < button_red[BTN_X] + button_red[BTN_WIDTH] and
                y > button_red[BTN_Y] and y < button_red[BTN_Y] + button_red[BTN_HEIGHT]):
            button_red[BTN_IS_CLICKED] = True
            ship_color = button_red[BTN_COLOR]
        elif (x > button_blue[BTN_X] and x < button_blue[BTN_X] + button_blue[BTN_WIDTH] and
                y > button_blue[BTN_Y] and y < button_blue[BTN_Y] + button_blue[BTN_HEIGHT]):
            button_blue[BTN_IS_CLICKED] = True
            ship_color = button_blue[BTN_COLOR]

    elif current_screen == "instructions":
        if (x > button_back_menu[BTN_X] and x < button_back_menu[BTN_X] + button_back_menu[BTN_WIDTH] and
                y > button_back_menu[BTN_Y] and y < button_back_menu[BTN_Y] + button_back_menu[BTN_HEIGHT]):
            button_back_menu[BTN_IS_CLICKED] = True
            current_screen = "menu"

    elif current_screen == "controls":
        if (x > button_back_menu[BTN_X] and x < button_back_menu[BTN_X] + button_back_menu[BTN_WIDTH] and
                y > button_back_menu[BTN_Y] and y < button_back_menu[BTN_Y] + button_back_menu[BTN_HEIGHT]):
            button_back_menu[BTN_IS_CLICKED] = True
            current_screen = "menu"

    elif current_screen == "play":
        if (x > button_pause[BTN_X] and x < button_pause[BTN_X] + button_pause[BTN_WIDTH] and
                y > button_pause[BTN_Y] and y < button_pause[BTN_Y] + button_pause[BTN_HEIGHT]):
            button_pause[BTN_IS_CLICKED] = True
            left_pressed = False
            right_pressed = False
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

    elif current_screen == "gameover":
        if (x > button_quit[BTN_X] and x < button_quit[BTN_X] + button_quit[BTN_WIDTH] and
                y > button_quit[BTN_Y] and y < button_quit[BTN_Y] + button_quit[BTN_HEIGHT]):
            button_quit[BTN_IS_CLICKED] = True
            current_screen = "menu"
        if (x > button_restart[BTN_X] and x < button_restart[BTN_X] + button_restart[BTN_WIDTH] and
                y > button_restart[BTN_Y] and y < button_restart[BTN_Y] + button_restart[BTN_HEIGHT]):
            button_restart[BTN_IS_CLICKED] = True
            current_screen = "play"

def draw_menu():
    arcade.set_background_color(arcade.color.DARK_LAVA)
    arcade.draw_text("OPERATION INTERSTALLAR", WIDTH/2, HEIGHT/2 + 150,
                     arcade.color.WHITE, font_size=75, anchor_x="center")
    arcade.draw_xywh_rectangle_filled(100, 480, 1100, 20, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(100, 680, 1100, 20, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(100, 480, 20, 200, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(1180, 480, 20, 200, arcade.color.BLACK)
    arcade.draw_text("* WELCOME TO *", WIDTH/2, HEIGHT/2 + 250,
                     arcade.color.WHITE, font_size=40, anchor_x="center")
    arcade.draw_text("CUSTOMIZE YOUR SHIP", 200, 280,
                     arcade.color.WHITE, font_size=20, anchor_x="center")
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
    arcade.draw_text("INSTRUCTIONS", button_instructions[BTN_X] + 73,
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
    arcade.draw_text("PLAY", button_play[BTN_X] + 50, button_play[BTN_Y] + 15,
                        arcade.color.WHITE, font_size=20)

    if button_controls[BTN_IS_CLICKED]:
        color2 = button_controls[BTN_CLICKED_COLOR]
    else:
        color2 = button_controls[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_controls[BTN_X]-1,
                                      button_controls[BTN_Y]-2,
                                      button_controls[BTN_WIDTH]+3,
                                      button_controls[BTN_HEIGHT]+3,
                                      button_controls[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_controls[BTN_X],
                                      button_controls[BTN_Y],
                                      button_controls[BTN_WIDTH],
                                      button_controls[BTN_HEIGHT],
                                      color2)
    arcade.draw_text("CONTROLS", button_controls[BTN_X] + 95, button_controls[BTN_Y] + 15,
                        arcade.color.WHITE, font_size=20)

#Cutomization Buttons For Ship
    color2 = button_grey[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_grey[BTN_X]-1,
                                      button_grey[BTN_Y]-2,
                                      button_grey[BTN_WIDTH]+3,
                                      button_grey[BTN_HEIGHT]+3,
                                      button_grey[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_grey[BTN_X],
                                      button_grey[BTN_Y],
                                      button_grey[BTN_WIDTH],
                                      button_grey[BTN_HEIGHT],
                                      color2)

    color2 = button_red[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_red[BTN_X]-1,
                                      button_red[BTN_Y]-2,
                                      button_red[BTN_WIDTH]+3,
                                      button_red[BTN_HEIGHT]+3,
                                      button_red[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_red[BTN_X],
                                      button_red[BTN_Y],
                                      button_red[BTN_WIDTH],
                                      button_red[BTN_HEIGHT],
                                      color2)

    color2 = button_blue[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_blue[BTN_X]-1,
                                      button_blue[BTN_Y]-2,
                                      button_blue[BTN_WIDTH]+3,
                                      button_blue[BTN_HEIGHT]+3,
                                      button_blue[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_blue[BTN_X],
                                      button_blue[BTN_Y],
                                      button_blue[BTN_WIDTH],
                                      button_blue[BTN_HEIGHT],
                                      color2)

#Ship Display
    arcade.draw_circle_filled(300, 100, 50, ship_color)
    arcade.draw_circle_filled(300, 100+100, 25, ship_color)
    arcade.draw_circle_filled(300, 100+100, 18, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(300, 100, 100, 40, ship_color)
    arcade.draw_rectangle_filled(300, 100+50, 40, 100, ship_color)
    arcade.draw_rectangle_filled(300-30, 100+10, 20, 100, ship_color)
    arcade.draw_rectangle_filled(300+30, 100+10, 20, 100, ship_color)
    arcade.draw_rectangle_filled(300+55, 100-20, 30, 60, ship_color)
    arcade.draw_rectangle_filled(300-55, 100-20, 30, 60, ship_color)
    arcade.draw_rectangle_filled(300, 100+50, 15, 100, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(300, 100+40, 30, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(300, 100+40, 20, 70, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(300, 100+30, 50, 30, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(300, 90, 50, 50, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(300, 100-12, 120, 20, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(300-50, 100-12, 20, 30, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(300+50, 100-12, 20, 30, arcade.color.DARK_GRAY)

def draw_instructions():
    arcade.set_background_color(arcade.color.PURPLE)
    arcade.draw_text("INSTRUCTIONS", WIDTH / 2, HEIGHT - 200,
                arcade.color.WHITE, font_size=100, anchor_x="center")
    arcade.draw_text("You must collect the nova cores while dodging the asteroids.", WIDTH / 2, HEIGHT / 2+100,
                arcade.color.WHITE, font_size=30, anchor_x="center")
    arcade.draw_text("Small asteroids take away 1 life, medium asteroids take away 2 lives,", WIDTH / 2, HEIGHT / 2+60,
                arcade.color.WHITE, font_size=30, anchor_x="center")
    arcade.draw_text("and large asteroids take away all lives. You have only 3 lives. Good Luck", WIDTH / 2, HEIGHT / 2+20,
                arcade.color.WHITE, font_size=30, anchor_x="center")
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

def draw_controls():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("CONTROLS", WIDTH / 2, HEIGHT - 200,
                arcade.color.WHITE, font_size=100, anchor_x="center")
    if button_back_menu[BTN_IS_CLICKED]:
        color3 = button_back_menu[BTN_CLICKED_COLOR]
    else:
        color3 = button_back_menu[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button_back_menu[BTN_X]-1,
                                      button_back_menu[BTN_Y]-1,
                                      button_back_menu[BTN_WIDTH]+3,
                                      button_back_menu[BTN_HEIGHT]+3,
                                      arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(button_back_menu[BTN_X],
                                      button_back_menu[BTN_Y],
                                      button_back_menu[BTN_WIDTH],
                                      button_back_menu[BTN_HEIGHT],
                                      color3)
    arcade.draw_text("Go Back", button_back_menu[BTN_X] + 100,
                 button_back_menu[BTN_Y] + 15, arcade.color.WHITE, font_size=20)
    arcade.draw_xywh_rectangle_filled(448, 398, 85, 85, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(450, 400, 80, 80, arcade.color.ASH_GREY)
    arcade.draw_text("A", 472, 415, arcade.color.BLUE, font_size=50)
    arcade.draw_text("LEFT", 250, 417, arcade.color.BLUE, font_size=50)
    arcade.draw_xywh_rectangle_filled(768, 398, 85, 85, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(770, 400, 80, 80, arcade.color.ASH_GREY)
    arcade.draw_text("D", 792, 415, arcade.color.BLUE, font_size=50)
    arcade.draw_text("RIGHT", 925, 417, arcade.color.BLUE, font_size=50)

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
    arcade.draw_text(f"Lives: {health}", 30, 30,
                     arcade.color.ASH_GREY, font_size=40)
    arcade.draw_text(f"Score: {score}", 1000, 680,
                     arcade.color.ASH_GREY, font_size=40)
    
def draw_pause():
    arcade.draw_text("MENU", WIDTH / 2, HEIGHT - 200,
                     arcade.color.ASH_GREY, font_size=100, anchor_x="center")
    if button_exit[BTN_IS_CLICKED]:
        color3 = button_exit[BTN_CLICKED_COLOR]
    else:
        color3 = button_exit[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(WIDTH/2-257,
                                      HEIGHT/2-182,
                                      505,
                                      305,
                                      arcade.color.ASH_GREY)
    arcade.draw_xywh_rectangle_filled(WIDTH/2-255,
                                      HEIGHT/2-180,
                                      500,
                                      300,
                                      arcade.color.DARK_BYZANTIUM)
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

def update_play(delta_time):
    global left_pressed, right_pressed, ship_x_position, current_screen, ship, MAX_HEALTH, health, score
    if current_screen == "play":
        if left_pressed:
            ship[ship_x_position] -= movement
            ship_hitbox[HIT_BOX_X] -= movement
        elif right_pressed:
            ship[ship_x_position] += movement
            ship_hitbox[HIT_BOX_X] += movement
        if ship[ship_x_position] > WIDTH - 70:
            ship[ship_x_position] = WIDTH - 70
            ship_hitbox[HIT_BOX_X] = WIDTH - 70
        elif ship[ship_x_position] < 70:
            ship[ship_x_position] = 70
            ship_hitbox[HIT_BOX_X] = 70

# Large Asteroid
        for index in range(1):
            Large_ast_y[index] -=1
            if Large_ast_y[index] < -175:
                Large_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                Large_ast_x[index] = random.randrange(0, WIDTH)

            a = Large_ast_x[index] - ship_hitbox[HIT_BOX_X]
            b = Large_ast_y[index] - ship_hitbox[HIT_BOX_Y]
            dist = math.sqrt(a ** 2 + b ** 2)
            if dist < large_asteroid[2] + ship_hitbox[HIT_BOX_R]:
                Large_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                Large_ast_x[index] = random.randrange(0, WIDTH)
                health -= 3

# Medium Asteroid
        for index in range(3):
            Medium_ast_y[index] -= 3
            if Medium_ast_y[index] < -175:
                Medium_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                Medium_ast_x[index] = random.randrange(0, WIDTH)

            a = Medium_ast_x[index] - ship_hitbox[HIT_BOX_X]
            b = Medium_ast_y[index] - ship_hitbox[HIT_BOX_Y]
            dist = math.sqrt(a ** 2 + b ** 2)
            if dist < medium_asteroid[2] + ship_hitbox[HIT_BOX_R]:
                Medium_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                Medium_ast_x[index] = random.randrange(0, WIDTH)
                health -= 2

# Small Asteroid
        for index in range(5):
            Small_ast_y[index] -= 5
            if Small_ast_y[index] < -175:
                Small_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                Small_ast_x[index] = random.randrange(0, WIDTH)

            a = Small_ast_x[index] - ship_hitbox[HIT_BOX_X]
            b = Small_ast_y[index] - ship_hitbox[HIT_BOX_Y]
            dist = math.sqrt(a ** 2 + b ** 2)
            if dist < small_asteroid[2] + ship_hitbox[HIT_BOX_R]:
                Small_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                Small_ast_x[index] = random.randrange(0, WIDTH)
                health -= 1
#Cores
        for index in range(1):
            cores_y[index] -= 2
            if cores_y[index] < -175:
                cores_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                cores_x[index] = random.randrange(0, WIDTH)

            a = cores_x[index] - ship_hitbox[HIT_BOX_X]
            b = cores_y[index] - ship_hitbox[HIT_BOX_Y]
            dist = math.sqrt(a ** 2 + b ** 2)
            if dist < cores[2] + ship_hitbox[HIT_BOX_R]:
                cores_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
                cores_x[index] = random.randrange(0, WIDTH)
                score += 1

#Reset When User is in menu
    elif current_screen == "menu":
        for index in range(1):
            Large_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            Large_ast_x[index] = random.randrange(0, WIDTH)
        for index in range(3):
            Medium_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            Medium_ast_x[index] = random.randrange(0, WIDTH)
        for index in range(5):
            Small_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            Small_ast_x[index] = random.randrange(0, WIDTH)
        for index in range(1):
            cores_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            cores_x[index] = random.randrange(0, WIDTH)
        ship[ship_x_position] = WIDTH/2
        ship_hitbox[HIT_BOX_X] = WIDTH/2
        health = 3
        score = 0

def draw_gameover():
    arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
    arcade.draw_text("GAME OVER", WIDTH / 2, HEIGHT - 200,
                arcade.color.WHITE, font_size=100, anchor_x="center")
    arcade.draw_text("Your ship was destroyed", WIDTH / 2, HEIGHT / 2 + 100,
                arcade.color.WHITE, font_size=30, anchor_x="center")
    arcade.draw_xywh_rectangle_filled(button_quit[BTN_X]-1,
                                      button_quit[BTN_Y]-1,
                                      button_quit[BTN_WIDTH]+3,
                                      button_quit[BTN_HEIGHT]+3,
                                      button_quit[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_quit[BTN_X],
                                      button_quit[BTN_Y],
                                      button_quit[BTN_WIDTH],
                                      button_quit[BTN_HEIGHT],
                                      button_quit[BTN_COLOR])
    arcade.draw_text("Quit", button_quit[BTN_X] + 145,
                 button_quit[BTN_Y] + 15, arcade.color.WHITE, font_size=20, anchor_x="center")

    arcade.draw_xywh_rectangle_filled(button_restart[BTN_X]-1,
                                      button_restart[BTN_Y]-1,
                                      button_restart[BTN_WIDTH]+3,
                                      button_restart[BTN_HEIGHT]+3,
                                      button_restart[BTN_OUTLINE_COLOR])
    arcade.draw_xywh_rectangle_filled(button_restart[BTN_X],
                                      button_restart[BTN_Y],
                                      button_restart[BTN_WIDTH],
                                      button_restart[BTN_HEIGHT],
                                      button_restart[BTN_COLOR])
    arcade.draw_text("Try Again", button_restart[BTN_X] + 100,
                 button_restart[BTN_Y] + 15, arcade.color.WHITE, font_size=20)

def update_gameover(delta_time):
    global health, current_screen, left_pressed, right_pressed, score
    if health <= 0:
        current_screen = "gameover"
#Reset game when user is in screen "gameover"
        health = 3
        for index in range(1):
            Large_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            Large_ast_x[index] = random.randrange(0, WIDTH)
        for index in range(3):
            Medium_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            Medium_ast_x[index] = random.randrange(0, WIDTH)
        for index in range(5):
            Small_ast_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            Small_ast_x[index] = random.randrange(0, WIDTH)
        for index in range(1):
            cores_y[index] = random.randrange(HEIGHT + 150, HEIGHT + 300)
            cores_x[index] = random.randrange(0, WIDTH)
        left_pressed = False
        right_pressed = False
        ship[ship_x_position] = WIDTH/2
        ship_hitbox[HIT_BOX_X] = WIDTH/2
        score = 0

#Ship Functions
def draw_ship(x, y):
    arcade.draw_circle_filled(ship[ship_x_position]-52, ship[ship_y_position]-52, 25, arcade.color.YELLOW)
    arcade.draw_circle_filled(ship[ship_x_position]-55, ship[ship_y_position]-50, 20, arcade.color.ORANGE)
    arcade.draw_circle_filled(ship[ship_x_position]+52, ship[ship_y_position]-52, 25, arcade.color.YELLOW)
    arcade.draw_circle_filled(ship[ship_x_position]+55, ship[ship_y_position]-50, 20, arcade.color.ORANGE)
    arcade.draw_circle_filled(ship[ship_x_position], ship[ship_y_position], 50, ship_color)
    arcade.draw_circle_filled(ship[ship_x_position], ship[ship_y_position]+100, 25, ship_color)
    arcade.draw_circle_filled(ship[ship_x_position], ship[ship_y_position]+100, 18, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position], 100, 40, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]+50, 40, 100, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position]-30, ship[ship_y_position]+10, 20, 100, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position]+30, ship[ship_y_position]+10, 20, 100, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position]+55, ship[ship_y_position]-20, 30, 60, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position]-55, ship[ship_y_position]-20, 30, 60, ship_color)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]+50, 15, 100, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]+40, 30, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]+40, 20, 70, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]+30, 50, 30, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position], 50, 50, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(ship[ship_x_position], ship[ship_y_position]-12, 120, 20, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(ship[ship_x_position]-50, ship[ship_y_position]-12, 20, 30, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(ship[ship_x_position]+50, ship[ship_y_position]-12, 20, 30, arcade.color.DARK_GRAY)

def draw_ship_hitbox(x, y):
    arcade.draw_circle_outline(ship_hitbox[HIT_BOX_X], ship_hitbox[HIT_BOX_Y],
                                       ship_hitbox[HIT_BOX_R], ship_hitbox[HIT_BOX_CLR])

#Asteroid Functions
def draw_large_asteroid(x, y):
    arcade.draw_circle_filled(x, y, large_asteroid[2], arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x, y, 105, arcade.color.COCOA_BROWN)

def draw_medium_asteroid(x, y):
    arcade.draw_circle_filled(x, y, medium_asteroid[2], arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x, y, 65, arcade.color.COCOA_BROWN)

def draw_small_asteroid(x, y):
    arcade.draw_circle_filled(x, y, small_asteroid[2], arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x, y, 45, arcade.color.COCOA_BROWN)

def draw_cores(x, y):
    arcade.draw_circle_filled(x, y, cores[2]+2, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, cores[2], arcade.color.BABY_BLUE)
    arcade.draw_circle_filled(x, y, 20, arcade.color.ASH_GREY)
    arcade.draw_xywh_rectangle_filled(x-5, y-30, 10, 55, arcade.color.BABY_BLUE)

if __name__ == '__main__':
    setup()
