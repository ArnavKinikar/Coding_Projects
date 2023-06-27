import pygame

Screen = Width, Height = 300, 300
CellSize= 20
Padding = 20
Rows = Cols = (Width - 4 * Padding) // CellSize
print(Rows, Cols)

pygame.init()
win = pygame.display.set_mode(Screen)

running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False

pygame.quit()