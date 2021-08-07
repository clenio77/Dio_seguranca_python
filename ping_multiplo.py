import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 60)
        # se for windows use -n
        os.system('ping -c 6 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)