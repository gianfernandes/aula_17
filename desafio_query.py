from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Fornecedor(Base):
  __tablename__ = 'fornecedores'
  id = Column(Integer, primary_key=True)
  nome = Column(String(50), nullable=False)
  telefone = Column(String(20))
  email = Column(String(50))
  endereco = Column(String(100))

class Produto(Base):
  __tablename__ = 'produtos'
  id = Column(Integer, primary_key=True)
  nome = Column(String(50), nullable=False)
  descricao = Column(String(50))
  preco = Column(Integer)
  fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

# Estabelece a relação entre Produto e Fornecedor
fornecedor = relationship("Fornecedor")

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

resultado = session.query(
  Produto.nome.label('produto_nome'),
  Fornecedor.nome.label('fornecedor_nome') 
).join(Fornecedor, Fornecedor.id == Produto.fornecedor_id).all()

for produto_nome, fornecedor_nome in resultado:
  print(f"Produto: {produto_nome}, Fornecedor: {fornecedor_nome}")