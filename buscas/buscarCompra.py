def buscar_compra(session):

    busca = session.run('MATCH (u:Cliente)-[c:COMPROU] ->(p:Produto) RETURN *')

    for c in busca:
        compra = c.value()
        print("\nInformações da compra")
        print("id: " + compra.element_id.split(":")[2])
        print(f"Data da compra: {compra._properties['data_compra']}")

        for info_compra in compra.nodes:
            label = list(info_compra.labels)
            if label[0] == "Cliente":
                print("Informações do cliente: {nome}, email: {email}".format(nome = info_compra._properties['nome'], email = info_compra._properties['email']))
            if label[0] == "Produto":
                print("Produto: {nome}, preco: {preco}".format( nome = info_compra._properties['nome'], preco = info_compra._properties['preco']))