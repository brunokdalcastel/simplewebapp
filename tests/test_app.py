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

    def test_404_not_found(self):
        """Testa se uma rota inexistente retorna 404."""
        tester = app.test_client(self)
        response = tester.get('/nonexistent', content_type='html/text')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
