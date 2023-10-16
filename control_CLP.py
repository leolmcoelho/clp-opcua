import json
from time import sleep
from opcua import Client, ua
from save_data import *
from datetime import datetime

import docker
import time


# Abrir o arquivo JSON
with open('config.json', 'r') as arquivo_json:
    # Carregar o conteúdo do arquivo JSON
    dados = json.load(arquivo_json)

HOST = dados['host']
BASE = dados['BASE_NAME']
TAGS = dados['TAGS']
PATH = dados['PATH']
EXPORT = dados['EXPORT']
FILE_NAME = dados['FILE_NAME']


def get_node_value(name):
    var_node = cliente.get_node(f'{BASE}.{name.upper()}')
    return var_node.get_value()


def get_all_data():
    data = {}
    for tag in TAGS:
        var_node = cliente.get_node(f'{BASE}.{tag}')
        value = var_node.get_value()
        data[tag] = value
    data['DATA HORA'] = datetime.now()
    # print(data)
    return createDF(data)


def set_node_value(name, new_value):
    var_node = cliente.get_node(f'{BASE}.{name.upper()}')
    var_node.set_value(new_value)


# Crie um cliente OPC UA
cliente = Client(HOST)

try:
    # Conecte-se ao servidor
    cliente.connect()

    print("Conectado ao servidor OPC UA")
    # set_node_value("save_values", True)

    while True:
        if get_node_value('SAVE_VALUES'):
            data = get_all_data()
            # print(data)
            if EXPORT == 'xlsx':
                export_to_xlsx(data, PATH, FILE_NAME, TAGS)
            if EXPORT == 'csv':
                export_to_csv(data, PATH, FILE_NAME, TAGS)

            set_node_value("RESET_SAVE", True)
            sleep(2)
            set_node_value("RESET_SAVE", False)

        else:
            sleep(dados['delay'])
            print('sem valor')
            set_node_value("save_values", True)


finally:
    # Certifique-se de sempre fechar a conexão quando terminar
    cliente.disconnect()
    print("Conexão encerrada")
