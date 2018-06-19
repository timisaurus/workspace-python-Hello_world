import random
import time

import pygame

pygame.init()

display_width = 640
display_height = 480

black = (0, 0, 0)
white = (255, 255, 255)
gray = (127, 127, 127)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
button_green = (0, 200, 0)
button_red = (200, 0, 0)

game_display = pygame.display.set_mode((display_width, display_height))  # display size
pygame.display.set_caption('sonic the headshot')  # window name
clock = pygame.time.Clock()

hedgehog_img = pygame.image.load('sonic_the_hedgehog.png')  # loads image into game
hedgehog_img = pygame.transform.scale(hedgehog_img, (100, 140))
hedgehog_width: int = 100

pickaxe_img = pygame.image.load('pickaxe.png')
pygame.display.set_icon(pickaxe_img)  # edits window icon


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: ' + str(count), True, black)  # (text printed+text printed, anti aliasing, color)
    game_display.blit(text, (0, 0))  # actually prints function + position


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])


def hedgehog(x, y):
    game_display.blit(hedgehog_img, (x, y))


def quit_game():
    pygame.quit()
    quit()


def text_object(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def massage_display(text, color):
    game_display.fill(black)
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_object(text, large_text, color)
    text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)
    pygame.display.update()
    game_loop()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'play':
                game_loop()
            elif action == 'quit':
                quit_game()
    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))

    small_text = pygame.font.Font('freesansbold.ttf', 30)
    text_surf, text_rect = text_object(str(msg), small_text, black)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(text_surf, text_rect)


def crash():
    game_exit = True
    massage_display('YOU DIED', red)
    game_exit = False


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():  # print (event) event is every input
            if event.type == pygame.QUIT:
                quit_game()

        game_display.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 40)
        text_surf, text_rect = text_object("Sonic the Squareshot", large_text, blue)
        text_rect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surf, text_rect)

        button('Go!', 100, 300, 100, 50, button_green, green, 'play')
        button('Quit', 440, 300, 100, 50, button_red, red, 'quit')

        pygame.display.update()
        clock.tick(10)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.71)

    dodged = 0
    thing_speed = 0

    x_change_left = 0
    x_change_right = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -640
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    movement_allowed = True
    game_exit = False

    while not game_exit:  # Gameloop (logic for game)

        try:
            x_change_left_speed = -3 - (thing_speed / 2)
            x_change_right_speed = 3 + (thing_speed / 2)
        except ValueError as speed_error:
            print(type(speed_error), speed_error)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change_left = x_change_left_speed
                if event.key == pygame.K_RIGHT:
                    x_change_right = x_change_right_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change_left = 0
                if event.key == pygame.K_RIGHT:
                    x_change_right = 0

        while x > display_width - hedgehog_width or x < 0:
            crash()
            movement_allowed = False
            x = (display_width * 0.5)
            y = (display_height * 0.7)
            movement_allowed = True

        if movement_allowed == True:
            x += x_change_left
            x += x_change_right

        game_display.fill(white)
        things_dodged(dodged)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.5
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            if (
                    thing_startx < x < thing_startx + thing_width or
                    thing_startx < x + hedgehog_width < thing_startx + thing_width
            ):
                crash()

        things(thing_startx, thing_starty, thing_width, thing_height, gray)
        thing_starty += thing_speed
        hedgehog(x, y)

        pygame.display.update()
        clock.tick(60)  # frames per second


game_intro()
game_loop()
pygame.quit()
quit()
