def excluir_vendedor(session):

    busca = session.run("MATCH (b:Vendedor) RETURN b")

    for resultado in busca:
        vendedor = resultado.value()
        print('\nid: ' + vendedor.element_id.split(":")[2])
        print('Nome: ' + vendedor._properties['nome'])
        print('Email: ' + vendedor._properties['email'])
    
    id_vend = input(str("Insira o ID do vendedor a ser excluído: "))

    # QUERY DE EXCLUSÃO
    query = f'MATCH (b:Vendedor) WHERE ID(b) = {id_vend} DETACH DELETE b'
    session.run(query)
    print('\n Vendedor excluído com sucesso !!!')