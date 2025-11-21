# Use a imagem oficial do Python como imagem base
FROM python:3.8-slim

# Instala dependências de sistema necessárias para psutil e outros pacotes
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Configurações de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Cria um usuário não-root para rodar a aplicação
RUN useradd -m myuser

# Copie o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instale as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Muda a propriedade dos arquivos para o novo usuário
RUN chown -R myuser:myuser /app

# Muda para o usuário não-root
USER myuser

# Exponha a porta 5000 para o mundo exterior
EXPOSE 5000

# Execute o gunicorn quando o contêiner for iniciado
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]