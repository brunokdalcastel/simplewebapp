# Importa a classe Flask do pacote flask. A classe Flask é o componente central de qualquer aplicação web com Flask.
from flask import Flask, jsonify

# Cria uma instância da aplicação Flask.
# A variável `__name__` é uma variável especial em Python que contém o nome do módulo atual.
# O Flask utiliza essa informação para saber onde procurar por recursos como templates e arquivos estáticos.
app = Flask(__name__)

# Define uma rota para a URL raiz ('/').
# O decorator `@app.route()` é usado para associar uma URL a uma função específica.
# Quando um usuário acessa a URL raiz do site (ex: http://seusite.com/), a função `hello()` será executada.
@app.route('/')
def hello():
    # Esta é a "view function", a função que responde à requisição para a URL definida na rota.
    # Ela retorna a string que será exibida como resposta no navegador do usuário.
    return "Hello, World from a Docker container!"

@app.route('/health')
def health_check():
    """
    Endpoint de verificação de saúde.
    Retorna o status da aplicação em formato JSON.
    """
    return jsonify(status="ok", message="Application is healthy")

# Este bloco condicional verifica se o script está sendo executado diretamente pelo interpretador Python.
# Se o arquivo for importado como um módulo em outro script, este bloco não será executado.
# É uma boa prática para garantir que o servidor de desenvolvimento só rode quando o arquivo é o ponto de entrada principal.
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento web embutido no Flask.
    # O método `app.run()` coloca a aplicação no ar.
    # `debug=True`: Ativa o modo de depuração. Com isso, o servidor reinicia automaticamente a cada alteração no código
    # e exibe páginas de erro detalhadas caso algo dê errado.
    # `host='0.0.0.0'`: Faz com que o servidor escute em todas as interfaces de rede públicas.
    # Isso é crucial para que a aplicação, rodando dentro de um contêiner Docker, possa ser acessada a partir do seu computador (o "host").
    app.run(debug=True, host='0.0.0.0')

# Adicionando um comentário para testar o trigger da pipeline de CI.
