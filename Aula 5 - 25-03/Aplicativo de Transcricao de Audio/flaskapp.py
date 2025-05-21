from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, mundo! Este é o Flask rodando no venv.'

if __name__ == '__main__':
    app.run(debug=True)