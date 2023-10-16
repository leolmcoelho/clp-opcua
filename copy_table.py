import docker
import time
def copy_files():
# Conecta-se ao cliente Docker
    client = docker.from_env()

    while True:
        # Filtra contêineres com base no nome da imagem (ancestor=clp)
        containers = client.containers.list(filters={"ancestor": "clp"})
        
        if containers:
            # Pega o ID do primeiro contêiner da lista
            container_id = containers[0].id
            
            # Copia os arquivos do contêiner para o sistema host
            try:
                client.containers.get(container_id).exec_run(cmd="cp -r /resultados /host_resultados")
                print(f"Arquivos copiados do contêiner {container_id} para /host_resultados")
            except Exception as e:
                print(f"Erro ao copiar arquivos do contêiner: {e}")

        # Espera 1 segundo antes de verificar novamente
        time.sleep(1)
