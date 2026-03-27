#imports
import random
import json
import pygame

#initialization of pygame
pygame.init()
pygame.mixer.init()

game_icon = pygame.image.load('IMAGES/dieicon.ico')

pygame.display.set_icon(game_icon)

#screen width and height constants
WIDTH = 600
HEIGHT = 540

def col(color):
    #custom color list in json format with html color names as keys
    colorspaceurl = "JSON/colorspace.json"
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
gold = tuple(col("Gold"))

#background color can be set from above colors
background = burlywood

#setting screen mode with width and height
screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen_center = (WIDTH // 2, HEIGHT // 2)
#setting the title of the program window
pygame.display.set_caption('Yachtzed!')
#not sure exactly what this is doing, come back to it
timer = pygame.time.Clock()
#frames per second setting
fps = 60
#setting your standard fonts. I may add more of these so I'll give them different names
bold = 'FONTS/OpenSans-Bold.ttf'
font_reg = pygame.font.Font('FONTS/OpenSans-Regular.ttf', 18)
font_title = pygame.font.Font(bold, 96)
font_h1 = pygame.font.Font(bold, 72)
font_h2 = pygame.font.Font(bold, 48)
font_h3 = pygame.font.Font(bold, 36)
font_h4 = pygame.font.Font(bold, 24)
font_h5 = pygame.font.Font(bold, 20)
font_h6 = pygame.font.Font(bold, 16)
font_i = pygame.font.Font('FONTS/OpenSans-Italic.ttf', 18)
font_b = pygame.font.Font(bold, 18)
font_m = pygame.font.Font('FONTS/OpenSans-Medium.ttf', 18)
font_l = pygame.font.Font('FONTS/OpenSans-Light.ttf', 18)
font_c = pygame.font.Font('FONTS/OpenSans_Condensed-Regular.ttf', 18)

#intiial numbers list. Might want to make them all blank
#numbers = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
numbers = [0,0,0,0,0]

#rolls_left = 3 #hiding this for now, looks like since I have a better option, I should use that

dice_selected = [False, False, False, False, False]

selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
totals = [0,0,0,0,0,0]
clicked = -1 #this might need to be global
current_score = 0
something_selected = False
game_over = False
turn_counter = 0
global reset_button

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
    rolls_text = font_reg.render(f'Rolls left this turn:', True, darkgray)
    screen.blit(rolls_text, (10, 10))
    rolls_rem_text = font_b.render(f'{rolls_remaining}', True, red)
    screen.blit(rolls_rem_text, (170, 10))
    inst_text = font_i.render(f'Click Dice to Keep or Release, Accept Turn to Score', True, white)
    screen.blit(inst_text, (190, 10))
    pygame.draw.rect(screen, white, [0, 240, WIDTH, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 240), (WIDTH, 240), 3)
    pygame.draw.line(screen, black, (0, 240), (0, HEIGHT), 3)
    pygame.draw.line(screen, black, ((WIDTH//2)-50, 240), ((WIDTH//2)-50, HEIGHT), 3)
    pygame.draw.line(screen, black, (WIDTH//2, 240), (WIDTH//2, HEIGHT), 3)
    pygame.draw.line(screen, black, (WIDTH-50, 240), (WIDTH-50, HEIGHT), 3)
    

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
            color = forestgreen
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
    def __init__(self, x_pos, y_pos, width, height, text, select, possible, done, score):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.select = select
        self.possible = possible
        self.done = done
        self.score = score
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
        
        if self.select:
            pygame.draw.rect(screen, gold, [self.x_pos+2, self.y_pos+2, (WIDTH//2)-53, 28])

        my_text = font_m.render(self.text, True, possiblecolor)
        if self.text == "Grand Total":
            my_text = font_b.render(self.text, True, possiblecolor)
        text_rect = my_text.get_rect()
        text_rect.centery = self.centery
        text_rect.x = self.x_pos + 10
        screen.blit(my_text, text_rect)

        score_text = font_m.render(str(self.score), True, possiblecolor)
        text_rect = score_text.get_rect()
        text_rect.centery = self.centery
        text_rect.x = self.x_pos + 260
        screen.blit(score_text, text_rect)

    def check_click(self, coords):
        if self.die.collidepoint(coords):
            if dice_selected[self.key]:
                dice_selected[self.key] = False
            elif not dice_selected[self.key]:
                dice_selected[self.key] = True

def check_scores(choice_list, numbers_list, possible_list, current_score):
    active = 0
    for index in range(len(choice_list)):
        if choice_list[index]:
            active = index
    if active == 0:
        current_score = numbers_list.count(1) * 1
    elif active == 1:
        current_score = numbers_list.count(2) * 2
    elif active == 2:
        current_score = numbers_list.count(3) * 3
    elif active == 3:
        current_score = numbers_list.count(4) * 4
    elif active == 4:
        current_score = numbers_list.count(5) * 5
    elif active == 5:
        current_score = numbers_list.count(6) * 6
    elif active == 6 or active == 7 or active == 8 or active == 13:
        if possible_list[active]:
            current_score = sum(numbers_list)
        else:
            current_score = 0
    elif active == 9:
        if possible_list[active]:
            current_score = 50
        else:
            current_score = 0
    elif active == 10:
        if possible_list[active]:
            current_score = 25
        else:
            current_score = 0
    elif active == 11:
        if possible_list[active]:
            current_score = 30
        else:
            current_score = 0
    elif active == 12:
        if possible_list[active]:
            current_score = 40
        else:
            current_score = 0  
    return current_score

def check_totals(totals_list, score_list, bonus):
    totals_list[0] = score_list[0] + score_list[1] + score_list[2] + score_list[3] + score_list[4] + score_list[5] + score_list[13]
    if totals_list[0] >= 80:
        totals_list[1] = 40
    else:
        totals_list[1] = 0
    totals_list[2] = totals_list[0] + totals_list[1]
    if bonus:
        totals_list[4] = 100
        bonus = False
    totals_list[3] = score_list[6] + score_list[7] + score_list[8] + score_list[9] + score_list[10] + score_list[11] + score_list[12] + totals_list[4]
    totals_list[5] = totals_list[2] + totals_list[3]
    return totals_list, bonus

def check_possible(possible_list, numbers_list):
    max_count = 0
    pairodice = 0
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
    
    possible_list[6] = pairodice >= 2

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
    if not done_list[clicked_num]:
        selected[clicked_num] = True #where I've left off 3/20/2026
    return selected

def draw_outlined_text(screen, text, font, text_color, outline_color, x, y, outline_thickness=3):
    # Render the outline text multiple times
    outline_surface = font.render(text, True, outline_color)
    
    # Blit the outline surface in different directions
    for dx in range(-outline_thickness, outline_thickness + 1):
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:
                screen.blit(outline_surface, (x + dx, y + dy))
                
    # Render the main text on top
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x, y))

def restart_button():
    global possible
    global selected_choice
    global done
    global score
    global totals
    global something_selected
    global numbers
    global game_over
    global turn_counter
    global rolls_remaining
    global clicked
    global current_score
    global dice_selected
    numbers = [0, -8, -10, -12, -8]
    dice_selected = [False, False, False, False, False]
    selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    possible = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    done = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    totals = [0,0,0,0,0,0]
    clicked = -1
    current_score = 0
    something_selected = False
    game_over = False
    turn_counter = 0
    rolls_remaining = 3

def main():
    global clicked #why not just make the original global?
    running = True
    roll = False
    #globalize the variable
    global rolls_remaining
    #local rolls variable
    rolls_remaining = 3 #3
    #Loading dice sounds
    #need to load possible as a global variable before it's used or redefined
    global possible
    global selected_choice
    global done
    global score
    global totals
    global something_selected
    global numbers
    global game_over
    global turn_counter
    bonus_time = False
    #Shake effect intialization for dice or other objects
    shakex = [0,0,0,0,0] #are these supposed to be lists, not integers? They were working all the same.
    shakey = [0,0,0,0,0]

    #setting the roll button parameters
    roll_text = f"Roll Dice"
    roll_button = Button(10, 165, 200, 50, gray, 5, roll_text, font_m, black, 0)

    #setting accept button parameters
    accept_text = f"Accept Turn"
    accept_button = Button(220, 165, 200, 50, gray, 5, accept_text, font_m, black, 0)

    reset_text = f"RESET"
    reset_button = Button(430, 165, 160, 50, gray, 5, reset_text, font_b, black, 0)

    while running:
        
        timer.tick(fps)
        screen.fill(background)
        
        #shake animation paired to sound mixer. Need a way to have this run only while
        #a specific sound is playing
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

        if True in selected_choice:
            something_selected = True

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
        roll_button.text = f"Roll Dice"

        if roll_button.button and roll_button.button.collidepoint(mouse_pos):
            roll_button.color = lightgray  # hover color
            roll_button.textcolor = black
        else:
            roll_button.color = gray      # default color
            roll_button.textcolor = black
        #drawing the roll button
        roll_button.draw()

        #Text for the roll button
        accept_button.text = f"Accept Turn"

        if accept_button.button and accept_button.button.collidepoint(mouse_pos):
            accept_button.color = lightgray  # hover color
            accept_button.textcolor = black
        else:
            accept_button.color = gray      # default color
            accept_button.textcolor = black
        accept_button.draw()

        #text for the reset button
        if reset_button.button and reset_button.button.collidepoint(mouse_pos) and not game_over:
            reset_button.text = f"RESET"
            reset_button.color = red  # hover color
            reset_button.textcolor = white
        elif reset_button.button and reset_button.button.collidepoint(mouse_pos) and game_over:
            reset_button.text = f"RESTART GAME"
            reset_button.color = black  # hover color
            reset_button.textcolor = gold
        elif game_over:
            reset_button.text = f"RESTART GAME"
            reset_button.color = forestgreen  #default color
            reset_button.textcolor = white
        else:
            reset_button.color = gray      # default color
            reset_button.textcolor = black
        reset_button.draw()

        draw_stuff()

        ones = Choice(0, 240, WIDTH//2, 30, '1s', selected_choice[0], possible[0], done[0], score[0])
        twos = Choice(0, 270, WIDTH//2, 30, '2s', selected_choice[1], possible[1], done[1], score[1])
        threes = Choice(0, 300, WIDTH//2, 30, '3s', selected_choice[2], possible[2], done[2], score[2])
        fours = Choice(0, 330, WIDTH//2, 30, '4s', selected_choice[3], possible[3], done[3], score[3])
        fives = Choice(0, 360, WIDTH//2, 30, '5s', selected_choice[4], possible[4], done[4], score[4])
        sixes = Choice(0, 390, WIDTH//2, 30, '6s', selected_choice[5], possible[5], done[5], score[5])
        chance = Choice(0, 420, WIDTH//2, 30, 'Chance', selected_choice[13], possible[13], done[13], score[13])

        uppersubt = Choice(0, 450, WIDTH//2, 30, 'Upper Subtotal', False, False, True, totals[0] )
        upperbonus = Choice(0, 480, WIDTH//2, 30, 'Bonus if 80+', False, False, True, totals[1] )
        uppertotal = Choice(0, 510, WIDTH//2, 30, 'Upper Total', False, False, True, totals[2] )

        two_pair = Choice(WIDTH//2, 240, WIDTH, 30, 'Two Pair', selected_choice[6], possible[6], done[6], score[6])
        three_kind = Choice(WIDTH//2, 270, WIDTH, 30, 'Three of a Kind', selected_choice[7], possible[7], done[7], score[7])
        four_kind = Choice(WIDTH//2, 300, WIDTH, 30, 'Four of a Kind', selected_choice[8], possible[8], done[8], score[8])
        yachtzed = Choice(WIDTH//2, 420, WIDTH, 30, 'YACHTZED!', selected_choice[9], possible[9], done[9], score[9])
        full_house = Choice(WIDTH//2, 330, WIDTH, 30, 'Full House', selected_choice[10], possible[10], done[10], score[10])
        sm_straight = Choice(WIDTH//2, 360, WIDTH, 30, 'Small Straight', selected_choice[11], possible[11], done[11], score[11])
        lg_straight = Choice(WIDTH//2, 390, WIDTH, 30, 'Large Straight', selected_choice[12], possible[12], done[12], score[12])
        
        lowersubt = Choice(WIDTH//2, 450, WIDTH, 30, 'Lower Subtotal', False, False, True, totals[3] )
        bonus1 = Choice(WIDTH//2, 480, WIDTH, 30, 'Bonus Yachtzed', False, False, True, totals[4] )
        grandtotal = Choice(WIDTH//2, 510, WIDTH, 30, 'Grand Total', False, False, False, totals[5] )

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
                if 0 <= event.pos[0] <= WIDTH//2:
                    if 240 <= event.pos[1] <= 450:
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
                        if 420 <= event.pos[1] <= 450:
                            clicked = 13
                        
                        selected_choice = make_choice(clicked, selected_choice, done)

                if WIDTH//2 < event.pos[0] <= WIDTH:
                    if 240 <= event.pos[1] <= 450:
                        if 240 <= event.pos[1] <= 270:
                            clicked = 6
                        if 270 <= event.pos[1] <= 300:
                            clicked = 7
                        if 300 <= event.pos[1] <= 330:
                            clicked = 8
                        if 330 <= event.pos[1] <= 360:
                            clicked = 10
                        if 360 <= event.pos[1] <= 390:
                            clicked = 11
                        if 390 <= event.pos[1] <= 420:
                            clicked = 12
                        if 420 <= event.pos[1] <= 450:
                            clicked = 9

                        selected_choice = make_choice(clicked, selected_choice, done)

                if roll_button.button.collidepoint(event.pos):
                    roll_button.pressed = True
                    if rolls_remaining > 0:
                        roll = True
                if accept_button.button.collidepoint(event.pos) and something_selected and rolls_remaining < 3:
                    accept_button.pressed = True
                    if score[11] == 50 and done[11] and possible[11]:
                        bonus_time = True
                    for i in range(len(selected_choice)):
                        if selected_choice[i]:
                            done[i] = True
                            score[i] = current_score
                            selected_choice[i] = False
                    for i in range(len(dice_selected)):
                        dice_selected[i] = False
                    numbers = [0, -8, -10, -12, -8]
                    something_selected = False
                    rolls_remaining = 3
                    turn_counter += 1
                if game_over == True:
                    reset_button.text = f"RESTART GAME"
                if reset_button.button.collidepoint(event.pos):
                    reset_button.pressed = True
                    restart_button()


            if event.type == pygame.MOUSEBUTTONUP:
                if roll_button.pressed or accept_button.pressed or reset_button.pressed:
                    roll_button.pressed = False
                    accept_button.pressed = False
                    reset_button.pressed = False
        if roll:
            dice_sounds = random.choice(["FX/BACKROLL.ogg","FX/SHAKE1.ogg","FX/SHAKE3.ogg"])
            #for number in range(len(numbers)):
                #numbers[number] = random.randint(1,6)
            #rolls_left -= 1
            rolls_remaining -= 1
            pygame.mixer.Sound(dice_sounds).play()
            roll = False
        
        possible = check_possible(possible, numbers)
        current_score = check_scores(selected_choice, numbers, possible, score)
        totals, bonus_time = check_totals(totals, score, bonus_time)

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

        grandtotal.draw()

        if turn_counter == 0 and rolls_remaining == 3:
            
            bdsize = (600, 301)
            backdrop = pygame.Rect(screen_center[0] - (bdsize[0]//2), screen_center[1] - (bdsize[1]//2) + 119, bdsize[0], bdsize[1])
            pygame.draw.rect(screen, black, backdrop, 0)

            pygame.draw.rect(screen, forestgreen, backdrop, 10)

            text1 = "Welcome To"
            gamestarttext2 = font_h2.render(text1, True, black)
            text_rect1 = gamestarttext2.get_rect() #fix the centering
            text_rect1.centerx = screen_center[0]
            text_rect1.centery = screen_center[1] - 72  + 120
            draw_outlined_text(screen, text1, font_h2, black, gold, text_rect1.x, text_rect1.y)

            text2 = "YACHTZED!"
            gamestarttext2 = font_h1.render(text2, True, black)
            text_rect2 = gamestarttext2.get_rect() #fix the centering
            text_rect2.center = (WIDTH // 2, (HEIGHT // 2) + 120)
            draw_outlined_text(screen, text2, font_h1, white, forestgreen, text_rect2.x, text_rect2.y)

            text3 = "Click Roll Dice to Start"
            gamestarttext3 = font_h3.render(text3, True, black)
            text_rect3 = gamestarttext3.get_rect() #fix the centering
            text_rect3.centerx = screen_center[0]
            text_rect3.centery = (screen_center[1] + 72  + 120)
            draw_outlined_text(screen, text3, font_h3, black, gold, text_rect3.x, text_rect3.y)

        if turn_counter >= 14:
            game_over = True

        if game_over:
            bdsize = (WIDTH, 213)
            backdrop = pygame.Rect(screen_center[0] - (bdsize[0]//2), screen_center[1] - (bdsize[1]//2) + 75, bdsize[0], bdsize[1])
            pygame.draw.rect(screen, black, backdrop, 0)

            pygame.draw.rect(screen, red, backdrop, 5)
            
            gameovertext1 = font_h1.render("Game Over", True, red)
            text_rect = gameovertext1.get_rect() #fix the centering
            text_rect.center = (screen_center[0], screen_center[1] + 39)
            screen.blit(gameovertext1, text_rect)
            
            gameovertext2 = font_h3.render("Click Restart to Play Again", True, red)
            text_rect = gameovertext2.get_rect() #fix the centering
            text_rect.center = (screen_center[0], screen_center[1] + 111)
            screen.blit(gameovertext2, text_rect)
            
        pygame.display.flip()

    pygame.quit()

main()