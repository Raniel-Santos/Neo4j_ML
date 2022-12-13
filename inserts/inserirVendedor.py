from datetime import date

def inserir_vendedor(session):
    dataAtual = date.today()

    # Dados do Vendedor
    nome = input(str('Insira o nome do vendedor: '))
    email = input(str('Insira o email do vendedor: '))
    cnpj = input(str('Insira o CNPJ do vendedor: '))   
    telefone = input(str('Insira o telefone do vendedor: '))
    data_cadastro = dataAtual.strftime('%d/%m/%Y')

    # QUERY DE INSERÇÃO
    query = 'CREATE (v:Vendedor{ nome: "' + nome +'", email: "' + email + '", cnpj:"' + cnpj +'", data_cadastro:"' + data_cadastro + '", telefone:"' + telefone + '" })'
    session.run(query)
    print('\n Vendedor cadastrado com Sucesso ! ')