from opcua import Server

# Crie um servidor OPC UA
server = Server()

# Configurar o Modelo de Informação (nós, variáveis, objetos, etc.)
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")  # Defina o endpoint adequado

# Inicialize o servidor
server.start()

# Escolha um namespace exclusivo
my_namespace = server.register_namespace("http://example.org/my-namespace")

# Adicione um objeto raiz
root = server.nodes.objects.add_object(nodeid=f"ns={my_namespace};s=MyObject", bname="MyObject")

# Adicione variáveis ao objeto com NodeIds exclusivos
var_names = [
    "PRODUTOR",
    "CULTIVAR",
    "LOTE",
    "CATEGORIA",
    "PENEIRA",
    "NUM_AMOSTRA",
    "QNT_SEMENTES",
    "PESO_AMOSTR",
    "PMS_AMOSTR",
    "PESO_BAG",
]

for var_name in var_names:
    variable = root.add_variable(f"ns={my_namespace};s={var_name}", var_name, 0.0)
    variable.set_writable()  # Permite escrita na variável

try:
    while True:
        pass
except KeyboardInterrupt:
    server.stop()
