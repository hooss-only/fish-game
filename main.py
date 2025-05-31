import pygame
from scenes.test_scene import TestScene

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1280))
    pygame.display.set_caption("fish game")

    scenes = []
    scenes.append(TestScene(screen))
    
    # basic game loop
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        scenes[0].tick()
        scenes[0].render()

        pygame.display.flip()
    return

if __name__ == "__main__":
    main()
