from flask import Flask
import os

app = Flask(__name__)

from app import routes

if __name__ == "__main__":
    app.run()

if __name__ == 'main' :
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)