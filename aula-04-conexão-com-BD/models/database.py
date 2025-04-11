from flask_sqlalchemy import SQLAlchemy

# Carregando o SQLAlchemy em uma variavel

db = SQLAlchemy()

#classe da entindade games

class Game(db.Model):
    id = db.column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.column(db.Integer)
    categoria = db.column(db.String(150))
    plataforma = db.column(db.String(150))
    preco = db.column(db.Float)
    
# Metodo contrutor da classe

def __init__(self, titulo, ano, categoria, plataforma, preco):
    self.titulo = titulo
    self.ano = ano
    self.categoria = categoria
    self.plataforma = plataforma
    self.preco = preco