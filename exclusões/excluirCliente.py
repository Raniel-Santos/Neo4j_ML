def excluir_cliente(session):

    busca = session.run("MATCH (b:Cliente) RETURN b")

    for resultado in busca:
        cliente = resultado.value()
        print(f'\nid: {cliente.element_id.split(":")[2]}')
        print('Nome: {nome}'.format(nome = cliente._properties['nome']))
        print('Email: {email}'.format(email = cliente._properties['email']))
    
    id_cliente = input(str('\n Insira o ID do cliente a ser excluído: '))

    #QUERY DE EXCLUSÃO
    query = f'MATCH (b:Cliente) WHERE ID(b) = {id_cliente} DELETE b'
    session.run(query)
    print('\n Cliente excluído com sucesso !!!')