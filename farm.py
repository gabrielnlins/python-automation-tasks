from time import time
from get_images import get_images, get_level_reset
from farm_utils import *
from data import get_data, set_data

def farm(location):
    try:
        click()
        start_time = time()
        sleep(0.5)
        data = get_data()
        while not get_images():
            print(f"Iniciando o loop de farm... start_time: {start_time}, timeout: {timeout}")
            if time() - start_time > timeout:
                print("Timeout atingido, retornando...")
                data['location'] = location
                set_data(data)
                # write_message(location)
                sleep(0.5)
                farm(location)
                # press_button()
                break
        if data['temporary_reset_count'] > 0 and data['temporary_reset_count'] < 15:
            write_message('/e 3500')
            write_message('/a 3500')
        move_and_attack(location, data)
        press_button()
        sleep(0.5)
        while not get_level_reset():
            print("Farmando...")
            sleep(2)
        return 0
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