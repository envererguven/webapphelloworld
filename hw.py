from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'python flask ile ilk web uygulaması, merhaba'

app.run(host='0.0.0.0', port=81)
