def update_cliente(session):

    busca = session.run("MATCH(b:Cliente) RETURN b")

    for resultado in busca:
        cliente = resultado.value()
        print(f'\nid: {cliente.element_id.split(":")[2]}')
        print('Nome: {nome}'.format(nome = cliente._properties['nome']))
        print('Email: {email}'.format(email = cliente._properties['email']))
        print('cpf: {cpf}'.format(cpf = cliente._properties['cpf']))
    id_cliente = input(str('Insira o ID do cliente a ser atualizado: '))

    nome = input(str('Insira o novo nome do usuario: '))
    email = input(str('Insira o novo endereço de email: '))
    cpf = input(str('Insira o novo numero do cpf: '))
    data_nascimento = input(str('Insira a nova data de nascimento: '))
    telefone = input(str('Insira o novo numero do telefone: '))
    endereco = input(str('Insira o novo endereço: '))

    novos_dados = 'b.nome = "' + nome +'", b.email = "' + email + '", b.cpf = "' + cpf + '",  b.data_nascimento = "' + data_nascimento + '", b.telefone = "' + telefone + '", b.endereco = "' + endereco + '"'
    
    # QUERY DE ATUALIZAÇÃO
    query_update = f'MATCH (b:Cliente) WHERE ID(b) = {id_cliente} SET {novos_dados}'
    session.run(query_update)
    print('\n Cliente atualizado com Sucesso!!!')