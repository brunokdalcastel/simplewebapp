import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    def test_home(self):
        """Testa a rota principal."""
        # Cria um cliente de teste
        tester = app.test_client(self)
        
        # Faz uma requisição GET para a rota '/'
        response = tester.get('/', content_type='html/text')
        
        # Verifica se o status da resposta é 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o conteúdo da resposta contém a string esperada
        self.assertTrue(b'Hello, World from a Docker container!' in response.data)

if __name__ == '__main__':
    unittest.main()
