import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()  # Скрываем основное окно

# Выбор JPG файла
file_path = filedialog.askopenfilename(title="Выберите JPG файл", filetypes=[("JPEG files", "*.jpg;*.jpeg")])
if file_path:
    image = Image.open(file_path)
    
    # Задаём имя выходного файла (заменяем расширение на .png)
    output_path = file_path.rsplit(".", 1)[0] + ".png"
    
    image.save(output_path, "PNG")
    print(f"Файл сохранён как: {output_path}")
