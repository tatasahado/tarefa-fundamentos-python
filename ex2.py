import random

while True:
    numero = random.randint(1, 100)
    tentativas = 0
    historico = []

    print("\n=== Jogo de Adivinhação ===")
    print("Tente adivinhar o número entre 1 e 100.")

    while tentativas < 7:

        entrada = input("Digite um número entre 1 e 100: ")

        # Validação para evitar erro caso o usuário digite texto
        if not entrada.isdigit():
            print("Digite apenas números!")
            continue

        palpite = int(entrada)
        tentativas += 1
        historico.append(palpite)

        if palpite < numero:
            print("Muito baixo!")
        elif palpite > numero:
            print("Muito alto!")
        else:
            print(f"\nParabéns! Você acertou em {tentativas} tentativa(s).")
            print("Histórico de tentativas:", historico)
            break

    else:
        print(f"\nVocê perdeu! O número era {numero}.")
        print("Histórico de tentativas:", historico)

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")

    if jogar_novamente.lower() != "s":
        print("Obrigado por jogar!")
        break