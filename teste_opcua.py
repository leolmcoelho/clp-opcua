import opcua
import time
from opcua import Client, ua

# Endereço do servidor
servidor = Client("opc.tcp://192.200.2.5:4840")

# Conectando ao servidor
servidor.connect()
print("Servidor Conectado!")
print("\n")

# Lendo o namespace do servidor
print("Namespace URI do servidor:\n", servidor.get_namespace_array())
print("\n")

# Lendo uma variável INT global do servidor
value = 0
var_node = servidor.get_node("ns=4;s=|var|ecomatDisplay/7/Touch.Application.GVL_OPC.TAG_RFID")
var = var_node.get_value()
print("Valor da variável:", var)

# Novo valor da variável INT global do servidor
# new_value = 58
# print("Valor atribuído:\n", new_value)
# dv = ua.DataValue(ua.Variant(new_value, ua.VariantType.Int16))
# var_node.set_value(dv)

# Lendo novo variável INT global do servidor
# var_node = servidor.get_node("ns=4;s=|var|ecomatDisplay/7/Touch.Application.GVL_VAR.test_int")
# var = var_node.get_value()
# print("Valor atualizado da variável:\n", var)

####
print("\n")
print("\n")
TAGS = [
'PRODUTOR',
'CULTIVAR',
'LOTE',
'CATEGORIA',
'PENEIRA',
'NUM_AMOSTRA',
'QNT_SEMENTES',
'PESO_AMOSTR',
'PMS_AMOSTR',
'PESO_BAG']


for tag in TAGS:
    var_node = servidor.get_node(f'ns=4;s=|var|ecomatDisplay/7"/Touch.Application.GVL_OPC.{tag}')

    var = var_node.get_value()
    print("Valor da variável:", var)


# Lendo uma variável BOOL global do servidor
# var_node = servidor.get_node("|var|ecomatDisplay/7/Touch.Application.GVL_OPC.TESTE2")
# var = var_node.get_value()
# print("Valor da variável:\n", var)

# Novo valor da variável BOOL global do servidor
# new_value = 0
# print("Valor atribuído:\n", new_value)
# dv = ua.DataValue(ua.Variant(new_value, ua.VariantType.Boolean))
# var_node.set_value(dv)

# Lendo novo variável BOOL global do servidor
# var_node = servidor.get_node("ns=4;s=|var|ecomatDisplay/7/Touch.Application.GVL_VAR.test_bool")
# var = var_node.get_value()
# print("Valor atualizado da variável:\n", var)

# while True:
#    print("Valor da variável:\n", value)
#    time.sleep(1)

# Desconectando do servidor
# servidor.disconnect()
