from opcua import Client

# Endereço do servidor OPC UA
server_endpoint = "opc.tcp://localhost:4840"  # Substitua pelo endereço do seu servidor OPC UA

# Crie um cliente OPC UA
client = Client(server_endpoint)

try:
    # Conecte-se ao servidor
    client.connect()

    # Acesse a variável no servidor
    produtor = client.get_node("ns=2;s=|var|ecomatDisplay/7/Touch.Application.GVL_OPC.PRODUTOR")

    # Defina um novo valor para a variável (certifique-se de que a variável permita escrita)
    novo_valor = "Novo Valor do Produtor"
    produtor.set_value(novo_valor)

    # Confirme que o valor foi definido com sucesso
    valor_atual = produtor.get_value()
    print(f"Valor de PRODUTOR definido como: {valor_atual}")

finally:
    # Certifique-se de sempre fechar a conexão quando terminar
    client.disconnect()
    print("Conexão encerrada")
