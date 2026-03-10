#imports
import random
import time
import json
import pygame

#initialization of pygame
pygame.init()

#screen width and height constants
WIDTH = 1600
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
font_reg = pygame.font.Font('Open_Sans\static\OpenSans-Regular.ttf', 18)
font_title = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 96)
font_h1 = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 72)
font_h2 = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 48)
font_h3 = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 36)
font_h4 = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 24)
font_h5 = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 20)
font_h6 = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 16)
font_i = pygame.font.Font('Open_Sans\static\OpenSans-Italic.ttf', 18)
font_b = pygame.font.Font('Open_Sans\static\OpenSans-Bold.ttf', 18)
font_m = pygame.font.Font('Open_Sans\static\OpenSans-Medium.ttf', 18)
font_l = pygame.font.Font('Open_Sans\static\OpenSans-Light.ttf', 18)
font_c = pygame.font.Font('Open_Sans\static\OpenSans-Condensed.ttf', 18)

def main():
    running = True
    while running:
        timer.tick(fps)
        screen.fill(background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    