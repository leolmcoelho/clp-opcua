# Use uma imagem Python
FROM python:3.10

# Copie o script Python para o contêiner
COPY teste.py /teste.py

# Defina o diretório de trabalho como /resultados
WORKDIR /
RUN mkdir /resultados

# Execute o script Python quando o contêiner for iniciado
CMD ["python", "/teste.py"]
