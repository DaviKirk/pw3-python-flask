# pip gerenciador de pacotes do python
# pip install flask
# importando pacote do Flask
from flask import Flask

# Importando o PyMySQL
import pymysql

#importando arquivo routes do controllers
from controllers import routes

#importa os models

from models.database import db


# carregando o Flask na variável app
app = Flask(__name__, template_folder="views")

#Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

# Define o nome do banco de dados
DB_NAME = 'games'
# Configura o Flask com banco de finido
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco de dados ao flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

if __name__ == '__main__':
    #criando os dados de conexão
    connection = pymysql.connect(host='localhost', 
                                 user='root', 
                                 passwd='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    
    #tentando criar o banco
    #try, trata o sucesso
    try:
        #with cria um recurso temporariamente
        with connection.cursor() as cursor: #alias
            #cria o banco de dados (se ele não existir)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados {DB_NAME} está criado!")
    #trata a falha    
    except Exception as e:
        print(f'Erro ao criar o banco de dados: {e}')
    finally:
        connection.close()
        
    # passando o flask para o SQLAlchemy
    db.init_app(app=app)
    
    # Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
    
    # Inicializando a aplicação flask
    app.run(host='localhost', port=5000, debug=True)
