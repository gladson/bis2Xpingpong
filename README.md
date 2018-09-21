# Teste Lógica de Programação

### Instruções:

> Pode-se utilizar qualquer linguagem de programação.
> Não queremos telas de sistema, apenas a lógica utilizado para resolução do exercício abaixo.

### Placar de Ping-Pong

Jogar Ping-Pong pode ser bem divertido. Porém, após uma longa partida, é fácil de esquecer de quem é a vez de sacar.

Escreva uma função que receba a pontuação atual separada pelo caractere ":" como único
parâmetro, e retorne "jogador a" ou "jogador b", dependendo de quem é a vez de sacar.

Estaremos jogando o ping-pong old-school, então a regra é que os jogadores troquem a vez a
cada 5 sacadas. A regra muda caso a pontuação chegue a "20:20" - a partir desse momento,
cada jogador passa a sacar apenas 2 vezes antes da troca.

Um jogo termina quando um dos jogadores chega em 21 pontos com uma liderança mínima de
2 pontos. Porém, caso um jogo chegue numa pontuação "20:20", o vencedor será o primeiro
jogador a alcançar uma liderança de 2 pontos.

Observações:

    ● Não há necessidade de validar as entradas, considere que elas sempre estarão em formato válido
    ● Não é necessário checar se um dos jogadores já ganhou, este caso não será utilizado nos testes do algoritmo.
    ● O "jogador a" sempre começa sacando.

Exemplos:

Exemplos de chamada de função:

saque("0:0"); // retorna "jogador a"
saque("3:2"); // retorna "jogador b"
saque("21:20"); // retorna "jogador a"
saque("21:22"); // retorna "jogador b"