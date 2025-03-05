import pygame
import ollama

# Инициализация Pygame
pygame.init()

# Настройки окна
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Чат с ИИ")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Шрифты
font = pygame.font.Font(None, 30)
input_font = pygame.font.Font(None, 24)

# Переменные
input_text = ""
chat_history = []

def draw_chat():
    screen.fill(WHITE)

    # Рисуем историю чата
    y_offset = 10
    for message in chat_history[-10:]:  # Показываем только последние 10 сообщений
        text = font.render(message, True, BLACK)
        screen.blit(text, (10, y_offset))
        y_offset += 40

    # Рисуем поле ввода
    input_box = pygame.Rect(10, SCREEN_HEIGHT - 40, SCREEN_WIDTH - 20, 30)
    pygame.draw.rect(screen, BLACK, input_box, 2)

    input_text_surface = input_font.render(input_text, True, BLACK)
    screen.blit(input_text_surface, (input_box.x + 5, input_box.y + 5))

    pygame.display.flip()

def chat_with_model(user_input):
    # Отправляем запрос модели
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["message"]["content"]

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Отправить сообщение при нажатии Enter
                if input_text.strip():  # Если поле ввода не пустое
                    chat_history.append(f"Ты: {input_text}")
                    response = chat_with_model(input_text)
                    chat_history.append(f"ИИ: {response}")
                    input_text = ""  # Очистить поле ввода
            elif event.key == pygame.K_BACKSPACE:  # Удалить последний символ
                input_text = input_text[:-1]
            else:
                input_text += event.unicode  # Добавить символ в текст

    # Обновляем экран
    draw_chat()

pygame.quit()
