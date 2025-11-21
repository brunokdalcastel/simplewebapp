# PyMonitor DevOps

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

Uma aplicação web moderna para monitoramento de sistemas e verificação de conectividade, projetada para demonstrar práticas de DevOps, Containerização e Desenvolvimento Web.

## 🚀 Funcionalidades

- **Dashboard de Recursos**: Monitoramento em tempo real de CPU, Memória e Disco.
- **Stress Test (Novo)**: Simulação de carga de CPU para validar o monitoramento em tempo real.
- **Verificador de Conectividade**: Teste a disponibilidade de sites e APIs externas (HTTP/HTTPS).
- **Histórico de Verificações**: Registro das últimas verificações realizadas (persistência com SQLite).
- **Interface Moderna**: UI responsiva com tema escuro e feedback visual.
- **API REST**: Endpoints JSON para integração com outras ferramentas.

## 🛠️ Tecnologias

- **Backend**: Python, Flask, SQLite, Psutil
- **Frontend**: HTML5, CSS3 (Grid/Flexbox), JavaScript (Fetch API)
- **Infraestrutura**: Docker, Docker Compose
- **CI/CD**: GitHub Actions (Linting, Testes Unitários, Build Docker)

## 📦 Como Executar

### Com Docker (Recomendado)

1.  Clone o repositório:
    ```bash
    git clone https://github.com/brunokdalcastel/simplewebapp.git
    cd simplewebapp
    ```

2.  Suba a aplicação:
    ```bash
    docker-compose up --build
    ```

3.  Acesse em seu navegador: `http://localhost:5000`

### Localmente (Desenvolvimento)

1.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  Execute a aplicação:
    ```bash
    python app.py
    ```

## 🧪 Testes

O projeto inclui uma suíte de testes unitários. Para executar:

```bash
python -m unittest discover tests
```

## 📝 API Endpoints

- `GET /api/stats`: Retorna uso de CPU, Memória e Disco.
- `POST /api/check_url`: Testa uma URL. Body: `{"url": "google.com"}`.
- `GET /api/history`: Retorna histórico de testes.
- `GET /health`: Health check da aplicação.
