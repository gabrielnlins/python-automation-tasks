from reset import reset
from farm import farm
from farm_utils import *
from get_images import processar_imagens
import pytesseract
import re

# def start():
#     while True:
#         data_from_farm = farm('/s15')
#         data_from_reset = reset()
#         if data_from_farm or data_from_reset > 1:
#             break

# start()

farm('/s15')

# image = pyautogui.screenshot(region=(1247, 0, 300, 500))
# image.save(r"C:\Users\Gabri\game\src\python-automation-tasks\teste.png")
# image = pytesseract.image_to_string(Image.open(r"C:\Users\Gabri\game\src\python-automation-tasks\teste.png"), lang="eng").lower()
# print(f"image: {image}")

# pyautogui.mouseInfo()()