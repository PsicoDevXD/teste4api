import os
from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from api.app import app as flask_app  # Importe a aplicação Flask principal

app = Flask(__name__)
CORS(app)  # Habilita o CORS para todas as rotas na aplicação Flask

# Use o middleware ProxyFix para lidar com headers de proxy corretamente
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
