from farm_utils import auto_farm
import win32gui
import win32api
import win32con
from time import sleep

# start_script()
auto_farm('/s15')
# auto_farm('/losttower7')


# def enviar_tecla_virtual(nome_janela, tecla):
#     hwnd = win32gui.FindWindow(None, nome_janela)
#     if hwnd:
#         win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, tecla, 0)
#         win32api.SendMessage(hwnd, win32con.WM_KEYUP, tecla, 0)
#         print(f"Tecla '{chr(tecla)}' enviada para a janela '{nome_janela}'")
#     else:
#         print(f"Janela '{nome_janela}' não encontrada.")

# def enviar_texto_virtual(nome_janela, texto):
#     for caractere in texto:
#         tecla = ord(caractere.upper())
#         enviar_tecla_virtual(nome_janela, tecla)
#         sleep(0.05)  # Pequeno atraso entre as teclas

# def enviar_texto_virtual(nome_janela, texto):
#     special_keys = {
#         " ": 0x20,  # Espaço
#         "\n": 0x0D,  # Enter
#     }
#     for caractere in texto:
#         if caractere in special_keys:
#             tecla = special_keys[caractere]
#         else:
#             tecla = ord(caractere.upper())
#         enviar_tecla_virtual(nome_janela, tecla)
#         sleep(0.05)  # Pequeno atraso entre as teclas

# # Exemplo de uso
# # enviar_texto_virtual("MudinhoX", "hello world")
# enviar_tecla_virtual("MudinhoX", 0x0D)  # Enter
# enviar_texto_virtual("MudinhoX", "c")

