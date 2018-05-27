import pygame
import core

chip8 = core.Chip8()

black = (0, 0, 0)
white = (255, 255, 255)
drawColor = white

def main():
    screen = pygame.display.set_mode((64, 32))
    pygame.display.set_caption("ChocChip")
    chip8.loadGame("roms/pong.c8")
    print(chip8.memory)
    running = True
    while running:
        w, h = pygame.display.get_surface().get_size()

        chip8.emulateCycle()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        if chip8.drawFlag:
            # Draw Graphics
            screen.fill(black)
            pygame.display.flip()
        chip8.setKeys()
        
    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
