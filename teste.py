import datetime, time

for _ in range(50):
# Obtém a hora atual
    hora_atual = datetime.datetime.now()

    # Formata a hora como uma string
    hora_formatada = hora_atual.strftime("%Y-%m-%d %H:%M:%S")

    # Nome do arquivo de texto
    nome_arquivo = "/resultados/hora.txt"


# Abre o arquivo para escrever a hora
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(hora_formatada)

    print(f"Hora escrita em {nome_arquivo}")
    time.sleep(1)