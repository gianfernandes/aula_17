from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

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

# Inserindo fornecedores
try:
  with Session() as session:
    fornecedores = [
      Fornecedor(nome="Fornecedor A", telefone="123456789", email="contato@a.com.br", endereco="Endereço A"),
      Fornecedor(nome="Fornecedor B", telefone="123456789", email="contato@b.com.br", endereco="Endereço B"),
      Fornecedor(nome="Fornecedor C", telefone="123456789", email="contato@c.com.br", endereco="Endereço C"),
      Fornecedor(nome="Fornecedor D", telefone="123456789", email="contato@d.com.br", endereco="Endereço D"),
      Fornecedor(nome="Fornecedor E", telefone="123456789", email="contato@e.com.br", endereco="Endereço E"),
    ]

    session.add_all(fornecedores)
    session.commit()
except SQLAlchemyError as e:
  print(f"Erro ao inserir fornecedores: {e}")

# Inserindo Produtos
try:
  with Session() as session:
    produtos = [
      Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
      Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
      Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
      Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
      Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5),
    ]

    session.add_all(produtos)
    session.commit()
except SQLAlchemyError as e:
  print(f"Erro ao inserir fornecedores: {e}")