#include <stdio.h>
#include <string.h>

// Iniciar função principal
int main(){
    // Declara um vetor para armazenar a frase inicial
    char frase[30];
    // Declara respctivamente a variavel que armazena o tamanho da frase
    // e um contador para espaços
    int tam, conta = 0;
    // Imprime na tela uma mensagem para o usuário
    printf("Digite uma frase: ");
    fflush(stdin);
    // Recebe do usuário a frase completa
    gets(frase);
    // Armazenamos o tamanho da frase
    tam = strlen(frase);
    // Se tam = 0, então significa que nada foi digitado, apenas enter
    if(tam == 0){
        // Informa uma mensagem para o usuário
        printf("Informe uma frase valida\n");
    // Mas caso tam > 0
    } else {
        // Laço que percorre a frase para contar os espaços 
        for(int i = 0; i < tam; i++){
            if(frase[i] == ' '){
                // Se o caracter acima for espaço, e incrementado mais um em conta
                conta++;
            }
        }

        // Se conta(número de espaços) for igual a tam(número de caracteres da frase) significa que so foi digitado espaços
        // Ou seja, não há caracteres além de espaços em branco
         if(conta == tam){
            // Informa uma mensagem ao usuário
            printf("A frase nao pode conter apenas espacos.\n");
        // Mas caso conta < tam, já que o número de espaços pode ser igual mas nunca maior
        } else {
            // A variavel conta e incrementado mais um, para corrigir a questão de indices
            conta++;
            // Declara uma matriz de caracteres que armazena cada palavra
            char wor[conta][30];
            // Zera totalmente a matriz para evitar lixo de memória
            memset(wor, 0, sizeof(wor));
            // Declara respectivamente p1 que representa o indice das linhas da matriz
            // E p2 representa o indice das colunas e também o tamanho de cada palavra
            int p1 = 0, p2 = 0;
            // Laço que pega cada caractere de frase a adiciona para cada elemento da matriz
            for(int i = 0; i < tam; i++){
                // Se meu caractere não for um espaço
                if(frase[i] !=  ' '){
                    
                    wor[p1][p2] = frase[i];
                    // Incrementa p2(coluna/tamanho)
                    p2++;
                // Caso contrario
                } else {
                    wor[p1][p2] = '\0';
                    // Incrementa p1(linha)
                    p1++;
                    // Reinicia o contagem de p2
                    p2 = 0;
                }
            }
            // Declara respectivamente vez que armazena a quantidade de vezes que a palavra aparece
            // res armazena a condição que verifica se dois vetores de caracteres são iguais
            // cond armazena a condição que faz com que não haja repetição de palavras
            int vez = 0, res = 1, cond = 1;
            
            // Percorre cada linha da matriz wor
            for(int i = 0; i < conta; i++){
                // Inicializa com 1, pois supomos que os vetores sejam diferentes
                res = 1;
                // Inicializa com 0, pois supomos que a palavra ainda não apareceu nenhuma vez, ou pelo menos uma
                vez = 0;
                // Inicializa com 1, pois supomos que já houve repetição
                cond = 1;
                // Percorre todas as linhas de wor
                for(int j = 0; j < conta; j++){
                    // Faz a comparação
                    res = strcmp(wor[i], wor[j]);
                    // Se forem iguais, e a primeira incidencia seja na primeiro indice ou apos este
                    if(res == 0 && i >= j){
                        cond = 0;
                        vez++;
                    // Mas caso sejam iguais, e a incidencia seja antes da posição do vetor de busca
                    // Significa que já houve a contagem desta palavra
                    } else if(res == 0 && j > i){
                        cond = 1;
                    }
                }
                // Se cond = 0, não houve repetição
                if(cond == 0){
                    printf("A palavra: %s, aparece %d vezes.\n", wor[i], vez);
                }
            }
        }
    }
    return 0;
}