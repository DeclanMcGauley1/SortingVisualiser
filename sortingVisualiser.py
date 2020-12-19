import pygame
import random
import time
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

    def moveLeft(self):
        self.barStart -= 20

    def moveRight(self):
        self.barStart += 20


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
        WINDOW.fill((0,0,0))
        window_start = 0
        for bar in bars:
            pygame.draw.rect(WINDOW, (255,0,0), [window_start, 450, 10, -(bar.height)])
            window_start += 20
        pygame.display.update()

    #Does an insertion sort on a given list of numbers
    def insertionSort(bars):
        for i in range(1, len(bars)):
            holder = bars[i]
            j = i - 1
            while j >= 0 and bars[j].value > holder.value:
                bars[j + 1] = bars[j]
                j -= 1
            bars[j + 1] = holder
            drawWindow()
            time.sleep(0.2)
        return toBeSorted

    while run:
        drawWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        time.sleep(2)
        insertionSort(bars)
        time.sleep(0.5)
        run = False

def mainMenu():
    titleFont = pygame.font.SysFont("comicsans", 30)
    run = True

    while run:
        WINDOW.fill((0,0,0))
        titleLabel = titleFont.render("Press the mouse button for a visualisation of Insertion Sort...", 1, (255, 255, 255))
        WINDOW.blit(titleLabel, (WIDTH / 2 - titleLabel.get_width() / 2, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()


    pygame.quit()

mainMenu()
