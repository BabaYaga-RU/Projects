// Prazo: 22/03/2026

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int indice = 1;
        System.out.println("====================== Exercicio " + indice + " ======================");
        /*
        1. Escreva um programa que leia dois vetores inteiros com dez posições cada. 
        A partir desses vetores, carregue um terceiro vetor onde o valor de cada elemento 
        será a média dos elementos de mesmo índice nos dois vetores anteriores.
        */
        try{
            double[] vetor_um = {6, 19, 184, 310, 12, 13, 28, 333, 666, 17};
            double[] vetor_dois = {21, 16, 1, 15, 27, 5, 11, 33, 22, 4};
            double[] vetor_tres = new double[10];
            for (int i = 0; i < vetor_um.length; i ++){
                vetor_tres[i] = (vetor_um[i] + vetor_dois[i]) / 2;
                System.out.println(vetor_tres[i]);
            }
        }catch(Exception e){}
        indice ++;
        System.out.println("====================== Exercicio " + indice + " ======================");
        /*
        2. Escreva um programa que carregue um vetor inteiro de cem posições com números 
        aleatórios entre 0 e 100. Percorrendo o vetor criado apenas uma vez, imprima a 
        posição onde ocorre o menor o valor, a soma dos números armazenados e preencha 
        os valores de um novo vetor com metade do tamanho do vetor original onde a primeira 
        posição do novo vetor é igual à soma da primeira e da última posição do vetor original. 
        A segunda posição do novo vetor é a soma da segunda e da penúltima posição do 
        vetor original e assim em diante.
        */
        try{

        }catch(Exception e){}
        indice ++;
        System.out.println("====================== Exercicio " + indice + " ======================");
        /*
        3. Escreva um programa que carregue dois vetores inteiros com 5 posições, sendo 
        um com números pares e o outro com números ímpares. O usuário pode digitar os 
        números em qualquer sequência e o programa deverá armazená-los no vetor correto 
        na ordem em que foram informados pelo usuário.
        */
        try{

        }catch(Exception e){}
        indice ++;
        System.out.println("====================== Exercicio " + indice + " ======================");
        /*
        4. Escreva um programa que ordene um vetor de tamanho arbitrário preenchido com 
        números aleatórios e execute a pesquisa por um valor passado como parâmetro 
        utilizando o algoritmo da busca binária.
        */
        try{

        }catch(Exception e){}
        indice ++;
        System.out.println("====================== Exercicio " + indice + " ======================");
        /*
        5. Implemente dois algoritmos que ordenem os elementos de um vetor em ordem 
        crescente e compare o número de trocas que eles efetuam durante a ordenação de:

        a) um vetor criado com os números de 1 até 100 aleatoriamente distribuídos.
        b) um vetor criado com os números de 1 até 100 ordenados em ordem decrescente
        */
        try{

        }catch(Exception e){}
    }
}