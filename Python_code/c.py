import pygame

# crear la ventana de Pygame
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Peso en cada lado de la celda')

# crear una fuente para renderizar el peso
FONT_SIZE = 20
font = pygame.font.SysFont(None, FONT_SIZE)

# crear un diccionario que contenga los pesos para cada celda
maze = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cell_size = 50

# dibujar cada celda
for row in range(len(maze)):
    for col in range(len(maze[0])):
        x = col * cell_size
        y = row * cell_size
        weight = maze[row][col]
        # dibujar el rectángulo superior
        pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size, cell_size/2))
        text = font.render(str(weight), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x + cell_size/2, y + cell_size/4)
        screen.blit(text, text_rect)
        # dibujar el rectángulo inferior
        pygame.draw.rect(screen, (255, 255, 255), (x, y + cell_size/2, cell_size, cell_size/2))
        text = font.render(str(weight), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x + cell_size/2, y + cell_size*3/4)
        screen.blit(text, text_rect)
        # dibujar el rectángulo izquierdo
        pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size/2, cell_size))
        text = font.render(str(weight), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x + cell_size/4, y + cell_size/2)
        screen.blit(text, text_rect)
        # dibujar el rectángulo derecho
        pygame.draw.rect(screen, (255, 255, 255), (x + cell_size/2, y, cell_size/2, cell_size))
        text = font.render(str(weight), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x + cell_size*3/4, y + cell_size/2)
        screen.blit(text, text_rect)

# actualizar la pantalla
pygame.display.update()

# esperar a que el usuario cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
