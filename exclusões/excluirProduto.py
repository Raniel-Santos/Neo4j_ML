def excluir_produtos(session):

    busca = session.run("MATCH (b:Produto) RETURN b")

    for resultado in busca:
        produto = resultado.value()
        print("\nid: "+ produto.element_id.split(":")[2])
        print("Nome: "+ produto._properties['nome'])
        print("Preço: "+ produto._properties['preco'])
        print("Descrição: "+ produto._properties['descricao'])
    
    
    id_produto = input(str("Digite o id do produto que deseja excluir: "))

    # QUERY DE EXCLUSÃO
    query = f'MATCH (p:Produto) WHERE ID(p) = {id_produto} DELETE p'
    session.run(query)
    print('\n Produto deletado com sucesso!!!')