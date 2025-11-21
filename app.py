import os
import sqlite3
import time
import psutil
import requests
from flask import Flask, render_template, jsonify, request, g

app = Flask(__name__)
DATABASE = 'monitor.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS checks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                status_code INTEGER,
                response_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()

# Inicializa o DB na primeira execução
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))
    
    return jsonify({
        'cpu': cpu_percent,
        'memory': {
            'total': memory.total,
            'available': memory.available,
            'percent': memory.percent
        },
        'disk': {
            'total': disk.total,
            'free': disk.free,
            'percent': disk.percent
        }
    })

@app.route('/api/check_url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
        
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        duration = time.time() - start_time
        
        status_code = response.status_code
        
        # Salvar no DB
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO checks (url, status_code, response_time) VALUES (?, ?, ?)',
                       (url, status_code, duration))
        db.commit()
        
        return jsonify({
            'url': url,
            'status': 'up' if status_code < 400 else 'down',
            'status_code': status_code,
            'time': f"{duration:.2f}s"
        })
        
    except requests.RequestException as e:
        return jsonify({
            'url': url,
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/history')
def history():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM checks ORDER BY timestamp DESC LIMIT 10')
    rows = cursor.fetchall()
    
    history_data = []
    for row in rows:
        history_data.append({
            'url': row['url'],
            'status_code': row['status_code'],
            'response_time': f"{row['response_time']:.2f}s",
            'timestamp': row['timestamp']
        })
        
    return jsonify(history_data)

import threading

# ... (imports existentes)

@app.route('/api/stress', methods=['POST'])
def stress_cpu():
    duration = 5  # segundos
    
    def run_stress():
        end_time = time.time() + duration
        while time.time() < end_time:
            # Realiza cálculos matemáticos intensivos para consumir CPU
            _ = [x**2 for x in range(10000)]
            
    # Roda em uma thread separada para não bloquear o servidor
    thread = threading.Thread(target=run_stress)
    thread.start()
    
    return jsonify({'status': 'started', 'message': f'Generating CPU load for {duration} seconds'})

@app.route('/health')
def health_check():
    return jsonify(status="ok", message="Application is healthy")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
