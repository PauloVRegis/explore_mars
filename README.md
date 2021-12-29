# explore_mars

Projeto que simula a exploração de uma área de Marte com duas sondas espaciais.

**Funcionamento:**

Cada sonda é inserida na área apontando para uma direção (norte, leste, oeste ou sul). Dada essa posição inicial e uma sequência de movimentos (virar 90 graus para a esquerda, para a direita, ou mover-se um ponto a frente), o programa deve retornar a posição final da sonda.

**Entrada:**

Primeira linha: coordenadas do canto superior direito do campo a ser explorado.
Depois, cada sonda contém duas linhas de informações.

Primeira linha: Coordenadas e direção da sonda no ponto inicial no formato "X Y D" (Exemplo: 1 3 N)
Segunda linha: Sequência de movimentos a serem realizados pela sonda (Exemplo: LMLMRMRM)

**Saída:**

Cada sonda gera uma linha de saída, indicando sua coordenada final e direção no formato "X Y D".

**EXECUÇÃO DO CÓDIGO**

docker build -t explore_mars .

docker run -t -i explore_mars

5 5 #coordenadas do canto superior direito do campo a ser explorado

1 3 N #Coordenadas e direção da primeira sonda no ponto inicial no formato "X Y D"

LMLMLMLMM #Sequência de movimentos a serem realizados pela sonda

3 3 E #Coordenadas e direção da segunda sonda no ponto inicial no formato "X Y D"

MMRMMRMRRM #Sequência de movimentos a serem realizados pela sonda

**Outupt do resultado das posições finais das sondas no formato "X Y D""**

