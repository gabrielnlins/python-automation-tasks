import pyautogui
import pytesseract
from time import sleep
from PIL import Image
import pygetwindow as gw
import win32gui
import win32api
import win32con

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\tesseract.exe"
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

invalid_response = 'resposta'
game = "MudinhoX"
solve_challenge = 'resolva o desafio'
confirmation_button_path = r"C:\Users\Gabri\game\src\python-automation-tasks\images\confirm_button.png"
verify_left_arrow = r"C:\Users\Gabri\game\src\python-automation-tasks\images\left_arrow_2.png"
avoid = r"C:\Users\Gabri\game\src\python-automation-tasks\images\avoid.png"

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
    r"C:\Users\Gabri\game\src\python-automation-tasks\images_on_format\dragon.png",
]

timeout = 30
middle_screen = 1566,320
attack_button = 1069,51
position_losttower = 1603,486

def click():
    pyautogui.click(middle_screen, duration=0.2)

def write_message(message):
    pyautogui.hotkey('enter', presses=1, interval=0.5)
    pyautogui.write(message)
    pyautogui.hotkey('enter', presses=1, interval=0.5)

def press_button():
    pyautogui.hotkey('c', presses=1, interval=0.5)

def press_esc():
    pyautogui.hotkey('esc', presses=1, interval=0.5)

def hold_button(x, y):
    pyautogui.mouseDown(x, y, button='left', duration=0.5)
    sleep(1)
    pyautogui.mouseDown(x, y, button='left', duration=0.5)
    pyautogui.mouseUp(x, y, button='left')

def stop_attack():
    try:
        pyautogui.click(attack_button, duration=0.5)
    except Exception as e:
        print(f"Erro ao procurar botão de STOP {e}")
        return True
def start_attack():
    try:
        pyautogui.click(attack_button, duration=0.5)
    except Exception as e:
        print(f"Erro ao procurar botão de START {e}")
        return True

def mouse():
    pyautogui.mouseInfo()

def click_on_confirm():
    try:
        sleep(1)
        button = pyautogui.locateOnScreen(confirmation_button_path, confidence=0.8)
        pyautogui.click(pyautogui.center(button), duration=0.15)
        sleep(1.5)
    except Exception as e:
        print(f"Erro ao procurar botão de confirmação {e}")
        return True

def tirar_print_janela(nome_janela, caminho_arquivo):
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
