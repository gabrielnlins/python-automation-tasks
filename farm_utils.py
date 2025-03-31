import pyautogui
import pytesseract
from time import sleep, time
from PIL import Image
import json
import pygetwindow as gw
import win32gui
import win32api
import win32con

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\tesseract.exe"
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

game = "MudinhoX"
solve_challenge = 'resolva o desafio'
confirmation_button_path = r"C:\Users\Gabri\game\src\python-automation-tasks\images\confirm_button.png"
verify_left_arrow = r"C:\Users\Gabri\game\src\python-automation-tasks\images\left_arrow_2.png"
avoid = r"C:\Users\Gabri\game\src\python-automation-tasks\images\avoid.png"
# attack_button = r"C:\Users\Gabri\game\src\python-automation-tasks\images\start.png"
# stop_button = r"C:\Users\Gabri\game\src\python-automation-tasks\images\stop.png"

timeout = 60
middle_screen = 1566,320
attack_button = 1069,51
position_losttower = 1603,486
npc_reset = 1395,185
walk = 1442,270
x, y = 1395,185
count = 0

def start_script():
    # TODO: adds validation if got recent MR or not
    auto_farm('/s15')
    # after_mr('/losttower7')

# def click(nome_janela, x_relativo, y_relativo):
def click():
    pyautogui.click(middle_screen, duration=0.2)
    # hwnd = win32gui.FindWindow(None, nome_janela)
    # if hwnd:
    #     # Obtém as coordenadas da janela
    #     left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #     x_absoluto = left + x_relativo
    #     y_absoluto = top + y_relativo

    #     # Envia um evento de clique para a janela
    #     lParam = win32api.MAKELONG(x_relativo, y_relativo)
    #     win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    #     win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
    #     print(f"Clique virtual realizado em ({x_absoluto}, {y_absoluto}) na janela '{nome_janela}'")
    # else:
    #     print(f"Janela '{nome_janela}' não encontrada.")

def write_message(message):
    pyautogui.hotkey('enter', presses=3, interval=0.2)
    pyautogui.write(message)
    pyautogui.hotkey('enter', presses=3, interval=0.2)

def press_button():
    pyautogui.hotkey('c', presses=3, interval=0.5)

def hold_button(x, y):
    pyautogui.mouseDown(x, y, button='left', duration=0.2)
    pyautogui.mouseUp(x, y, button='left')

def reset():
    print("Resetando...")
    try:
        # click(game, middle_screen[0], middle_screen[1])
        click()
        write_message('/resetar')
        start_time = time()
        while not get_images():
            print(f"Iniciando o loop de reset... start_time: {start_time}, timeout: {timeout}")
            get_images()
            if time() - start_time > timeout:
                print("Timeout atingido, retornando...")
                click_on_confirm()
                break
        return 0
    except KeyboardInterrupt as e:
        print(f"Script encerrado manualmente pelo usuário. {e}")
        return 1 # stops while loop, 0 continues

def farm(location):
    try:
        print("Iniciando farm...")
        start_time = time()
        while not get_images():
            print(f"Iniciando o loop de farm... start_time: {start_time}, timeout: {timeout}")
            get_images()
            if time() - start_time > timeout:
                print("Timeout atingido, retornando...")
                click_on_confirm()
                break
        time_to_sleep = 40
        sleep(1.5)
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
        print(f"Resets: {data['resets']}")
        # write_message('/a 1000')
        write_message('/e 3500')
        write_message('/a 3500')
        write_message('/f 3500')
        write_message('/v 3500')
        return 0
    except KeyboardInterrupt as e:
        print(f"Script encerrado manualmente pelo usuário. {e}")
        return 1 # stops while loop, 0 continues

def stop_attack():
    try:
        pyautogui.click(attack_button, duration=0.2)
    except Exception as e:
        print(f"Erro ao procurar botão de STOP {e}")
        return True
def start_attack():
    try:
        pyautogui.click(attack_button, duration=0.2)
    except Exception as e:
        print(f"Erro ao procurar botão de START {e}")
        return True

def auto_farm(map):
    init_loop(map)

def get_images():
    # click(game, middle_screen[0], middle_screen[1])
    click()
    try:
        text = pytesseract.image_to_string(Image.open(avoid), lang="eng")
        coord_images = pyautogui.locateOnScreen(verify_left_arrow, confidence=0.8)
        if solve_challenge in text.lower() and coord_images:
            rotate_image(verify_left_arrow)
            if not find_correct_image(count):
                return False
            else:
                print("Imagem encontrada...")
                click_on_confirm()
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
        pyautogui.click(pyautogui.center(button), duration=0.2)
    except Exception as e:
        print(f"Erro ao procurar botão de confirmação {e}")
        return True
def rotate_image(image_path):
    if "left_arrow" in image_path:
        button = pyautogui.locateOnScreen(verify_left_arrow, confidence=0.8)
        pyautogui.click(pyautogui.center(button), duration=0.2)

def find_correct_image(count):
    images_to_check = [
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\axe_1.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\bull_1.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\dragon_armor.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\dragon_helmet.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\boots_3.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\boots_1.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\boots_2.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\brass_armor_2.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\iron_shield_1.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\scale_helmet.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\skull_shield.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\sm_armor.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\small_shield.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\sorcerer.png",
        r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\spider.png",
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

def get_data():
    with open(r"C:\Users\Gabri\game\src\python-automation-tasks\database.json", 'r') as file:
        return json.load(file)

def set_data(data):
    with open(r"C:\Users\Gabri\game\src\python-automation-tasks\database.json", 'w') as file:
        json.dump(data, file, indent=4)

def tirar_print_janela(nome_janela, caminho_arquivo):
    #click(game, middle_screen[0], middle_screen[1])
    click()
    janela = gw.getWindowsWithTitle(nome_janela)[0]
    janela.activate()
    print(f"Janela encontrada: {janela.title}")
    x, y = janela.left, janela.top
    largura, altura = janela.width, janela.height

    print(f"Janela encontrada: {janela.title}")
    print(f"Coordenadas: ({x}, {y}), Tamanho: {largura}x{altura}")

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

import win32gui

def verificar_janela_ativa(nome_janela):
    hwnd = win32gui.GetForegroundWindow()
    janela_ativa = win32gui.GetWindowText(hwnd)
    return janela_ativa == nome_janela

def ativar_janela(nome_janela):
    janelas = gw.getWindowsWithTitle(nome_janela)
    if janelas:
        janela = janelas[0]
        janela.activate()
        print(f"Janela '{janela.title}' ativada.")
        if not verificar_janela_ativa(nome_janela):
            print(f"Falha ao ativar a janela '{nome_janela}'.")
    else:
        print(f"Janela '{nome_janela}' não encontrada.")

def init_loop(map):
    while True:
        data_from_reset = reset()
        data_from_farm = farm(map)
        if data_from_farm or data_from_reset > 1:
            break

def enviar_tecla_virtual(nome_janela, tecla):
    hwnd = win32gui.FindWindow(None, nome_janela)
    if hwnd:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, tecla, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, tecla, 0)
        print(f"Tecla '{chr(tecla)}' enviada para a janela '{nome_janela}'")
    else:
        print(f"Janela '{nome_janela}' não encontrada.")

def enviar_texto_virtual(nome_janela, texto):
    for caractere in texto:
        tecla = ord(caractere.upper())
        enviar_tecla_virtual(nome_janela, tecla)
        sleep(0.05)
