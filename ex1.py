total_produtos = 0
soma_precos = 0
produtos_acima_100 = 0

produto_mais_caro = ""
maior_preco = 0

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break