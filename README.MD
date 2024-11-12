## Solucionador de Sistemas Lineares com Eliminação de Gauss 📐
Este projeto implementa um programa em Python que lê um sistema de equações lineares a partir de um arquivo de texto, aplica o método de eliminação de Gauss para encontrar as soluções, e, opcionalmente, verifica se os valores obtidos satisfazem o sistema original. 

## 🎮 Funcionalidades
- Leitura de um sistema de equações lineares a partir de um arquivo.
- Aplicação do método de eliminação de Gauss para resolver o sistema.
- Impressão do vetor de soluções.
- Verificação opcional dos valores obtidos para garantir que satisfazem as equações originais.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python

## 🚀 Como Executar o Projeto
1. Clone este repositório:
  ```bash
  git clone https://github.com/AdelsonJ/seu-repositorio.git
  ```
2. Certifique-se de ter um arquivo contendo o sistema de equações, no seguinte formato:
- Todos os coeficientes 0 devem ser explicitamente representados junto das variáveis.
- O coeficiente 1 pode ser omitido (exemplo: x é interpretado como 1x).
- O arquivo deve ter, no mínimo, o mesmo número de linhas em relação ao número de variáveis no sistema.
  ```bash
  3x1 - 4x2 + x3 = 9
  x1 + 2x2 + 2x3 = 3
  4x1 + 0x2 - 3x3 = -2
  ```

3. Execute o programa com os seguintes argumentos:

  ```bash
  python nome_do_arquivo.py nome_do_arquivo.txt 1
  ```

- Substitua nome_do_arquivo.txt pelo nome do arquivo contendo as equações.
- O último argumento (1 ou 0) indica se a verificação deve ser feita (1 para sim, 0 para não).

Exemplo de saída:
  ```bash
  O vetor x eh: [2.0, -1.0, 3.0]
  ```

## 📦 Dependências
Nenhuma biblioteca externa é necessária além do Python.

## 💡 Como Funciona
- Leitura do Arquivo: A função leiaEntrada() lê o sistema de equações do arquivo e extrai os coeficientes.
- Eliminação de Gauss: A função metodoGauss() aplica o método de eliminação de Gauss para resolver o sistema.
- Impressão do Resultado: A função imprimeResultado() exibe o vetor de soluções.
- Verificação Opcional: A função conferindo() calcula e verifica o valor de cada equação com a solução obtida, se solicitado.

## 🧑‍💻 Autor
Projeto desenvolvido por AdelsonJ.
