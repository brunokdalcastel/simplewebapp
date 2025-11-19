# Aplicação Web Simples

Esta é uma aplicação web simples "Hello, World" construída com Flask e conteinerizada com Docker.

## Começando

Estas instruções permitirão que você obtenha uma cópia do projeto em execução em sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

- Python 3.8 ou posterior
- Docker

### Instalação

1. Clone o repositório
   ```sh
   git clone https://github.com/seu_usuario/simple-web-app.git
   ```
2. Instale os pacotes Python
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Para executar a aplicação sem Docker:

```sh
python app.py
```

A aplicação estará disponível em `http://localhost:5000`.

## Docker

### Construindo a imagem

```sh
docker build -t simple-web-app .
```

### Executando o contêiner

```sh
docker run -p 5000:5000 simple-web-app
```

### Usando o Docker Compose

Para construir e executar a aplicação com o Docker Compose:

```sh
docker-compose up
```

A aplicação estará disponível em `http://localhost:5000`.

## Pipeline de CI

O projeto utiliza um pipeline de CI com GitHub Actions. O pipeline é acionado em cada push ou pull request para a branch `master`.

O pipeline executa as seguintes etapas:
1. Configura o ambiente Python.
2. Instala as dependências.
3. Executa os testes automatizados.
4. Constrói a imagem Docker se os testes passarem.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
