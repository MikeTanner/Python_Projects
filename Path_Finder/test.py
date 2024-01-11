import pygame
import time

pygame.init()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.draw.rect(WIN, (255, 0, 0), (20, 20, 50, 50))
pygame.display.flip()
time.sleep(1)
