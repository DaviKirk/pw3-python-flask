# pip gerenciador de pacotes do python
# pip install flask
# importando pacote do Flask
from flask import Flask, render_template

# carregando o Flask na variável app
app = Flask(__name__, template_folder="views")

# criando a rota principal do site


@app.route('/')
# criando função no python
# view function - Função de visualização
def home():

    return render_template('index.html',)


@app.route('/games')
def games():

    game = {'Título': 'My summer car',
            'Ano': 2016,
            'categoria': 'Mundo Aberto'}

    jogadores = ["Mc Rodolfinho", "davi_lambari",
                 "juju_do_pix", "suaIrmã", "edsonGf"]


    return render_template('games.html',
                       game=game,
                       jogadores=jogadores
                       )

if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
