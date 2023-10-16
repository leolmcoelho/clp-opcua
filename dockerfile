# Use a imagem oficial do Python como a imagem base
FROM python:3.10

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Copie todo o conteúdo do diretório atual para o contêiner no diretório de trabalho
COPY . .

# Expose a porta (se necessário)
EXPOSE 4840

# Defina a pasta "resultados" como um ponto de montagem para um volume
RUN mkdir /resultados
VOLUME /resultados

# Comando padrão a ser executado quando o contêiner for iniciado
# Comando padrão a ser executado quando o contêiner for iniciado

# Dê permissões de execução ao script de inicialização
RUN chmod 777 startup.sh

# Comando padrão a ser executado quando o contêiner for iniciado
# Comando padrão a ser executado quando o contêiner for iniciado
# Use a imagem oficial do Python como a imagem base
FROM python:3.10

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .
COPY teste.py .

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Copie todo o conteúdo do diretório atual para o contêiner no diretório de trabalho
COPY . .

# Expose a porta (se necessário)
EXPOSE 4840


# Comando padrão a ser executado quando o contêiner for iniciado
# Comando padrão a ser executado quando o contêiner for iniciado

# Dê permissões de execução ao script de inicialização
#RUN chmod 777 startup.sh

# Comando padrão a ser executado quando o contêiner for iniciado
# Comando padrão a ser executado quando o contêiner for iniciado
RUN python teste.py

CMD ["py", "control_CLP.py"]
