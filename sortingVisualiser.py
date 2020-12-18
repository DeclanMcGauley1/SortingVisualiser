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

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bar in bars:
            pygame.draw.rect(WINDOW, (255,0,0), [bar.barStart , 450, 10, -(bar.height)])

        pygame.display.update()
        time.sleep(2)
        WINDOW.fill((0,0,0))



        for bar in bars:
            pygame.draw.rect(WINDOW, (255,0,0), [bar.barStart , 450, 10, -(bar.height)])

        pygame.display.update()

main()
