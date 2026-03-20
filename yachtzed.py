#imports
import random
import time
import json
import pygame

#initialization of pygame
pygame.init()
pygame.mixer.init()

game_icon = pygame.image.load('dieicon.png')
pygame.display.set_icon(game_icon)

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
        print(f"Error: The file '{colorspaceurl}' was not found.")
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

numbers = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]


#rolls_left = 3 #hiding this for now, looks like since I have a better option, I should use that

dice_selected = [False, False, False, False, False]

selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
clicked = -1


#creating a Dice class so we can call multiple of them with different pip counts. This version is for a standard 6 sided die.
class Dice:
    def __init__(self, x_pos, y_pos, num_pip, key):
        global dice_selected
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num_pip
        self.key = key
        self.selected = dice_selected[key]
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

        if self.selected:
            pygame.draw.rect(screen, forestgreen, [self.x_pos, self.y_pos, 100, 100], 5, 5)
        
    def check_click(self, coords):
        if self.die.collidepoint(coords):
            if dice_selected[self.key]:
                dice_selected[self.key] = False
            elif not dice_selected[self.key]:
                dice_selected[self.key] = True

def draw_stuff():
    #global rolls_left #just in case I want to separate the rolls left from the roll button
    #global rolls_remaining #my own spin on it, see if this works, looks like it's unnecessary
    #roll_text = font_b.render('Click to Roll', True, white)    this is handled elsewhere in my version
    #screen.blit(roll_text, (85, 167))                          this is handled more cleanly elsewhere
    #accept_text = font_m.render('Accept Turn', True, white)    this is handled elsewhere
    #screen.blit(accept_text, (375, 167))                       again, I handled this better elsewhere
    #rolls_text = font_b.render(f'Rolls left this turn: {rolls_left}', True, white) #hide this for now
    rolls_text = font_b.render(f'Rolls left this turn: {rolls_remaining}', True, white)
    screen.blit(rolls_text, (10, 10))
    pygame.draw.rect(screen, white, [0, 240, 225, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 240), (WIDTH, 240), 3)
    pygame.draw.line(screen, black, (155, 240), (155, HEIGHT), 3)
    pygame.draw.line(screen, black, (225, 240), (225, HEIGHT), 3)

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
                possiblecolor = forestgreen
            elif not self.possible:
                possiblecolor = brickred
        else:
            possiblecolor = darkgray
        my_text = font_m.render(self.text, True, possiblecolor)
        if self.text == "Grand Total":
            my_text = font_b.render(self.text, True, possiblecolor)
        text_rect = my_text.get_rect()
        text_rect.centery = self.centery
        text_rect.x = 10
        screen.blit(my_text, text_rect)

'''    def check_click(self, coords):
        if self.die.collidepoint(coords):
            if dice_selected[self.key]:
                dice_selected[self.key] = False
            elif not dice_selected[self.key]:
                dice_selected[self.key] = True'''

def check_possible(possible_list, numbers_list):
    max_count = 0
    pairodice = 0
    #needed for alternate way to check for full house
    #has_three = False
    #something is wrong with the logic. Try running it. Send it to claude.
    possible_list[0] = True #ones
    possible_list[1] = True #twos
    possible_list[2] = True #threes
    possible_list[3] = True #fours
    possible_list[4] = True #fives
    possible_list[5] = True #sixes
    possible_list[13] = True #chance

    for index in range(1,7):
        count = numbers_list.count(index)
        if count > max_count:
            max_count = count
        if count == 2:
            pairodice += 1
        #if count == 3:
            #has_three = True
    
    #Checks for 2 of more pairs of different dice
    possible_list[6] = pairodice >= 2
    #this is an alternate way to check for a full house
    #possible_list[10] = has_three and pairodice >= 1

    if max_count >= 3:
        possible_list[7] = True
        if max_count >= 4:
            possible_list[8] = True
            if max_count == 5:
                possible_list[9] = True

    if max_count < 3:
        possible_list[7] = False
        possible_list[8] = False
        possible_list[9] = False
        possible_list[10] = False

    if max_count == 3:
        possible_list[8] = False
        possible_list[9] = False
        checker = False
        for index in range(len(numbers_list)):
            if numbers_list.count(numbers_list[index]) == 2:
                possible_list[10] = True
                checker = True
        if not checker:
            possible_list[10] = False
    
    if max_count == 4:
        possible_list[9] = False

    lowest = 10
    highest = 0
    for index in range(len(numbers_list)):
        if numbers_list[index] < lowest:
            lowest = numbers_list[index]
        if numbers_list[index] > highest:
            highest = numbers_list[index]
        
    if (lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest + 3 in numbers_list) and (lowest + 4 in numbers_list):
        possible_list[12] = True
    else:
        possible_list[12] = False

    if ((lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest + 3 in numbers_list)) or ((highest - 1 in numbers_list) and (highest - 2 in numbers_list) and (highest-3 in numbers_list)):
        possible_list[11] = True
    else:
        possible_list[11] = False

    return possible_list

def make_choice(clicked_num, selected, done_list):
    for index in range(len(selected)):
        selected[index] = False
    if not done[clicked_num]:
        selected[clicked_num] = True #where I've left off 3/20/2026
    return selected

