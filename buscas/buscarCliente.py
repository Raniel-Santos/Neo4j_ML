def busca_cliente(session):
    
    busca = session.run("MATCH (b:Cliente) RETURN b") 
    print('\n Clientes cadastrados no sistema: ')

    for resultado in busca:
        id = resultado[0].element_id.split(":")
        print(f'\nid: {id[2]}')
        print('nome: {nome}'.format(nome=resultado[0]._properties['nome']))
        print('email: {email}'.format(email=resultado[0]._properties['email']))
        print('cpf: {cpf}'.format(cpf=resultado[0]._properties['cpf']))
        print('data de nascimento: {data_nascimento}'.format(data_nascimento=resultado[0]._properties['data_nascimento']))
        print('telefone: {telefone}'.format(telefone=resultado[0]._properties['telefone']))
        print('endereco: {endereco}'.format(endereco=resultado[0]._properties['endereco']))