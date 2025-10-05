from gtts import gTTS
import random
import time
import pygame
from datetime import datetime


def listen_command():
    """Отримує команду від користувача через текстовий ввід"""
    return input("Введіть команду: ")

def do_this_command(message):
    """Обробка команд користувача"""
    message = message.lower()

    if "hello" in message:
        say_message("Hello! How are you?")
    elif "goodbye" in message:
        say_message("Goodbye, friend!")
        exit()
    elif "time" in message:
        say_message(f"The current time is {datetime.now().strftime('%H:%M:%S')}")
    elif "how are you" in message:
        say_message("I'm fine, thank you!")
    else:
        say_message("Command not recognized")

def say_message(message):
    """Відтворення та збереження голосового повідомлення"""
    print("Voice assistant:", message)

    # Створюємо голосове повідомлення
    voice = gTTS(text=message, lang="en")

    # Унікальна назва файлу для збереження
    file_name = f"_audio_{str(time.time())}_{random.randint(0,100000)}.mp3"
    voice.save(file_name)

    # Відтворення аудіо через pygame
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    # Чекаємо поки аудіо відтвориться
    while pygame.mixer.music.get_busy():
        continue

# ---------------- Основна програма ----------------
if __name__ == '__main__':
    print("=== Голосовий помічник запущено ===")
    while True:
        command = listen_command()
        do_this_command(command)
