from datetime import date

def inserir_compra(session):

    busca_cliente = session.run("MATCH (b:Cliente) RETURN b")

    for resultado in busca_cliente:
        cliente = resultado.value()
        print("id:" + cliente.element_id.split(":")[2])
        print('nome: {nome}'.format(nome=cliente._properties['nome']))
        print('email: {email}'.format(email=cliente._properties['email']))
        print('cpf: {cpf}'.format(cpf=cliente._properties['cpf']))
    
    id_cliente = input(str('\n Insira o ID do Cliente: '))

    busca_produtos = session.run("MATCH (p:Produto) RETURN p")

    for p in busca_produtos:
        produto = p.value()
        print('id: ' + produto.element_id.split(":")[2])
        print('nome: ' + produto._properties['nome'])
        print('preço: ' + produto._properties['preco'])
        

    id_produto = input(str("\n Insira o ID do produto que deseja comprar: "))

    dataAtual = date.today()
    data_compra = dataAtual.strftime('%d/%m/%Y')

    # INSERT DA COMPRA
    session.run(f''' 
                MATCH (b:Cliente), (p:Produto)
                WHERE ID(b) = {id_cliente} AND ID(p) = {id_produto}
                CREATE (b)-[:COMPROU ''' + '{data_compra:" ' + str(data_compra) + '"}]->(p)'
                )
    print('\n Compra realizada com sucesso!!!')                
    