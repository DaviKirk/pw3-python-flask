from flask import render_template, request

jogadores = ["Mc Rodolfinho", "davi_lambari",
             "juju_do_pix", "suaIrmã", "edsonGf"]

gameList = [{'Título': 'My summer car',
             'Ano': 2016,
             'Categoria': 'Mundo Aberto'}
        ]

consoleList = [{'Nome' : 'Xbox360',
                'Valor' : '350,69',
                'País' : 'EUA'}
               ]


def init_app(app):

    # criando a rota principal do site

    @app.route('/')
    # criando função no python
    # view function - Função de visualização
    def home():

        return render_template('index.html',)

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        #acessando o primeiro jogo da lista de jogos
        game = gameList[0]
        if request.method == 'POST':
            if request.form.get('jogador'): #name do input
                jogadores.append(request.form.get('jogador'))
                
        return render_template('games.html' ,
                                game = game ,
                                jogadores=jogadores
                                )
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gameList.append({'Título': request.form.get('titulo'),
                                 'Ano' : request.form.get('ano'),
                                 'Categoria' : request.form.get('categoria')})
        return render_template('cadgames.html',
                               gameList=gameList)
        
    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('pais') and request.form.get('valor'):
                consoleList.append({'Nome' : request.form.get('nome'),
                                    'Valor' : request.form.get('valor'),
                                    'País' : request.form.get('pais')})
        return render_template('cadconsoles.html',
                            consoleList=consoleList)
    

      
