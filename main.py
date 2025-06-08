import pygame
from scenes.main_scene import MainScene
from scenes.play_scene import PlayScene

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1280))
    pygame.display.set_caption("fish game")

    scenes = []
    scenes.append(MainScene(screen))
    scenes.append(PlayScene(screen))
    scene_number = 0
    
    # basic game loop
    loop = True
    clock = pygame.time.Clock()
    delta_time = 0.1

    scenes[scene_number].init()
    while loop:
        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            scenes[scene_number].handle_event(event, delta_time)

        scenes[scene_number].tick(delta_time)
        scenes[scene_number].render()

        pygame.display.flip()

        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
            
        next_scene_number = scenes[scene_number].get_scene_number()
        if (scene_number != next_scene_number):
            scenes[scene_number].close()
            scene_number = next_scene_number
            scenes[scene_number].init()
    return

if __name__ == "__main__":
    main()
