from reset import reset
from farm import farm
from farm_utils import *
from get_images import processar_imagens
import pytesseract
import re

def start():
    while True:
        data_from_farm = farm('/s15')
        data_from_reset = reset()
        if data_from_farm or data_from_reset > 1:
            break

start()



# img = pyautogui.screenshot(region=(1642, 110, 125, 30)) # Level
# img = pyautogui.screenshot(region=(1642, 200, 125, 30)) # Força
# img = pyautogui.screenshot(region=(1642, 292, 125, 30)) # Agilidade
# img = pyautogui.screenshot(region=(1642, 380, 125, 30)) # Vitalidade
# img = pyautogui.screenshot(region=(1642, 465, 125, 30)) # Energia
# img.save(r"C:\Users\Gabri\game\src\python-automation-tasks\mudinho_teste.png")
# print(f"{img} salva")

# image = pyautogui.click(
#     pyautogui.locateCenterOnScreen(r"C:\Users\Gabri\game\src\python-automation-tasks\x.png")
#     )
# # pyautogui.mouseInfo()()

# print(f"image: {image}")