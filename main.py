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
    clock = pygame.time.Clock()
    delta_time = 0.1
    while loop:
        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            scenes[0].handle_event(event, delta_time)

        scenes[0].tick(delta_time)
        scenes[0].render()

        pygame.display.flip()

        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
    return

if __name__ == "__main__":
    main()
