import unittest
import json
from unittest.mock import patch, MagicMock
from app import app, init_db

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        # Usa um banco de dados em memória para testes
        app.config['DATABASE'] = ':memory:'
        self.tester = app.test_client(self)
        
        # Inicializa o DB (embora o app.py use 'monitor.db' hardcoded, 
        # para testes ideais deveríamos refatorar o app.py para aceitar config de DB.
        # Como não refatoramos isso, o teste vai criar um arquivo monitor.db localmente ou usar o existente.
        # Para simplificar e não alterar muito o app.py agora, vamos deixar assim, 
        # mas em produção idealmente injetariamos a config do DB.
        # O init_db() roda no import, então o arquivo já existe.
        pass

    def test_home(self):
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'DevOps System Monitor' in response.data)

    def test_health_check(self):
        response = self.tester.get('/health', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'ok')

    @patch('app.psutil')
    def test_api_stats(self, mock_psutil):
        # Configura mocks para psutil
        mock_psutil.cpu_percent.return_value = 50.0
        
        mock_memory = MagicMock()
        mock_memory.total = 8000000000
        mock_memory.available = 4000000000
        mock_memory.percent = 50.0
        mock_psutil.virtual_memory.return_value = mock_memory
        
        mock_disk = MagicMock()
        mock_disk.total = 100000000000
        mock_disk.free = 50000000000
        mock_disk.percent = 50.0
        mock_psutil.disk_usage.return_value = mock_disk

        response = self.tester.get('/api/stats', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('cpu', data)
        self.assertIn('memory', data)
        self.assertIn('disk', data)
        self.assertEqual(data['cpu'], 50.0)

    @patch('requests.get')
    def test_check_url_success(self, mock_get):
        # Mock da resposta do requests
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        payload = {'url': 'http://google.com'}
        response = self.tester.post('/api/check_url', 
                                  data=json.dumps(payload), 
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'up')
        self.assertEqual(data['status_code'], 200)

    @patch('requests.get')
    def test_check_url_failure(self, mock_get):
        # Mock de erro
        import requests
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")

        payload = {'url': 'http://invalid-url.com'}
        response = self.tester.post('/api/check_url', 
                                  data=json.dumps(payload), 
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')

if __name__ == '__main__':
    unittest.main()
