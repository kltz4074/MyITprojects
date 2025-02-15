

import pygame
import time

# Инициализация Pygame
pygame.init()

# Инициализация джойстика
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Включение вибрации
if joystick.get_numhats() > 0:
    joystick.rumble(1.0, 1.0, 2000)  # (сила левой вибрации, сила правой вибрации, длительность в миллисекундах)
    time.sleep(2)  # Ожидание окончания вибрации

# Завершение работы с джойстиком
joystick.quit()
pygame.quit()

