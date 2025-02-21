# pip gerenciador de pacotes do python
# pip install flask
# importando pacote do Flask
from flask import Flask, render_template

# carregando o Flask na variável app
app = Flask(__name__, template_folder="views")

# criando a rota principal do site
@app.route('/')
# criando função no python
#view function - Função de visualização
def home():
   
    return render_template('index.html',)

@app.route('/games')
def games():
    titulo = 'CS-GO'
    ano = 2012
    categoria = 'FPS Online'
    jogadores = ["Mc Rodolfinho", "davi_lambari", "juju_do_pix", "suaIrmã", "edsonGf"]
    games = ['My Summer Car', 'Assetto Corsa', 'Beamg Drive', 'Forza Horizon 4', 'Minecraft', 'Grand Theft Auto V', 'Ragnarök']
    return render_template('games.html',
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores,
                           games=games)

if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)