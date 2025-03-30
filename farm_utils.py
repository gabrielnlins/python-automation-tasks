import pyautogui
import pytesseract
from time import sleep, time
from PIL import Image
import json
import pygetwindow as gw

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\tesseract.exe"
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

solve_challenge = 'resolva o desafio'
confirmation_button_path = r"C:\Users\Gabri\game\src\python_automation_tasks\images\confirm_button.png"
verify_left_arrow = r"C:\Users\Gabri\game\src\python_automation_tasks\images\left_arrow_2.png"
avoid = r"C:\Users\Gabri\game\src\python_automation_tasks\images\avoid.png"
# attack_button = r"C:\Users\Gabri\game\src\python_automation_tasks\images\start.png"
# stop_button = r"C:\Users\Gabri\game\src\python_automation_tasks\images\stop.png"

timeout = 60
middle_screen = 1566,320
attack_button = 1069,51
position_losttower = 1603,486
npc_reset = 1395,185
walk = 1442,270
x, y = 1395,185
count = 0

def click():
    pyautogui.click(middle_screen, duration=0)

def reset():
    # click()
    stop_attack()
    write_message('/resetar')
    sleep(1)
    start_time = time()
    while not get_images():
        print(f"Executando o loop de reset()... start_time: {start_time}, timeout: {timeout}")
        get_images()
        if time() - start_time > timeout:
            print("Timeout atingido, retornando...")
            click_on_confirm()
            break
    sleep(1)

def write_message(message):
    pyautogui.hotkey('enter', presses=3, interval=0.5)
    pyautogui.write(message)
    pyautogui.hotkey('enter', presses=3, interval=0.5)

def press_button():
    pyautogui.hotkey('c', presses=3, interval=0.5)

def hold_button(x, y):
    pyautogui.mouseDown(x, y, button='left', duration=2)
    pyautogui.mouseUp(x, y, button='left')

def farm(location):
    sleep(1)
    # data = get_data()
    start_time = time()
    while not get_images():
        print(f"Executando o loop de farm()... start_time: {start_time}, timeout: {timeout}")
        get_images()
        if time() - start_time > timeout:
            print("Timeout atingido, retornando...")
            click_on_confirm()
            break
        sleep(1)
    time_to_sleep = 40
    write_message(location)
    if location == '/losttower7':
        hold_button(position_losttower[0], position_losttower[1])
        time_to_sleep = 90
    start_attack()
    press_button()
    sleep(time_to_sleep)
    print(f"Resetando...")
    data = get_data()
    data['count'] += 1
    data['resets'] += 1
    set_data(data)
    print(f"Data: {data}")
    # write_message('/a 1000')
    # write_message('/e 3500')    

def stop_attack():
    try:
        pyautogui.click(attack_button, duration=0)
        # button = pyautogui.locateOnScreen(stop_button, confidence=0.8)
        # pyautogui.click(pyautogui.center(button))
    except Exception as e:
        print(f"Erro ao procurar botão de STOP {e}")
        return True
def start_attack():
    try:
        pyautogui.click(attack_button, duration=0)
        # button = pyautogui.locateOnScreen(attack_button, confidence=0.8)
        # pyautogui.click(pyautogui.center(button))
    except Exception as e:
        print(f"Erro ao procurar botão de START {e}")
        return True
def auto_farm():
    while True:
        reset()
        farm('/s15')

def after_mr():
    while True:
        reset()
        farm('/losttower7')

def get_images():
    # click()
    clicar_na_janela_virtualmente("MudinhoX", 1566, 320)
    try:
        text = pytesseract.image_to_string(Image.open(avoid), lang="eng")
        coord_images = pyautogui.locateOnScreen(verify_left_arrow, confidence=0.8)
        if solve_challenge in text.lower() and coord_images:
            rotate_image(verify_left_arrow)
            if not find_correct_image(count):
                data = get_data()
                print(f"Contagem: {data['count_retry']}")
                return False
            else:
                sleep(3)
                print("Imagem encontrada...")
                click_on_confirm()
                # button = pyautogui.locateOnScreen(confirmation_button_path, confidence=0.8)
                # pyautogui.click(pyautogui.center(button))
                sleep(3)
                return True
        else:
            print("Botão não encontrado.")
            return False
    except Exception as e:
        print(f"Ainda não foi solicitado o preenchimento do Captcha {e}")
        return True

def mouse():
    pyautogui.mouseInfo()

def click_on_confirm():
    try:
        button = pyautogui.locateOnScreen(confirmation_button_path, confidence=0.8)
        pyautogui.click(pyautogui.center(button))
    except Exception as e:
        print(f"Erro ao procurar botão de confirmação {e}")
        return True
