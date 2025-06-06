from flask import render_template, request, redirect, url_for
from models.database import Game, db

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
        
      # Rota Crud (Estoque de jogos)
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        #se o Id for passado, então é para excluir o jogo
        if id:
            # Deletando o jogo do banco
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        if request.method == 'POST':
            # Cadastro de jogos no banco
            newGame = Game(request.form.get('titulo'),
                            request.form.get('ano'),
                            request.form.get('categoria'), request.form.get('plataforma'), request.form.get('preco'))
            # Adicionando o jogo no banco
            db.session.add(newGame)
            db.session.commit()
            return redirect(url_for('estoque'))
        # ORM que estamos usnado é o SQLAlchemy
        # O método query.all = SELECT * FROM games
        gamesEmEstoque = Game.query.all()
        return render_template('estoque.html', gamesEmEstoque=gamesEmEstoque)
        
    @app.route('/edit/<int:id>', methods=['GET','POST'])
    def edit(id):
        g = Game.query.get(id)
        #Edita o jogo com as informações do formulário
        if request.method == 'POST':
            g.titulo = request.form['titulo']
            g.ano = request.form['ano']
            g.categoria = request.form['categoria']
            g.plataforma = request.form['plataforma']
            g.preco = request.form['preco']
            # g.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoque'))
        else:
            # Captura o valor de 'page' que foi passado pelo método GET
            # Define como padrão o valor 1 e o tipo inteiro
            page = request.args.get('page', 1, type=int)
            # Valor padrão de registros por página informada(page)
            per_page = 3
            # Faz um SELECT no banco a partir da pagina informada(page)
            # filtrando os registros de 3 em 3 (per_page)
            games_page = Game.query.paginate(page=page, per_page=per_page)
        return render_template('editgame.html', g=g)
        