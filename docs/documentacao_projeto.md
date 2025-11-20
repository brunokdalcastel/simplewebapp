# Diário de Bordo - Simple Web App

Este documento serve como um diário de bordo para o desenvolvimento do projeto "Simple Web App", detalhando desde a criação da aplicação até a sua automação com Docker e GitHub Actions.

## 1. Visão Geral do Projeto

O objetivo deste projeto é criar uma aplicação web simples utilizando Flask, containerizá-la com Docker e configurar uma pipeline de Integração Contínua (CI) para automatizar o processo de build e teste a cada alteração no código.

## 2. A Aplicação Web (`app.py`)

A base do projeto é uma aplicação web minimalista desenvolvida em Python com o framework Flask.

- **`app.py`**: Este arquivo contém o código-fonte da aplicação. Ele cria um servidor web que, ao ser acessado na rota principal (`/`), retorna a mensagem "Hello, World from a Docker container!". O código é extensivamente comentado para explicar cada parte do processo, desde a importação do Flask até a execução do servidor de desenvolvimento.
- **`requirements.txt`**: Lista as dependências Python do projeto, que neste caso é apenas o `Flask`.

A aplicação foi projetada para rodar em modo de depuração, escutando em todas as interfaces de rede (`host='0.0.0.0'`), o que é essencial para que ela seja acessível de fora do contêiner Docker.

## 3. Dockerização

Para garantir que a aplicação rode de forma consistente em qualquer ambiente, utilizamos o Docker para containerizá-la.

### 3.1. `Dockerfile`

O `Dockerfile` é a "receita" para construir a imagem Docker da nossa aplicação. Ele executa os seguintes passos:
1.  **`FROM python:3.8-slim`**: Usa uma imagem base leve do Python, o que resulta em uma imagem final menor e mais eficiente.
2.  **`WORKDIR /app`**: Define o diretório de trabalho padrão dentro do contêiner como `/app`. Todas as operações subsequentes serão executadas neste diretório.
3.  **`COPY . /app`**: Copia todos os arquivos do projeto do diretório local para o diretório `/app` dentro do contêiner.
4.  **`RUN pip install -r requirements.txt`**: Instala as dependências Python listadas no `requirements.txt` utilizando o `pip`.
5.  **`EXPOSE 5000`**: Informa que o contêiner expõe a porta 5000. Isso não publica a porta, mas serve como documentação para o usuário que for executar o contêiner.
6.  **`CMD ["python", "app.py"]`**: Define o comando que será executado quando o contêiner iniciar, que neste caso é o comando para iniciar a aplicação Flask.

### 3.2. `docker-compose.yml`

Para facilitar a orquestração e execução do contêiner, criamos um arquivo `docker-compose.yml`.
- Ele define um serviço chamado `web`.
- **`build: .`**: Instrui o Docker Compose a construir a imagem a partir do `Dockerfile` no diretório atual.
- **`ports: ["5000:5000"]`**: Mapeia a porta 5000 do contêiner para a porta 5000 da máquina host, permitindo o acesso à aplicação pelo navegador através de `http://localhost:5000`.
- **`volumes: [- .:/app]`**: Cria um "volume", que espelha o diretório do projeto na máquina host para o diretório `/app` dentro do contêiner. Isso permite que alterações no código sejam refletidas instantaneamente na aplicação sem a necessidade de reconstruir a imagem, agilizando o desenvolvimento.

## 4. Controle de Versão com Git

O código-fonte foi versionado com Git e hospedado no GitHub. Os seguintes passos foram executados no terminal (via WSL):

1.  **`git init`**: Inicializou um novo repositório Git no diretório do projeto.
2.  **Configuração de identidade**: Foram configurados o nome de usuário e o e-mail para os commits.
    ```bash
    git config --global user.name "seu-nome"
    git config --global user.email "seu-email@example.com"
    ```
3.  **Primeiro Commit**: Todos os arquivos do projeto foram adicionados e comitados.
    ```bash
    git add .
    git commit -m "Commit inicial"
    ```
4.  **Conexão com Repositório Remoto**: O repositório local foi conectado a um repositório criado no GitHub (`https://github.com/brunokdalcastel/simplewebapp`).
5.  **Push para o GitHub**: O código foi enviado para o GitHub, utilizando um Token de Acesso Pessoal para autenticação, já que a autenticação por senha foi descontinuada.
    ```bash
    git push -u origin master
    ```

## 5. Testes Automatizados



Para garantir a qualidade e a estabilidade da aplicação, foram criados testes automatizados utilizando o módulo nativo `unittest` do Python.



### 5.1. Estrutura de Testes (`tests/test_app.py`)



Foi criado um diretório `tests` na raiz do projeto para abrigar os arquivos de teste.



