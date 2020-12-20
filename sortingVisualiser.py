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
            drawWindow(bars)
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
                drawWindow(bars)
                #stops the program for half a second
                time.sleep(0.5)

def quickSort(bars):
    if len(bars) <= 1:
        return bars
    return partition(bars,0,len(bars)-1)

def partition(bars,start,end):
    pivot = bars[end]
    pivot.selected = True
    border = start
    if start < end:
        for i in range(start,end+1):
            if bars[i].value <= pivot.value:
                temp = bars[border]
                bars[border] = bars[i]
                bars[i] = temp
                if i != end:
                    border += 1
        drawWindow(bars)
        time.sleep(0.2)
        partition(bars,start,border-1)
        partition(bars,border+1,end)
        drawWindow(bars)
        time.sleep(0.2)

    return bars

def selectionSort(bars):
    for i in range(0, len(bars) - 1):
        minimum = i
        for j in range(i + 1, len(bars)):
            if bars[j].value < bars[minimum].value:
                minimum = j

        if minimum != i:
            bars[minimum].selected = True
            temp = bars[minimum]
            bars[minimum] = bars[i]
            bars[i] = temp
            drawWindow(bars)
            time.sleep(0.5)

def merge(bars, start, middle, end):
    sublistStart = middle + 1
    if (bars[middle].value <= bars[sublistStart].value):
        return

    while (start <= middle and sublistStart <= end):

        if (bars[start].value <= bars[sublistStart].value):
            start += 1
        else:
            value = bars[sublistStart]
            index = sublistStart

            while (index != start):
                bars[index] = bars[index - 1]
                index -= 1;

            bars[start] = value

            start += 1
            middle += 1
            sublistStart += 1
    drawWindow(bars)
    time.sleep(0.2)
    return bars

def mergeSort(bars, start, end):
    if start < end:
        middle = start + (end - start) // 2;
        mergeSort(bars, start, middle);
        mergeSort(bars, middle + 1, end);
        return merge(bars, start, middle, end);


#draws the bars and the animations to the window
def drawWindow(bars):
    a = 2 * (len(bars) - 1)
    b = WIDTH - a
    c = b / len(bars)
    #blacks out the screen to redraw elements
    WINDOW.fill((0,0,0))
    width_start = 0
    #Draws bars onto the screen from a list of bars
    for bar in bars:
        #If a bar is the one moving it is drawn green rather than red
        if bar.selected == True:
            pygame.draw.rect(WINDOW, (0,255,0), [width_start, 450, c, -(bar.height)])
        else:
            pygame.draw.rect(WINDOW, (255,0,0), [width_start, 450, c, -(bar.height)])
        width_start += (c + 2)
        bar.selected = False
    pygame.display.update()


def main(sort, num):
    run = True

    #generates the list to be sorted
    toBeSorted = list()
    for i in range(num):
        toBeSorted.append(random.randint(1, 40))

    #Generates bar objecs from the generated list
    bars = list()
    for number in toBeSorted:
        bars.append(Bar(number))


    #Draws the initial unsorted bars to the screen
    drawWindow(bars)

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
    elif sort == "Quick":
        quickSort(bars)
    elif sort == "Selection":
        selectionSort(bars)
    elif sort == "Merge":
        mergeSort(bars, 0, len(bars) - 1)

    time.sleep(2)

    run = False

#Controls the main menu that will load before and after the visualisation takes place
def mainMenu():
    titleFont = pygame.font.SysFont("comicsans", 60)
    promptFont = pygame.font.SysFont("comicsans", 30)
    run = True

    while run:
        #Puts the prompt in the form of a label on the middle of the screen
        WINDOW.fill((0,0,0))
        titleLabel = titleFont.render("Welcome to the algorithms visualiser!", 1, (255,255,255))
        promptLabel = promptFont.render("Click your mouse to start...", 1, (255, 255, 255))
        WINDOW.blit(titleLabel, (WIDTH / 2 - titleLabel.get_width() / 2, 100))
        WINDOW.blit(promptLabel, (WIDTH / 2 - promptLabel.get_width() / 2, 250))
        pygame.display.update()

        #Checks if the user closes the window or if they click the mous button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                controlScreen()
    pygame.quit()


def controlScreen():
    run = True
    numberFont = pygame.font.SysFont("comicsans", 40)

    while run:
        WINDOW.fill((0,0,0))
        numberLabel = numberFont.render("Click the mouse to select the number of elements to sort..", 1, (255,255,255))
        WINDOW.blit(numberLabel, (WIDTH / 2 - numberLabel.get_width() / 2, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                valid = False
                while not valid:
                    ROOT = tk.Tk()
                    ROOT.withdraw()
                    selectedNum = simpledialog.askstring(title="Number", prompt="Choose a number of elements")
                    valid = True
                    algorithmPick(int(selectedNum))



def algorithmPick(number):
    algoFont = pygame.font.SysFont("comicsans", 40)
    chosenFont = pygame.font.SysFont("comicsans", 50)
    run = True
    while run:
        #Puts the prompt in the form of a label on the middle of the screen
        WINDOW.fill((0,0,0))
        algoLabel = algoFont.render("Choose an algorithm to visualise..", 1, (255,255,255))
        insertionLabel = chosenFont.render("Press the I key to visualise an Insertion sort", 1, (255,255,255))
        bubbleLabel = chosenFont.render("Press the B key to visualise a Bubble sort", 1, (255,255,255))
        quickLabel = chosenFont.render("Press the Q key to visualise a Quick sort", 1, (255,255,255))
        selectionLabel = chosenFont.render("Press the S key to visualise a Selection sort", 1, (255,255,255))
        WINDOW.blit(algoLabel, (WIDTH / 2 - algoLabel.get_width() / 2, 250))
        WINDOW.blit(insertionLabel, (WIDTH / 2 - insertionLabel.get_width() / 2, 300))
        WINDOW.blit(bubbleLabel, (WIDTH / 2 - bubbleLabel.get_width() / 2, 350))
        WINDOW.blit(quickLabel, (WIDTH / 2 - quickLabel.get_width() / 2, 400))
        WINDOW.blit(selectionLabel, (WIDTH / 2 - selectionLabel.get_width() / 2, 450))
        pygame.display.update()

        #Checks if the user closes the window or if they click the mous button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_i]:
            main("Insertion", number)
        elif keys[pygame.K_b]:
            main("Bubble", number)
        elif keys[pygame.K_q]:
            main("Quick", number)
        elif keys[pygame.K_s]:
            main("Selection", number)
        elif keys[pygame.K_m]:
            main("Merge", number)


mainMenu()
