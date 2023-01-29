import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Tamaño de la pantalla
tamaño_pantalla = (800, 600)
pantalla = pygame.display.set_mode(tamaño_pantalla)

# Título de la pantalla
pygame.display.set_caption("Juego de la serpiente")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)

# Variables del juego
reloj = pygame.time.Clock()
tamaño_cuadro = 10
velocidad = 30

# Posición inicial de la serpiente
serpiente_x = 300
serpiente_y = 300
serpiente_cuerpo = []
longitud_serpiente = 1

# Dirección de la serpiente
direccion = "derecha"

# Comida para la serpiente
comida_x = 0
comida_y = 0

# Fuente para el puntaje
fuente = pygame.font.SysFont(None, 25)

# Puntuación
puntuacion = 0

# Bucle principal del juego
juego_corriendo = True
while juego_corriendo:
    # Control de velocidad del juego
    reloj.tick(velocidad)

    # Eventos del juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_corriendo = False

    # Lógica del juego
    # Mover la serpiente
    if direccion == "derecha":
        serpiente_x += tamaño_cuadro
    if direccion == "izquierda":
        serpiente_x -= tamaño_cuadro
    if direccion == "arriba":
        serpiente_y -= tamaño_cuadro
    if direccion == "abajo":
        serpiente_y += tamaño_cuadro

    # Agregar un cuadro al cuerpo de la serpiente
    cuerpo_serpiente = []
    cuerpo_serpiente.append(serpiente_x)
    cuerpo_serpiente.append(serpiente_y)
    serpiente_cuerpo.append(cuerpo_serpiente)
    if len(serpiente_cuerpo) > longitud_serpiente:
        del serpiente_cuerpo[0]

    # Comida para la serpiente
    if serpiente_x == comida_x and serpiente_y == comida_y:
        comida_x = round(random.random)
