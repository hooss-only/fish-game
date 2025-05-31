import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1280))
    pygame.display.set_caption("fish game")

    # basic game loop
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        pygame.display.flip()
    return

if __name__ == "__main__":
    main()
