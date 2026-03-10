#imports
import random
import time
import json
import pygame

#initialization of pygame
pygame.init()
pygame.mixer.init()

#screen width and height constants
WIDTH = 600
HEIGHT = 900

def col(color):
    #custom color list in json format with html color names as keys
    colorspaceurl = "colorspace.json"
    #load the json file
    try:
        with open(colorspaceurl, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file. Check if the JSON is valid.")
    except KeyError as e:
        print(f"Error: Missing key in JSON Data: {e}")
    return data[color]

#syntax for direct access of colors data["Gray"]

#colors
black = tuple(col("Black"))
white = tuple(col("White"))
red = tuple(col("Red"))
green = tuple(col("Green"))
blue = tuple(col("Blue"))
yellow = tuple(col("Yellow"))
orange = tuple(col("Orange"))
purple = tuple(col("Purple"))
gray = tuple(col("Gray"))
darkgray = tuple(col("DarkGray"))
lightgray = tuple(col("LightGray"))
brown = tuple(col("Brown"))
burlywood = tuple(col("Burlywood"))
brickred = tuple(col("Firebrick"))
forestgreen = tuple(col("ForestGreen"))

#background color can be set from above colors
background = burlywood

#setting screen mode with width and height
screen = pygame.display.set_mode([WIDTH, HEIGHT])
#setting the title of the program window
pygame.display.set_caption('Yachtzed!')
#not sure exactly what this is doing, come back to it
timer = pygame.time.Clock()
#frames per second setting
fps = 60
#setting your standard fonts. I may add more of these so I'll give them different names
font_reg = pygame.font.Font('Open_Sans/static/OpenSans-Regular.ttf', 18)
font_title = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 96)
font_h1 = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 72)
font_h2 = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 48)
font_h3 = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 36)
font_h4 = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 24)
font_h5 = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 20)
font_h6 = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 16)
font_i = pygame.font.Font('Open_Sans/static/OpenSans-Italic.ttf', 18)
font_b = pygame.font.Font('Open_Sans/static/OpenSans-Bold.ttf', 18)
font_m = pygame.font.Font('Open_Sans/static/OpenSans-Medium.ttf', 18)
font_l = pygame.font.Font('Open_Sans/static/OpenSans-Light.ttf', 18)
font_c = pygame.font.Font('Open_Sans/static/OpenSans_Condensed-Regular.ttf', 18)

numbers = [1,2,3,4,5]

#creating a Dice class so we can call multiple of them with different pip counts. This version is for a standard 6 sided die.
class Dice:
    def __init__(self, x_pos, y_pos, num_pip, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num_pip
        self.key = key
        self.die = ''

    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number % 2 == 1:
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number > 1:
            pygame.draw.circle(screen, black, (self.x_pos + 25, self.y_pos + 25), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 75, self.y_pos + 75), 10)
        if self.number > 3:
            pygame.draw.circle(screen, black, (self.x_pos + 25, self.y_pos + 75), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 75, self.y_pos + 25), 10)
        if self.number == 6:
            pygame.draw.circle(screen, black, (self.x_pos + 25, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 75, self.y_pos + 50), 10)

def draw_stuff():
    print("useless so far")


#creating a button class so I don't need to do this over and over
class Button:
    def __init__(self, x_pos, y_pos, width, height, color, padding, text, font, textcolor, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color #tuple(col(color))
        self.padding = padding
        self.text = text
        self.font = font
        self.textcolor = textcolor #tuple(col(textcolor))
        #self.action = action  // should this become necessary later on
        self.key = key
        self.pressed = False
        self.outline = ''
        self.button = ''
        self.centerx = (self.width // 2) + x_pos
        self.centery = (self.height // 2) + y_pos

    #draws the button
    def draw(self):
        if self.pressed:
            color = blue
            textcolor = white
        else:
            color = self.color
            textcolor = self.textcolor
        #Draws the button itself. Might want to add some shading or an outline. If I could get an on mouseover state and an on click state too, that'd be amazing. Work for later.
        self.button = pygame.draw.rect(screen, color, [self.x_pos, self.y_pos, self.width, self.height], 0, 5)
        #attempting to make an outline
        self.outline = pygame.draw.rect(screen, textcolor, [self.x_pos, self.y_pos, self.width, self.height], 3, 5)
        #Difining the paramerters of the text on the button. Text, Anti-Aliasing, and Color
        text_surface = self.font.render(self.text, True, textcolor)
        #Getting the box the text exists in
        text_rect = text_surface.get_rect()
        #defining the center point of the text, and where to place it
        text_rect.center = (self.centerx, self.centery)
        screen.blit(text_surface, text_rect)

#Choices / Options. Those spaces where the scores and numbers are tallied.
class Choice:
    def __init__(self, x_pos, y_pos, width, height, text, select, possible, done):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.select = select
        self.possible = possible
        self.done = done
        #self.centerx = (self.width // 2) + x_pos
        self.centery = (self.height // 2) + y_pos
    
    def draw(self):
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos),(self.x_pos + self.width, self.y_pos), 2)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + self.height),(self.x_pos + self.width, self.y_pos + self.height), 2)
        if not self.done:
            if self.possible:
                my_text = (self.text, True, forestgreen)
            elif not self.possible:
                my_text = (self.text, True, brickred)
        else:
            my_text = (self.text, True, darkgray)
        my_text = font_m.render(self.text, True, black)
        if self.text == "Grand Total":
            my_text = font_b.render(self.text, True, black)
        text_rect = my_text.get_rect()
        text_rect.centery = self.centery
        text_rect.x = 10
        screen.blit(my_text, text_rect)

