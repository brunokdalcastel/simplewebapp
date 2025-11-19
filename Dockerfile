# Use a imagem oficial do Python como imagem base
FROM python:3.8-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instale as dependências necessárias
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta 5000 para o mundo exterior
EXPOSE 5000

# Execute o app.py quando o contêiner for iniciado
CMD ["python", "app.py"]