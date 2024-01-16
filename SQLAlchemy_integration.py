from sqlalchemy import(
    create_engine,
    Column,
    Integer,
    String,
    Binary,
    Float,
    ForeignKey,
    DECIMAL
)


from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy.orm import(
    relationship,
    sessionmaker
)


Base = declarative_base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))


    contas = relationship('Conta', back_populates='cliente')


class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Binary, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(DECIMAL)


    cliente = relationship('Cliente', back_populates='contas')


# Criando o banco de dados e as tabelas


engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)


# Inserindo dados de exemplo


Session = sessionmaker(bind=engine)
session = Session()


cliente1 = Cliente(nome='Cliente1', cpf='123456789', endereco='Endereco 1')
conta1 = Conta(id=b'1', tipo='Corrente', agencia='001', num=123, id_cliente=cliente1.id, saldo=1000.00)


session.add(cliente1)
session.add(conta1)


session.commit()


# Recuperando dados


clientes = session.query(Cliente).all()
print('Clientes:')
for cliente in clientes:
    print(f'ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}')


contas = session.query(Conta).all()
print('\nContas:')
for conta in contas:
    print(f'ID: {conta.id}, Tipo: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.numero}, Saldo: {conta.saldo}')



session.close()