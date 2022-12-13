def update_vendedor(session):
    
    busca = session.run("MATCH (b:Vendedor) RETURN b")

    for resultado in busca:
        vendedor = resultado.value()
        print('\nid: ' + vendedor.element_id.split(":")[2])
        print('Nome: ' + vendedor._properties['nome'])
        print('Email: ' + vendedor._properties['email'])
    
    id_vend = input(str('\n Insira o ID do vendedor a ser atualizado: '))

    nome = input(str("Insira o nome do vendedor: "))
    email = input(str('Insira o endereço de email: '))
    cnpj = input(str("Insira o cnpj: "))
    telefone = input(str('Insira o numero do telefone: '))

    novos_dados =  'v.nome = "' + nome +'", v.email = "' + email + '", v.cnpj ="' + cnpj +'", v.telefone ="' + telefone + '"'

    #QUERY DE ATUALIZAÇÃO
    query = f'MATCH (v:Vendedor) WHERE ID(v) = {id_vend} SET {novos_dados}'
    session.run(query)
    print('\n Vendedor atualizado com sucesso !!!')
