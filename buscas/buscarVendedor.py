def busca_vendedor(session):
    busca = session.run("MATCH (b:Vendedor) RETURN b")
    print('\n Vendedores cadastrados no sistema')

    for resultado in busca:
        vendedor = resultado.value()
        print('\nid: ' + vendedor.element_id.split(":")[2])
        print('Nome: ' + vendedor._properties['nome'])
        print('Email: ' + vendedor._properties['email'])
        print('Cnpj: ' + vendedor._properties['cnpj'])
        print('Telefone: ' + vendedor._properties['telefone'])
        print('Data de cadastro: ' + vendedor._properties['data_cadastro'])