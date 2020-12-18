import pygame
import random
import time

WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#Represents the bars that are going to move in the visualisation
class Bar:
    def __init__(self, value, barStart):
        self.value = value
        self.barStart = barStart
        self.height = self.value * 10

    def moveLeft(self):
        self.barStart -= 20

    def moveRight(self):
        self.barStart += 20

#Does an insertion sort on a given list of numbers
def insertionSort(toBeSorted, bars):
    for i in range(1, len(toBeSorted)):
        holder = toBeSorted[i]
        j = i - 1

        while j >= 0 and toBeSorted[j] > holder:
            toBeSorted[j + 1] = toBeSorted[j]
            j -= 1

        toBeSorted[j + 1] = holder

    return toBeSorted


def main():
    run = True
    width_count = 0

    #generates the list to be sorted
    toBeSorted = list()
    for i in range(10):
        toBeSorted.append(random.randint(1, 30))

    bars = list()
    for number in toBeSorted:
        bars.append(Bar(number, width_count))
        width_count += 20


    def drawWindow():
        for bar in bars:
            pygame.draw.rect(WINDOW, (255,0,0), [bar.barStart , 450, 10, -(bar.height)])

        pygame.display.update()

    while run:
        drawWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        time.sleep(2)




main()
