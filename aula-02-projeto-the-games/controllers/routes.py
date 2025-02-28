from flask import render_template


def init_app(app):

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
