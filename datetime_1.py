print("Digite o seu nome: ")
nome = input()

executar = True

while executar:
    print("Digite o ano em que nascimento")
    try:
        ano = int(input())
        if ano < 1922 or ano > 2021:
            print("O ano digitado precisa ser entre 1922 e 2021")
        else:
            idade = 2022 - ano
            print("O usuário", nome, "completou ou irá completar", idade, "anos de idade em 2022.")
            executar = False
    except ValueError:
        print("Erro: Os anos precisam ser escritos apenas com números!")
# Usei 'while executar' para simplificar a condição de loop. Acrescentei também a mensagem 'Value Error' na exceção para ficar mais específico.