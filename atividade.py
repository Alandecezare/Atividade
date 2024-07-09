# Aqui importamos o random para gerar números aleatórios
import random

def criar_vetor():
    """
    Cria um vetor de 50 elementos inteiros únicos.
    """
    vetor = []  # Inicializa uma lista vazia para armazenar os elementos
    while len(vetor) < 50:  # Loop até que o vetor tenha 50 elementos
        numero = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        if numero not in vetor:  # Verifica se o número gerado já está no vetor
            vetor.append(numero)  # Se não estiver, adiciona o número ao vetor
    return vetor  # Retorna o vetor criado

def soma_vetores(x, y):
    """
    Retorna a soma elemento a elemento dos vetores x e y.
    """
    return [x[i] + y[i] for i in range(50)]  # Retorna uma lista com a soma dos elementos correspondentes de x e y

def produto_vetores(x, y):
    """
    Retorna o produto elemento a elemento dos vetores x e y.
    """
    return [x[i] * y[i] for i in range(50)]  # Retorna uma lista com o produto dos elementos correspondentes de x e y

def diferenca_vetores(x, y):
    """
    Retorna os elementos de x que não estão em y.
    """
    return [elem for elem in x if elem not in y]  # Retorna uma lista com os elementos de x que não estão em y

def intersecao_vetores(x, y):
    """
    Retorna os elementos que estão em ambos os vetores x e y.
    """
    return [elem for elem in x if elem in y]  # Retorna uma lista com os elementos que estão em ambos os vetores x e y

def uniao_vetores(x, y):
    """
    Retorna todos os elementos de x e todos os elementos de y que não estão em x.
    """
    return list(set(x + y))  # Retorna uma lista com todos os elementos de x e y, removendo duplicatas com set

def main():
    # Cria os vetores x e y
    x = criar_vetor()  # Chama a função criar_vetor para gerar o vetor x
    y = criar_vetor()  # Chama a função criar_vetor para gerar o vetor y

    # Mostra os vetores x e y
    print("Vetor x:", x)  # Exibe o vetor x
    print("Vetor y:", y)  # Exibe o vetor y

    # Menu de opções para o usuário
    while True:  # Loop infinito para exibir o menu até que o usuário decida sair
        print("\nEscolha uma operação:")  # Exibe uma mensagem de escolha de operação
        print("1. Soma entre x e y")  # Opção 1: Soma entre x e y
        print("2. Produto entre x e y")  # Opção 2: Produto entre x e y
        print("3. Diferença entre x e y")  # Opção 3: Diferença entre x e y
        print("4. Intersecção entre x e y")  # Opção 4: Intersecção entre x e y
        print("5. União entre x e y")  # Opção 5: União entre x e y
        print("6. Sair")  # Opção 6: Sair

        opcao = input("Digite o número da operação desejada: ")  # Lê a opção escolhida pelo usuário

        # Verifica qual opção foi escolhida e executa a operação correspondente
        if opcao == '1':
            resultado = soma_vetores(x, y)  # Chama a função soma_vetores
            print("Soma entre x e y:", resultado)  # Exibe o resultado da soma
        elif opcao == '2':
            resultado = produto_vetores(x, y)  # Chama a função produto_vetores
            print("Produto entre x e y:", resultado)  # Exibe o resultado do produto
        elif opcao == '3':
            resultado = diferenca_vetores(x, y)  # Chama a função diferenca_vetores
            print("Diferença entre x e y:", resultado)  # Exibe o resultado da diferença
        elif opcao == '4':
            resultado = intersecao_vetores(x, y)  # Chama a função intersecao_vetores
            print("Intersecção entre x e y:", resultado)  # Exibe o resultado da intersecção
        elif opcao == '5':
            resultado = uniao_vetores(x, y)  # Chama a função uniao_vetores
            print("União entre x e y:", resultado)  # Exibe o resultado da união
        elif opcao == '6':
            print("Saindo...")  # Exibe uma mensagem de saída
            break  # Encerra o loop
        else:
            print("Opção inválida. Tente novamente.")  # Informa ao usuário que a opção é inválida

if __name__ == "__main__":
    main()  # Chama a função main para executar o programa