def main():
    
    running = True
    roll = False
    #local rolls variable
    rolls_remaining = 3
    #Loading dice sounds

    #Shake effect intiialization for dice or other objects
    shakex = 0
    shakey = 0

    #setting the roll button parameters
    roll_text = f"Rolls Remaining: {rolls_remaining}"
    roll_button = Button(5, 165, 200, 50, gray, 5, roll_text, font_m, black, 0)

    while running:
        timer.tick(fps)
        screen.fill(background)

        if pygame.mixer.get_busy():
            for x in shakex:
                shakex[x] = random.randint(-3,3)
            for y in shakey:
                shakey[y] = random.randint(-3,3)
            for number in range(len(numbers)):
                numbers[number] = random.randint(1,6)
        else:
            shakex = [0,0,0,0,0]
            shakey = [0,0,0,0,0]

        #setting the dice positions, list key, and object key
        die1 = Dice(10 + shakex[0], 50 + shakey[0], numbers[0], 0)
        die2 = Dice(130 + shakex[1], 50 + shakey[1], numbers[1], 1)
        die3 = Dice(250 + shakex[2], 50 + shakey[2], numbers[2], 2)
        die4 = Dice(370 + shakex[3], 50 + shakey[3], numbers[3], 3)
        die5 = Dice(490 + shakex[4], 50 + shakey[4], numbers[4], 4)
        #drawing the dice
        die1.draw()
        die2.draw()
        die3.draw()
        die4.draw()
        die5.draw()
    
        #Text for the roll button
        roll_button.text = f"Rolls Remaining: {rolls_remaining}"

        if roll_button.button and roll_button.button.collidepoint(mouse_pos):
            roll_button.color = lightgray  # hover color
            roll_button.textcolor = darkgray
        else:
            roll_button.color = gray      # default color
            roll_button.textcolor = black
        #drawing the roll button
        roll_button.draw()

        accept_text = f"Accept Turn"
        accept_button = Button(240, 165, 200, 50, gray, 5, accept_text, font_m, black, 0)
        accept_button.draw()

        #draw_stuff()

        ones = Choice(0, 240, 225, 30, '1s', True, True, False )
        twos = Choice(0, 270, 225, 30, '2s', True, True, False )
        threes = Choice(0, 300, 225, 30, '3s', True, True, False )
        fours = Choice(0, 330, 225, 30, '4s', True, True, False )
        fives = Choice(0, 360, 225, 30, '5s', True, True, False )
        sixes = Choice(0, 390, 225, 30, '6s', True, True, False )
        uppersubt = Choice(0, 420, 225, 30, 'Upper Score', False, False, True )
        upperbonus = Choice(0, 450, 225, 30, 'Bonus if 63+', False, False, True )
        uppertotal = Choice(0, 480, 225, 30, 'Upper Total', False, False, True )

        two_pair = Choice(0, 520, 225, 30, 'Two Pair', True, True, False )
        three_kind = Choice(0, 550, 225, 30, 'Three of a Kind', True, True, False )
        four_kind = Choice(0, 580, 225, 30, 'Four of a Kind', True, True, False )
        yachtzed = Choice(0, 770, 225, 30, 'YACHTZED!', True, True, False )
        full_house = Choice(0, 610, 225, 30, 'Full House', True, True, False )
        sm_straight = Choice(0, 640, 225, 30, 'Small Straight', True, True, False )
        lg_straight = Choice(0, 670, 225, 30, 'Large Straight', True, True, False )
        chance = Choice(0, 700, 225, 30, 'Chance', True, True, False )
        lowersubt = Choice(0, 740, 225, 30, 'Lower Subtotal', True, True, False )
        bonus1 = Choice(0, 800, 225, 30, 'Bonus Yachtzed', True, True, False )
        bonus2 = Choice(0, 830, 225, 30, 'Bonus Yachtzed', True, True, False )
        grandtotal = Choice(0, 870, 225, 30, 'Grand Total', True, True, False )

        ones.draw()
        twos.draw()
        threes.draw()
        fours.draw()
        fives.draw()
        sixes.draw()
        uppersubt.draw()
        upperbonus.draw()
        uppertotal.draw()

        two_pair.draw()
        three_kind.draw()
        four_kind.draw()
        full_house.draw()
        sm_straight.draw()
        lg_straight.draw()
        yachtzed.draw()
        chance.draw()

        lowersubt.draw()

        bonus1.draw()
        bonus2.draw()

        grandtotal.draw()
        
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if roll_button.button.collidepoint(event.pos):
                    roll_button.pressed = True
                    if rolls_remaining > 0:
                        roll = True
            if event.type == pygame.MOUSEBUTTONUP:
                if roll_button.pressed == True:
                    roll_button.pressed = False
        if roll:
            dice_sounds = random.choice(["FX/MORESNDS/8BIT/CASINO/BACKROLL.WAV","FX/MORESNDS/8BIT/CASINO/SHAKE1.WAV", "FX/MORESNDS/8BIT/CASINO/SHAKE2.WAV", "FX/MORESNDS/8BIT/CASINO/SHAKE3.WAV"])
            for number in range(len(numbers)):
                numbers[number] = random.randint(1,6)
            rolls_remaining -= 1
            pygame.mixer.Sound(dice_sounds).play()
            roll = False
            

        pygame.display.flip()

    pygame.quit()

main()