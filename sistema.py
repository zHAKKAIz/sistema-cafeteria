# ==============================================
#            ATIVIDADE AVALIATIVA - PYTHON
#    Sistema de Gerenciamento - Cafeteria Tia Rosa
# ==============================================
# Desenvolvido por zHAKKAIz

# ============================
# ======= BASE DE DADOS ======
# ============================

produtos = []
clientes = []
vendas = []

# ============================
# ========= FUNÇÕES ==========
# ============================

def cabecalho(texto):
    """Exibe um cabeçalho estilizado"""
    print("\n" + "=" * 45)
    print(f"{texto.center(45)}")
    print("=" * 45)

def cadastrar_produto():
    cabecalho("Cadastro de Produto")
    nome = input("Nome: ").strip()
    preco = float(input("Preço (R$): "))
    descricao = input("Descrição: ").strip()
    ingredientes = input("Ingredientes (separados por vírgula): ").split(",")
    promocao = input("Está em promoção? (s/n): ").strip().lower() == 's'
    estoque = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "descricao": descricao,
        "ingredientes": [i.strip() for i in ingredientes],
        "promocao": promocao,
        "estoque": estoque
    }

    produtos.append(produto)
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")

def cadastrar_cliente():
    cabecalho("Cadastro de Cliente")
    nome = input("Nome: ").strip()
    contato = input("E-mail ou telefone: ").strip()
    clientes.append({"nome": nome, "contato": contato})
    print(f"✅ Cliente '{nome}' cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    cabecalho("Produtos Disponíveis")
    for i, p in enumerate(produtos):
        status = "🔥 Promoção" if p["promocao"] else "Preço normal"
        print(f"{i + 1}. {p['nome']} - R${p['preco']:.2f} - {status} | Estoque: {p['estoque']}")

def fazer_pedido():
    if not produtos:
        print("Nenhum produto disponível.")
        return

    cabecalho("Novo Pedido")
    nome_cliente = input("Nome do cliente: ").strip()
    pedido = {"cliente": nome_cliente, "itens": [], "total": 0}

    while True:
        listar_produtos()
        escolha = input("Digite o número do produto (ou 'fim' para encerrar): ").strip()
        if escolha.lower() == 'fim':
            break

        try:
            indice = int(escolha) - 1
            if 0 <= indice < len(produtos):
                produto = produtos[indice]
                quantidade = int(input("Quantidade: "))
                if quantidade <= produto["estoque"]:
                    produto["estoque"] -= quantidade
                    subtotal = produto["preco"] * quantidade
                    pedido["itens"].append((produto["nome"], quantidade, subtotal))
                    pedido["total"] += subtotal
                else:
                    print("⚠️ Estoque insuficiente.")
            else:
                print("⚠️ Produto inválido.")
        except ValueError:
            print("⚠️ Entrada inválida. Tente novamente.")

    vendas.append(pedido)
    print(f"🧾 Pedido finalizado. Total: R${pedido['total']:.2f}")

def ver_estoque():
    cabecalho("Estoque Atual")
    for p in produtos:
        print(f"{p['nome']}: {p['estoque']} unidades")

def ver_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    cabecalho("Histórico de Vendas")
    for venda in vendas:
        print(f"🧍 Cliente: {venda['cliente']}")
        for item in venda["itens"]:
            print(f" - {item[0]} x{item[1]} = R${item[2]:.2f}")
        print(f"💰 Total: R${venda['total']:.2f}\n")

def exibir_menu():
    print("\n" + "=" * 45)
    print(" MENU PRINCIPAL ".center(45, "="))
    print("=" * 45)
    print("1. Cadastrar Produto")
    print("2. Cadastrar Cliente")
    print("3. Fazer Pedido")
    print("4. Ver Estoque")
    print("5. Ver Vendas")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            cadastrar_cliente()
        elif opcao == '3':
            fazer_pedido()
        elif opcao == '4':
            ver_estoque()
        elif opcao == '5':
            ver_vendas()
        elif opcao == '6':
            print("\n📦 Encerrando o sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Execução principal
if __name__ == "__main__":
    main()