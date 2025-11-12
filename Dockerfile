# Use a imagem oficial do Python como imagem base
FROM python:3.8-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o diretório atual para o contêiner em /app
COPY . /app

# Instale as dependências necessárias
RUN pip install -r requirements.txt

# Exponha a porta 5000 para o mundo exterior
EXPOSE 5000

# Execute o app.py quando o contêiner for iniciado
CMD ["python", "app.py"]