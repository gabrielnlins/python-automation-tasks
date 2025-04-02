
from farm_utils import write_message
from data import set_data
from time import sleep
import pyautogui

def dar_mr(data):
    write_message('/a 10000')
    sleep(0.5)
    write_message('/f 31267')
    sleep(0.5)
    write_message('/v 31267')
    sleep(0.5)
    pyautogui.hotkey('enter', presses=1, interval=0.5)
    pyautogui.write('/darmr')
    pyautogui.hotkey('enter', presses=1, interval=0.5)
    sleep(10)
    pyautogui.hotkey('enter', presses=1, interval=0.5)
    data['temporary_reset_count'] = 0
    set_data(data)
