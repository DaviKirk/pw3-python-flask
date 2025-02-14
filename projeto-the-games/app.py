# pip gerenciador de pacotes do python
# pip install flask
# importando pacote do Flask
from flask import Flask

# carregando o Flask na variável app
app = Flask(__name__)

# criando a rota principal do site
@app.route('/')
# criando função no python
def home():
    return '<h1>Meu primeiro site em Flask, seja bem-vindo!</h1>'

@app.route('/games')
def games():
    return '<h1>Seja Bem vindo a pagina de games</h1>'

if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)