def main():
    
    running = True
    roll = False
    #globalize the variable
    global rolls_remaining
    #local rolls variable
    rolls_remaining = 10 #3
    #Loading dice sounds
    #need to load possible as a global variable before it's used or redefined
    global possible
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
            
                for x in range(len(shakex)):
                    if not dice_selected[x]:
                        shakex[x] = random.randint(-3,3)
                for y in range(len(shakey)):
                    if not dice_selected[y]:
                        shakey[y] = random.randint(-3,3)
                for number in range(len(numbers)):
                    if not dice_selected[number]:
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

        draw_stuff()

        ones = Choice(0, 240, 225, 30, '1s', selected_choice[0], possible[0], done[0] )
        twos = Choice(0, 270, 225, 30, '2s', selected_choice[1], possible[1], done[1] )
        threes = Choice(0, 300, 225, 30, '3s', selected_choice[2], possible[2], done[2] )
        fours = Choice(0, 330, 225, 30, '4s', selected_choice[3], possible[3], done[3] )
        fives = Choice(0, 360, 225, 30, '5s', selected_choice[4], possible[4], done[4] )
        sixes = Choice(0, 390, 225, 30, '6s', selected_choice[5], possible[5], done[5] )
        uppersubt = Choice(0, 420, 225, 30, 'Upper Score', False, False, False )
        upperbonus = Choice(0, 450, 225, 30, 'Bonus if 63+', False, False, True )
        uppertotal = Choice(0, 480, 225, 30, 'Upper Total', False, False, True )

        two_pair = Choice(0, 520, 225, 30, 'Two Pair', selected_choice[6], possible[6], done[6] )
        three_kind = Choice(0, 550, 225, 30, 'Three of a Kind', selected_choice[7], possible[7], done[7] )
        four_kind = Choice(0, 580, 225, 30, 'Four of a Kind', selected_choice[8], possible[8], done[8] )
        yachtzed = Choice(0, 740, 225, 30, 'YACHTZED!', selected_choice[9], possible[9], done[9] )
        full_house = Choice(0, 610, 225, 30, 'Full House', selected_choice[10], possible[10], done[10])
        sm_straight = Choice(0, 640, 225, 30, 'Small Straight', selected_choice[11], possible[11], done[11] )
        lg_straight = Choice(0, 670, 225, 30, 'Large Straight', selected_choice[12], possible[12], done[12] )
        chance = Choice(0, 700, 225, 30, 'Chance', selected_choice[13], possible[13], done[13] )
        lowersubt = Choice(0, 770, 225, 30, 'Lower Subtotal', False, False, False )
        bonus1 = Choice(0, 800, 225, 30, 'Bonus Yachtzed', False, False, False )
        bonus2 = Choice(0, 830, 225, 30, 'Bonus Yachtzed', False, False, False )
        grandtotal = Choice(0, 870, 225, 30, 'Grand Total', False, False, False )

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                die1.check_click(event.pos)
                die2.check_click(event.pos)
                die3.check_click(event.pos)
                die4.check_click(event.pos)
                die5.check_click(event.pos)
                if 0 <= event.pos[0] <= 155:
                    if 240 <= event.pos[1] <= 420 or 520 <= event.pos[1] <= 730 or 740 <= event.pos[1] <= 770:
                        if 240 <= event.pos[1] <= 270:
                            clicked = 0
                        if 270 <= event.pos[1] <= 300:
                            clicked = 1
                        if 300 <= event.pos[1] <= 330:
                            clicked = 2
                        if 330 <= event.pos[1] <= 360:
                            clicked = 3
                        if 360 <= event.pos[1] <= 390:
                            clicked = 4
                        if 390 <= event.pos[1] <= 420:
                            clicked = 5

                        if 520 <= event.pos[1] <= 550:
                            clicked = 6
                        if 550 <= event.pos[1] <= 580:
                            clicked = 7
                        if 580 <= event.pos[1] <= 610:
                            clicked = 8
                        if 610 <= event.pos[1] <= 640:
                            clicked = 10
                        if 640 <= event.pos[1] <= 670:
                            clicked = 11
                        if 670 <= event.pos[1] <= 700:
                            clicked = 12
                        if 700 <= event.pos[1] <= 730:
                            clicked = 13
                        if 740 <= event.pos[1] <= 770:
                            clicked = 9
                        selected_choice = make_choice[clicked, selected_choice, done]

                if roll_button.button.collidepoint(event.pos):
                    roll_button.pressed = True
                    if rolls_remaining > 0:
                        roll = True
            if event.type == pygame.MOUSEBUTTONUP:
                if roll_button.pressed == True:
                    roll_button.pressed = False
        if roll:
            dice_sounds = random.choice(["FX/MORESNDS/8BIT/CASINO/BACKROLL.WAV","FX/MORESNDS/8BIT/CASINO/SHAKE1.WAV", "FX/MORESNDS/8BIT/CASINO/SHAKE2.WAV", "FX/MORESNDS/8BIT/CASINO/SHAKE3.WAV"])
            #for number in range(len(numbers)):
                #numbers[number] = random.randint(1,6)
            #rolls_left -= 1
            rolls_remaining -= 1
            pygame.mixer.Sound(dice_sounds).play()
            roll = False
        
        possible = check_possible(possible, numbers)

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

        pygame.display.flip()

    pygame.quit()

main()