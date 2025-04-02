from PIL import Image
from time import sleep
from farm_utils import *
from concurrent.futures import ThreadPoolExecutor
import pyautogui
import pytesseract
import re

def get_images():
    click()
    try:
        text = pytesseract.image_to_string(Image.open(avoid), lang="eng")
        coord_images = pyautogui.locateOnScreen(verify_left_arrow, confidence=0.8)
        if solve_challenge in text.lower() and coord_images:
            rotate_image(verify_left_arrow)
            if not processar_imagens(images_to_check):
                return False
            else:
                print("Imagem encontrada...")
                click_on_confirm()
                if invalid_response in pytesseract.image_to_string(Image.open(r"C:\Users\Gabri\game\src\python-automation-tasks\invalid_response.png"), lang="eng").lower():
                    return False
                sleep(0.5)
                return True
        else:
            print("Botão não encontrado.")
            return False
    except Exception as e:
        print(f"Ainda não foi solicitado o preenchimento do Captcha {e}")
        return True

def rotate_image(image_path):
    if "left_arrow" in image_path:
        button = pyautogui.locateOnScreen(verify_left_arrow, confidence=0.8)
        pyautogui.click(pyautogui.center(button), duration=0.15)

def verificar_imagem(image_path):
    try:
        image_found = pyautogui.locateOnScreen(image_path, confidence=0.8)
        if image_found:
            return image_path
    except Exception as e:
        return None
    return None

def processar_imagens(images_to_check):
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(verificar_imagem, images_to_check))
    imagens_encontradas = [resultado for resultado in resultados if resultado]
    if (imagens_encontradas):
        return True
    return False

# images = [
#     pyautogui.screenshot(region=(1642, 205, 125, 30)), # Força
#     pyautogui.screenshot(region=(1642, 292, 125, 30)), # Agilidade
#     pyautogui.screenshot(region=(1642, 380, 125, 30)), # Vitalidade
#     pyautogui.screenshot(region=(1642, 465, 125, 30)), # Energia
# ]

def get_level_reset():
    image = pyautogui.screenshot(region=(1642, 110, 125, 30))
    image.save(r"C:\Users\Gabri\game\src\python-automation-tasks\temporary_level_image.png")
    image = pytesseract.image_to_string(Image.open(r"C:\Users\Gabri\game\src\python-automation-tasks\temporary_level_image.png"), lang="eng")
    level = re.sub(r"\D", "", image)
    if level:
        if int(level) >= 325:
            return True
        else:
            return False
    else:
        return False

# def get_attributes():
#     # for image in images:
#     #     image.save(r"C:\Users\Gabri\game\src\python-automation-tasks\temporary_attribute_image.png")
#     #     image = pytesseract.image_to_string(Image.open(r"C:\Users\Gabri\game\src\python-automation-tasks\temporary_attribute_image.png"), lang="eng")
#     #     print(f"image: {re.sub(r"\D", "", image)}")
#     image = pyautogui.screenshot(region=(1642, 205, 125, 30)) # Força
#     image.save(r"C:\Users\Gabri\game\src\python-automation-tasks\temporary_attribute_image.png")
#     image = pytesseract.image_to_string(Image.open(r"C:\Users\Gabri\game\src\python-automation-tasks\temporary_attribute_image.png"), lang="eng")
#     if image 
    
#     pyautogui.screenshot(region=(1642, 292, 125, 30)) # Agilidade
#     pyautogui.screenshot(region=(1642, 380, 125, 30)) # Vitalidade
#     pyautogui.screenshot(region=(1642, 465, 125, 30)) # Energia