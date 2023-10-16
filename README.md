# Guia de Uso do Docker e WSL para Executar o Comando

Neste guia, vamos explicar como executar o comando Docker e, antes disso, como instalar o Docker e o Windows Subsystem for Linux (WSL) no seu sistema.


## Instalando o Windows Subsystem for Linux (WSL)

O Windows Subsystem for Linux (WSL) permite que você execute distribuições Linux em um ambiente Windows. Para instalá-lo, siga as etapas abaixo:

1. Abra o PowerShell ou o Prompt de Comando como administrador.

2. Execute o seguinte comando para habilitar o recurso WSL:

```bash
wsl --install
```

3. Reinicie o computador quando solicitado.

4. Após a reinicialização, abra a Microsoft Store e procure por uma distribuição Linux de sua escolha, como o Ubuntu. Baixe e instale a distribuição.

5. Siga as instruções na tela para criar uma conta de usuário e senha.

## Instalando o Docker

O Docker é uma plataforma que permite empacotar, distribuir e executar aplicativos em contêineres. Para instalar o Docker no seu sistema, siga as etapas abaixo:

### Windows

1. Certifique-se de que você esteja usando uma versão do Windows que suporte o Docker, como Windows 10 Pro, Enterprise ou Education. Você também deve ter o Windows 11.
2. Baixe o instalador do Docker Desktop para Windows em [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).
3. Execute o instalador e siga as instruções na tela para concluir a instalação.
4. Após a instalação, inicie o Docker Desktop.

### Linux

No Linux, a instalação do Docker varia de acordo com a distribuição. Abaixo estão alguns comandos genéricos que você pode usar, mas consulte a documentação oficial do Docker para obter instruções específicas para a sua distribuição:

#### Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install docker-ce
```

#### CentOS/Fedora:

```bash
sudo yum install docker-ce
```


Agora que você tem o Docker e o WSL instalados, você pode executar o comando Docker fornecido.

## Executando o Comando Docker

O comando Docker que você mencionou:

```bash
docker run -d -v ${PWD}/resultados:/resultados clp
```

Isso irá executar um contêiner Docker baseado na imagem chamada "clp" em segundo plano. O contêiner compartilhará uma pasta local chamada "resultados" com o contêiner em "/resultados".

Lembre-se de que você deve substituir "clp" pelo nome da imagem do contêiner que deseja executar e garantir que a imagem esteja disponível localmente ou em um registro de contêiner (como Docker Hub).

Certifique-se de estar no diretório onde deseja criar a pasta "resultados" ou ajuste o caminho de montagem de acordo com o local desejado.

Execute o comando no terminal WSL para iniciar o contêiner. Você agora tem o Docker e o WSL configurados e pode usar contêineres para isolar suas aplicações e ambientes de desenvolvimento.