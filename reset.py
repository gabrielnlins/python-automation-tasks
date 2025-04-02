from farm_utils import *
from get_images import get_images, get_level_reset
from data import get_data, set_data
from master_reset import dar_mr
from time import time, sleep

def reset():
    try:
        data = get_data()
        click()
        start_time = time()
        while not get_images():
            print(f"Iniciando o loop de reset... start_time: {start_time}, timeout: {timeout}")
            if time() - start_time > timeout:
                print("Timeout atingido, retornando...")
                # write_message(data['location'])
                reset()
                # press_button()
                sleep(0.5)
                break
        if get_level_reset():
            write_message('/resetar')
            print("Resetando...")
            data['temporary_reset_count'] += 1
            data['resets'] += 1
            # data['is_already_farming'] = 0
            set_data(data)
            print(f"Resets: {data['resets']}. Contagem temporária de resets: {data['temporary_reset_count']}")
            if data['temporary_reset_count'] >= 30: 
                dar_mr(data)
        return 0
    except KeyboardInterrupt as e:
        print(f"Script encerrado manualmente pelo usuário. {e}")
        return 1 # stops while loop, 0 continues
