import re  
import sys  

# Funcao que le o arquivo
def leiaEntrada(nome_arquivo):
    # Abre o arquivo em modo leitura
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Conta o numero total de linhas no arquivo
    nlinhas = len(linhas)
    
    # Inicializa a lista que armazenara os coeficientes e o termo independente de cada equacao
    equacoes = []
    
    for linha in linhas:
        # Extrair a parte da equacao antes e depois do '='
        esquerda, direita = linha.split('=')
        direita = float(direita.strip())
        
        # Usar regex para encontrar os coeficientes e sinais
        numeros = re.findall(r'([+-]?\s*\d*\.?\d*)\s*x\d+', esquerda)
        
        # Processar os termos para obter os coeficientes
        coeficientes = []
        for termo in numeros:
            termo = termo.replace(" ", "")
            if termo == '+' or termo == '':
                coeficientes.append(1)
            elif termo == '-':
                coeficientes.append(-1)
            else:
                coeficientes.append(float(termo))
        
        coeficientes.append(direita)        
        
        equacoes.append(coeficientes)
    
    return nlinhas, equacoes

# Funcao que resolve o sistema usando o metodo de elinacao de gauss
def metodoGauss(nlinhas, equacao):    
    for variavel in range(nlinhas):
        # Verifica se eh necessario trocar linhas para evitar divisao por zero
        if equacao[variavel][variavel] == 0:
            for k in range(variavel + 1, nlinhas):
                if equacao[k][variavel] != 0:
                    equacao[variavel], equacao[k] = equacao[k], equacao[variavel]
                    break

        # Aplicar eliminacao para todas as linhas abaixo da linha pivo
        for i in range(variavel + 1, nlinhas):
            fator = equacao[i][variavel] / equacao[variavel][variavel]
            for j in range(variavel, nlinhas + 1):
                equacao[i][j] -= fator * equacao[variavel][j]

# Funcao que encontra a resposta usando o substituicao regressiva
def substituicao_regressiva(nlinhas, equacao):
    resposta = [0] * nlinhas
    for i in range(nlinhas - 1, -1, -1):
        soma = sum(equacao[i][j] * resposta[j] for j in range(i + 1, nlinhas))
        resposta[i] = (equacao[i][-1] - soma) / equacao[i][i]
    return resposta

# Funcao que confere se os dados estao corretos
def conferindo(nome_arquivo, resposta):
    nlinhas, equacao = leiaEntrada(nome_arquivo)
    print("\nConferindo resultados:")
    for i in range(nlinhas):
        total = sum(equacao[i][j] * resposta[j] for j in range(nlinhas))
        print(f"Equacao {i + 1}: Calculado = {total:.4f}, Original = {equacao[i][-1]:.4f}")

###########################################################################################################################################

if len(sys.argv) != 3:
    print("Por favor, digite o nome do arquivo e se deseja que a verificao seja impressa tambem (1-sim 0-nao).")
    sys.exit()

nome_arquivo = sys.argv[1]  
verificacao = int(sys.argv[2])  

nlinhas, equacao = leiaEntrada(nome_arquivo)
print("Matriz inicial:")
for linha in equacao:
    print(linha)

metodoGauss(nlinhas, equacao)

resposta = substituicao_regressiva(nlinhas, equacao)
print("\nSolucao:", resposta)

if verificacao == 1:
    conferindo(nome_arquivo, resposta)
