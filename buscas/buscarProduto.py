def busca_produtos(session):

    busca = session.run("MATCH (b:Produto) RETURN b")
    print('\n Produtos cadastrados no sistema: ')

    for resultado in busca:
        produto = resultado.value()
        print("\nid: "+ produto.element_id.split(":")[2])
        print("Codigo de identificação do produto: " + produto._properties['codigo_identificacao'])
        print("Nome: "+ produto._properties['nome'])
        print("Descricao: "+ produto._properties['descricao'])
        print("Preço: "+ produto._properties['preco'])
        print("Quantidade: "+ produto._properties['quantidade'])
        print("Data de postagem: "+ produto._properties['data_postagem'])