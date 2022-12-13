def inserir_cliente(session):

    # Dados do Cliente
    nome = input(str('Insira o nome do cliente: '))
    email = input(str('Insira o email do cliente: '))
    cpf = input(str('Insira o CPF do cliente: '))
    data_nascimento = input(str('Insira a data de nascimento do cliente: '))
    telefone = input(str('Insira o telefone do cliente: '))
    endereco = input(str('Insira o endereço completo do cliente: '))

    # QUERY DE INSERÇÃO
    query = 'CREATE (c:Cliente{nome:"' + nome +'", email: "' + email + '", cpf: "' + cpf + '", data_nascimento: "' + data_nascimento + '", telefone:"' + telefone + '", endereco:"' + endereco + '"})'
    session.run(query)
    print('\n Cliente cadastrado com Sucesso ! ')