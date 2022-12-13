def update_produto(session):

    busca = session.run("MATCH (b:Produto) RETURN b")

    for resultado in busca:
        produto = resultado.value()
        print("\nid: "+ produto.element_id.split(":")[2])
        print("Nome: "+ produto._properties['nome'])
        print("Preço: "+ produto._properties['preco'])
        print("Descrição: "+ produto._properties['descricao'])

    id_produto = input(str("\n Insira o id do produto que deseja atualizar: "))

    nome = input(str("Insira o novo nome do produto: "))
    descricao = input(str("Insira a nova descrição do produto: "))
    preco = input(str("Insira o novo preço do produto: "))
    quantidade = input(str("Insira a nova quantidade de produtos em estoque: "))

    novos_dados = 'p.nome = "' + nome + '", p.descricao = "' + descricao + '", p.preco = "' + preco + '", p.quantidade =  "' + quantidade +'"'

    # QUERY DE ATUALIZAÇÃO
    query = f'MATCH (p:Produto) WHERE ID(p) = {id_produto} SET {novos_dados}'
    session.run(query)
    print('\n Produto atualizado com sucesso !!!')
