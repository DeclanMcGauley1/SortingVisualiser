import pygame
import random
import time
import tkinter as tk
from tkinter import simpledialog
pygame.font.init()

#Creating the window
WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


#Represents the bars that are going to move in the visualisation
class Bar:
    def __init__(self, value):
        self.value = value
        self.height = self.value * 10
        self.selected = False



def main(sort):
    run = True

    #generates the list to be sorted
    toBeSorted = list()
    for i in range(10):
        toBeSorted.append(random.randint(1, 40))

    #Generates bar objecs from the generated list
    bars = list()
    for number in toBeSorted:
        bars.append(Bar(number))

    #draws the bars and the animations to the window
    def drawWindow():
        #blacks out the screen to redraw elements
        WINDOW.fill((0,0,0))
        width_start = 0
        #Draws bars onto the screen from a list of bars
        for bar in bars:
            #If a bar is the one moving it is drawn green rather than red
            if bar.selected == True:
                pygame.draw.rect(WINDOW, (0,255,0), [width_start, 450, 10, -(bar.height)])
            else:
                pygame.draw.rect(WINDOW, (255,0,0), [width_start, 450, 10, -(bar.height)])
            width_start += 20
            bar.selected = False
        pygame.display.update()


    #Does an insertion sort on a given list of numbers
    def insertionSort(bars):
        for i in range(1, len(bars)):
            j = i - 1

            while (j >= 0 and bars[j].value > bars[j + 1].value):
                #if the two values are the wrong war around, swap them
                bars[j + 1].selected = True
                temp = bars[j + 1]
                bars[j + 1] = bars[j]
                bars[j] = temp
                j-=1
                #redraws the window every time bars are swapped
                drawWindow()
                #stops the program for half a second
                time.sleep(0.5)

        return bars

    #Does a bubble sort on the bars list
    def bubbleSort(bars):
        sorted = False
        while not sorted:
            sorted = True
            for i in range(0, len(bars) - 1):
                if bars[i].value > bars[i + 1].value:
                    sorted = False
                    bars[i].selected = True
                    holder = bars[i + 1]
                    bars[i + 1] = bars[i]
                    bars[i] = holder
                    #redraws the window every time the bars are swapped
                    drawWindow()
                    #stops the program for half a second
                    time.sleep(0.5)


    #Draws the initial unsorted bars to the screen
    drawWindow()

    #handles the user event for when the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #runs different sorting algorithms based on what the user has chosen
    time.sleep(2)
    if sort == "Insertion":
        insertionSort(bars)
    elif sort == "Bubble":
        bubbleSort(bars)
    time.sleep(2)

    run = False

#Controls the main menu that will load before and after the visualisation takes place
def mainMenu():
    titleFont = pygame.font.SysFont("comicsans", 30)
    run = True

    while run:
        #Puts the prompt in the form of a label on the middle of the screen
        WINDOW.fill((0,0,0))
        titleLabel = titleFont.render("Press the to pick a sorting algorithm to visualise...", 1, (255, 255, 255))
        WINDOW.blit(titleLabel, (WIDTH / 2 - titleLabel.get_width() / 2, 250))
        pygame.display.update()

        #Checks if the user closes the window or if they click the mous button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #while there isnt a valid user input the program will continue to prompt the user for input
                notValid = True
                while notValid:
                    ROOT = tk.Tk()
                    ROOT.withdraw()
                    selectedSort = simpledialog.askstring(title="Sorting", prompt="Choose a sort to visualise")
                    #Checks which sort the user wants to see
                    if selectedSort == ("insertion" or "Insertion"):
                        notValid = False
                        main("Insertion")
                    elif selectedSort == ("bubble" or "Bubble"):
                        notValid = False
                        main("Bubble")
    pygame.quit()

mainMenu()
