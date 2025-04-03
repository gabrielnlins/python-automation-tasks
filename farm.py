from time import time
from get_images import get_images, get_level_reset, get_chat_print, print_muhelper
from farm_utils import *
from data import get_data, set_data
import reset

def farm(location):
    try:
        click()
        start_time = time()
        # sleep(0.5)
        data = get_data()
        if print_muhelper():
            press_enter()
            # farm(location)
        while not get_images():
            print(f"Iniciando o loop de farm... start_time: {start_time}, timeout: {timeout}")
            if time() - start_time > timeout:
                print("Timeout atingido, retornando...")
                data['location'] = location
                set_data(data)
                if get_chat_print():
                    write_message(lorencia)
                    sleep(180)
                sleep(0.5)
                farm(location)
                break
        if data['temporary_reset_count'] > 0 and data['temporary_reset_count'] < 15:
            write_message('/e 3500')
            write_message('/a 3500')
        move_and_attack(location, data)
        press_button()
        print("Farmando...")
        while not get_level_reset():
            if print_muhelper():
                press_enter()
                farm(location)
            sleep(4)
        return reset.reset()
    except KeyboardInterrupt as e:
        print(f"Script encerrado manualmente pelo usuário. {e}")
        return 1 # stops while loop, 0 continues

def move_and_attack(location, data):
    if data['temporary_reset_count'] < 6:
        location = '/losttower7'
    write_message(location)
    if location == '/losttower7':
        hold_button(position_losttower[0], position_losttower[1])
    start_attack()
    set_data(data)
    # if print_muhelper():
    #     farm(location)