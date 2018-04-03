import pygame

if __name__ == "__main__":
    screen = pygame.display.set_mode((480,890),0,32)
    backgroud = pygame.image.load("./images/bg2.jpg").convert()
    while True:
        screen.blit(backgroud(0,0))
        pygame.display.update()
        time.sleep(0.04)
