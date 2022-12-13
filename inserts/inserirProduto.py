from datetime import date
import uuid

def inserir_produto(session):
    busca_vendedores = session.run("MATCH (b:Vendedor) RETURN b")

    for vendedor in busca_vendedores:
        print('id: ' + vendedor[0].element_id[-2::])
        print('Nome: ' + vendedor[0]._properties['nome'])
        print('Email: ' + vendedor[0]._properties['email'])

    id_vend = input(str('\n Insira o ID do Vendedor do produto: '))
    
    # Dados do Produto
    dataAtual = date.today()
    nome = input(str("Insira o nome do produto: "))
    descricao = input(str("Insira a descrição do produto: "))
    preco = input(str("Insira o preço do produto: "))
    quantidade = input(str("Insira a quantidade de produtos em estoque: "))
    data_postagem = dataAtual.strftime('%d/%m/%Y')
    codigo_identificacao = str(uuid.uuid1())

    # QUERY DE INSERÇÃO
    query_prod = 'CREATE (p:Produto{codigo_identificacao:"' + codigo_identificacao + '", nome:"' + nome + '", descricao:"' + descricao + '", preco:"' + preco + '", quantidade: "' + quantidade +'", data_postagem: "' + data_postagem +'"})'
    session.run(query_prod)

    # QUERY DE LIGAÇÃO VENDEDOR E PRODUTO
    query_vend = ''' MATCH (v:Vendedor), (p:Produto) WHERE ID(v) = {id_vend} and p.codigo_identificao = "{cod_id}"
    CREATE (v)-[:VENDE]->(p)'''.format(id_vend = id_vend, cod_id = codigo_identificacao)
    session.run(query_vend)
    print('\n Produto cadastrado com sucesso !')