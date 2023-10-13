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
EXPOSE 4840

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "control_CLP.py"]
