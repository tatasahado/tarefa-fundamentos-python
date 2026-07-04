total_produtos = 0
soma_precos = 0
produtos_acima_100 = 0

produto_mais_caro = ""
maior_preco = 0

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    preco = float(input("Digite o preço do produto: R$ "))

    total_produtos += 1
    soma_precos += preco

    if preco > 100:
        produtos_acima_100 += 1

    if total_produtos == 1 or preco > maior_preco:
        maior_preco = preco
        produto_mais_caro = nome
        
print("\n===== RESULTADO =====")

print(f"Total de produtos cadastrados: {total_produtos}")

if total_produtos > 0:
    media = soma_precos / total_produtos
    print(f"Produto mais caro: {produto_mais_caro} (R$ {maior_preco:.2f})")
    print(f"Média dos preços: R$ {media:.2f}")
else:
    print("Nenhum produto foi cadastrado.")

print(f"Produtos com preço acima de R$100: {produtos_acima_100}")