import pygame
import random
import time
import tkinter as tk
from tkinter import simpledialog
pygame.font.init()

WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#Represents the bars that are going to move in the visualisation
class Bar:
    def __init__(self, value, barStart):
        self.value = value
        self.barStart = barStart
        self.height = self.value * 10
        self.selected = False

    def moveLeft(self):
        self.barStart -= 20

    def moveRight(self):
        self.barStart += 20


def main(sort):
    run = True
    width_count = 0

    #generates the list to be sorted
    toBeSorted = list()
    for i in range(10):
        toBeSorted.append(random.randint(1, 40))

    bars = list()
    for number in toBeSorted:
        bars.append(Bar(number, width_count))
        width_count += 20


    def drawWindow():
        WINDOW.fill((0,0,0))
        window_start = 0
        for bar in bars:
            if bar.selected == True:
                pygame.draw.rect(WINDOW, (0,255,0), [window_start, 450, 10, -(bar.height)])
            else:
                pygame.draw.rect(WINDOW, (255,0,0), [window_start, 450, 10, -(bar.height)])
            window_start += 20
            bar.selected = False
        pygame.display.update()

    #Does an insertion sort on a given list of numbers
    def insertionSort(bars):
        for i in range(1, len(bars)):
            holder = bars[i]
            holder.selected = True
            j = i - 1
            while j >= 0 and bars[j].value > holder.value:
                bars[j + 1] = bars[j]
                j -= 1
                drawWindow()
                time.sleep(0.3)
            bars[j + 1] = holder
            time.sleep(0.5)
        return toBeSorted

    #Draws the initial unsorted bars to the screen
    drawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #sorts the bars and shows the visualisation
    time.sleep(2)
    if sort == "Insertion":
        insertionSort(bars)
    elif sort == "Bubble":
        bubbleSort(bars)
    time.sleep(0.5)
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
                    selectedSort = simpledialog.askstring(title="Sorting", prompt="Choose a sort to visualise..")
                    #Checks which sort the user wants to see
                    if selectedSort == "insertion" or "Insertion":
                        notValid = False
                        main("Insertion")
    pygame.quit()

mainMenu()