- **`tests/test_app.py`**: Este arquivo contém o primeiro caso de teste para a nossa aplicação.

    1.  **`import unittest` e `from app import app`**: Importa as bibliotecas necessárias, incluindo a instância da aplicação Flask.

    2.  **`class BasicTestCase(unittest.TestCase)`**: Define uma classe de teste que herda de `unittest.TestCase`.

    3.  **`def test_home(self)`**: Define um método de teste.

        - **`tester = app.test_client(self)`**: Cria um "cliente de teste" que permite simular requisições à aplicação sem a necessidade de um servidor web rodando.

        - **`response = tester.get('/', ...)`**: Envia uma requisição `GET` para a rota principal (`/`).

        - **`self.assertEqual(response.status_code, 200)`**: Verifica se o código de status da resposta é `200 OK`, indicando que a requisição foi bem-sucedida.

        - **`self.assertTrue(b'Hello, World...' in response.data)`**: Verifica se o corpo da resposta contém a mensagem esperada, garantindo que a rota está retornando o conteúdo correto.



## 6. Pipeline de Integração Contínua (CI) com GitHub Actions



A pipeline de CI, definida em `.github/workflows/ci.yml`, foi atualizada para incorporar a execução dos testes automatizados.



O workflow continua sendo acionado a cada `push` ou `pull_request` e executa os seguintes passos em ordem:

1.  **`actions/checkout@v3`**: Faz o checkout do código.
2.  **`actions/setup-python@v3`**: Configura o ambiente Python.
3.  **`Install dependencies`**: Instala as dependências do `requirements.txt`.
4.  **`Lint with flake8`**: **Novo passo!** Executa a verificação estática de código (Linting) para garantir que o código siga os padrões de estilo (PEP 8) e não contenha erros de sintaxe.
5.  **`Run tests`**: Executa os testes automatizados com o comando `python -m unittest discover tests`. O `discover` encontra e executa automaticamente todos os testes no diretório `tests`. Se algum teste falhar, a pipeline é interrompida aqui, impedindo que código com problemas avance.
6.  **`Build Docker image`**: Se os testes passarem, o workflow prossegue para construir a imagem Docker. Este passo agora serve como uma validação final de que a aplicação, já testada, também pode ser empacotada corretamente.

Esta atualização garante que qualquer alteração no código seja automaticamente verificada e testada, aumentando a confiança de que novas mudanças não quebrarão a funcionalidade existente nem introduzirão código fora do padrão.

## 7. Configuração do Ambiente de Desenvolvimento Local

Para garantir que os testes e o desenvolvimento local não interfiram no sistema operacional principal, configuramos um ambiente virtual Python (`venv`).

1.  **Instalação do `venv`**: O pacote `python3.12-venv` foi instalado no WSL (Ubuntu) para permitir a criação de ambientes virtuais.
    ```bash
    sudo apt install python3.12-venv
    ```
2.  **Criação do Ambiente Virtual**: Um ambiente virtual chamado `venv` foi criado na raiz do projeto.
    ```bash
    python3 -m venv venv
    ```
3.  **Ativação do Ambiente**: O ambiente foi ativado. No WSL, o comando é:
    ```bash
    source venv/bin/activate
    ```
    Após a ativação, o prompt do terminal exibe `(venv)`, indicando que o ambiente virtual está ativo.

4.  **Instalação de Dependências**: Com o ambiente ativo, o `pip` foi usado para instalar as dependências do projeto de forma isolada.
    ```bash
    pip install -r requirements.txt
    ```
5.  **Execução dos Testes**: Os testes foram executados novamente, desta vez usando o interpretador Python e as bibliotecas do ambiente virtual, garantindo um resultado bem-sucedido e consistente.
    ```bash
    python3 -m unittest discover tests
    ```

## 8. Adição do Endpoint de Health Check

Para facilitar o monitoramento da saúde da aplicação, especialmente em ambientes orquestrados, foi adicionado um endpoint `/health`.

- **`app.py`**: Uma nova rota `/health` foi criada. Ela retorna uma resposta JSON `{"status": "ok"}` e um código de status `200 OK`.
- **`tests/test_app.py`**: Um novo teste, `test_health_check`, foi adicionado para garantir que o endpoint `/health` está funcionando como esperado, verificando o status da resposta e o conteúdo JSON.

## 9. Comandos Linux Utilizados



Durante o processo de desenvolvimento e configuração, os seguintes comandos foram utilizados no terminal:



- `git init`: Para inicializar o repositório Git.

- `git config --global user.name "..."`: Para configurar o nome de usuário do Git.

- `git config --global user.email "..."`: Para configurar o e-mail do Git.

- `git add .`: Para adicionar todos os arquivos ao stage do Git.

- `git commit -m "..."`: Para criar um commit com uma mensagem.

- `git push -u origin master`: Para enviar os commits para o repositório remoto no GitHub.

- `python -m unittest discover tests`: Para executar os testes localmente.



## 9. Como Executar a Aplicação



Para executar a aplicação localmente, siga os passos abaixo:



1.  Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2.  Clone o repositório do GitHub.

3.  Navegue até o diretório do projeto no terminal.

4.  Execute o comando:

    ```bash

    docker-compose up

    ```

5.  Acesse a aplicação em seu navegador no endereço `http://localhost:5000`.