def rotate_image(image_path):
    if "left_arrow" in image_path:
        button = pyautogui.locateOnScreen(verify_left_arrow, confidence=0.8)
        pyautogui.click(pyautogui.center(button))
        add_retry()

def find_correct_image(count):
    images_to_check = [
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\axe_1.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\bull_1.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\dragon_armor.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\dragon_helmet.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\boots_3.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\boots_1.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\boots_2.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\brass_armor_2.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\iron_shield_1.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\scale_helmet.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\skull_shield.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\sm_armor.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\small_shield.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\sorcerer.png",
        r"C:\Users\Gabri\game\src\python_automation_tasks\images_on_format\spider.png",
    ]
    try:
        for images in images_to_check:
            end = {images.split('\\')[-1]}
            image_found = None
            while True:
                try:
                    image_found = pyautogui.locateOnScreen(images, confidence=0.8)
                    if image_found:
                        print(f"Imagem encontrada: {image_found}")
                        return True
                    else:
                        break
                except pyautogui.ImageNotFoundException:
                    if count > 25:
                        print(f"Imagem não encontrada: {end}")
                        return True
                    break
    except Exception as e:
        print(f"An error occurred: {e} while looking for: {end}")
        return False

def add_retry():
    data = get_data()
    data['count_retry'] = data['count_retry'] + 1
    set_data(data)
    return data

def is_possible_retry(data):
    if data['count_retry'] > 5: #30
        print("Retorna True para evitar loop infinito.")
        return False
    else:
        return True

def get_data():
    with open(r"C:\Users\Gabri\game\src\python_automation_tasks\database.json", 'r') as file:
        return json.load(file)

def set_data(data):
    with open(r"C:\Users\Gabri\game\src\python_automation_tasks\database.json", 'w') as file:
        json.dump(data, file, indent=4)




def tirar_print_janela(nome_janela, caminho_arquivo):
    # click()
    janela = gw.getWindowsWithTitle(nome_janela)[0]
    janela.activate()
    print(f"Janela encontrada: {janela.title}")
    x, y = janela.left, janela.top
    largura, altura = janela.width, janela.height

    print(f"Janela encontrada: {janela.title}")
    print(f"Coordenadas: ({x}, {y}), Tamanho: {largura}x{altura}")

    # Tira o print apenas da região da janela
    screenshot = pyautogui.screenshot(region=(x, y, largura, altura))
    screenshot.save(caminho_arquivo)
    print(f"Screenshot salvo em: {caminho_arquivo}")
    read_properties(caminho_arquivo)

def read_properties(file_path):
    full_list = []
    text = pytesseract.image_to_string(Image.open(file_path), lang="eng")
    list_of_strings = text.split()
    for string in list_of_strings:
        if string == '32767':
            print(f"Status full encontrado: {string}")
            full_list.append(string)
    print(f"Quantidade de atributos full: {len(full_list)}")
    return len(full_list)

def clicar_na_janela(nome_janela, x_relativo, y_relativo):
    # Localiza a janela pelo título
    janela = gw.getWindowsWithTitle(nome_janela)[0]
    if janela:
        # Calcula as coordenadas absolutas com base na posição da janela
        x_absoluto = janela.left + x_relativo
        y_absoluto = janela.top + y_relativo

        # Simula o clique nas coordenadas calculadas
        pyautogui.click(x=x_absoluto, y=y_absoluto)
        print(f"Clique realizado em ({x_absoluto}, {y_absoluto}) na janela '{nome_janela}'")
    else:
        print(f"Janela '{nome_janela}' não encontrada.")

import win32gui
import win32api
import win32con

def clicar_na_janela_virtualmente(nome_janela, x_relativo, y_relativo):
    # Localiza a janela pelo título
    hwnd = win32gui.FindWindow(None, nome_janela)
    if hwnd:
        # Obtém as coordenadas da janela
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        # x_absoluto = left + x_relativo
        # y_absoluto = top + y_relativo
        x_absoluto = x_relativo
        y_absoluto = y_relativo

        # Envia um evento de clique para a janela
        lParam = win32api.MAKELONG(x_absoluto, y_absoluto)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
        print(f"Clique virtual realizado em ({x_absoluto}, {y_absoluto}) na janela '{nome_janela}'")
    else:
        print(f"Janela '{nome_janela}' não encontrada.")

# Exemplo de uso
# clicar_na_janela_virtualmente("MudinhoX", 1566, 320)  # Clique em (100, 200) relativo à janela

# Exemplo de uso
# clicar_na_janela("MudinhoX", 100, 200)  # Clique em (100, 200) relativo à janela