from neo4j import GraphDatabase


# INSERTS
from inserts.inserirCliente import inserir_cliente
from inserts.inserirVendedor import inserir_vendedor
from inserts.inserirProduto import inserir_produto

# BUSCAS
from buscas.buscarCliente import busca_cliente
from buscas.buscarVendedor import busca_vendedor
from buscas.buscarProduto import busca_produtos

# UPDATES
from updates.updateCliente import update_cliente
from updates.updateVendedor import update_vendedor
from updates.updateProduto import update_produto

# EXCLUSÕES
from exclusões.excluirCliente import excluir_cliente
from exclusões.excluirVendedor import excluir_vendedor
from exclusões.excluirProduto import excluir_produtos

#  Conexão com o Neo4j
# uri = "neo4j+s://c87d723c.databases.neo4j.io"
# user = "neo4j"
# password = "6Q0Ytiw6C-bSjOWFVYv1weh0isXgKRqB6Bxj8G8IHrY"

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    session = driver.session()
    print("Conexão com Neo4j estabelecida com sucesso!")
except Exception as erro:
    print("Ih rapaz...deu erro", erro)


# MENU DE OPÇÕES

execucao = True

while execucao:
    print(''' 
        [1] Cadastrar Cliente
        [2] Cadastrar Vendedor
        [3] Cadastrar Produto
        [4] Cadastrar Compra
        [5] Buscar Cliente
        [6] Buscar Vendedor
        [7] Buscar Produto
        [8] Buscar Compra
        [9] Excluir Cliente
        [10] Excluir Vendedor
        [11] Excluir Produto
        [12] Excluir Compra
        [13] Update Cliente
        [14] Update Vendedor
        [15] Update Produto
        [0] Sair da Aplicação    
    ''')
    opcao = input(str('Bem-vindo! Escolha uma das opções acima: '))

    match int(opcao):
        case 1:
            inserir_cliente(session)
        case 2:
            inserir_vendedor(session)
        case 3:
            inserir_produto(session)
        # case 4:
        #     
        case 5:
            busca_cliente(session)
        case 6:
            busca_vendedor(session)
        case 7:
            busca_produtos(session)
        # case 8:
        #     
        case 9:
            excluir_cliente(session)
        case 10:
            excluir_vendedor(session)
        case 11:
            excluir_produtos(session)
        # case 12:
        #     
        case 13:
            update_cliente(session)
        case 14:
            update_vendedor(session)
        case 15:
            update_produto(session)
        case 0:
            execucao = False
            break
        case _:
            print("Operação não entendida...")