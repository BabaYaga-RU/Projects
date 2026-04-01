/*
 * Lista baseada em Arranjo (Array)
 * 
 * Em vez de usar nós encadeados, esta lista usa um ARRANJO (array) de inteiros.
 * É como uma fila numerada: cada elemento tem uma POSIÇÃO fixa (0, 1, 2, ...).
 * 
 * Quando o arranjo enche, criamos um NOVO arranjo maior e copiamos os elementos.
 * 
 * Vantagem: acesso rápido por posição (elementos[i] pega o elemento na posição i)
 * Desvantagem: inserir/remover no início é lento (precisa mover todos os elementos)
 * 
 * Exercícios:
 * 1. Criar lista vazia
 * 2. Inserir no início
 * 3. Inserir no fim
 * 4. Inserir em posição específica
 * 5. Remover do início
 * 6. Remover do fim
 * 7. Remover de posição específica
 * 8. Remover elemento específico
 * 9. Exibir lista
 * 10. Pesquisar elemento
 * 11. Retornar tamanho
 */
public class Nao_foi_feito_por_ia_confia {

    // Atributos da lista baseada em arranjo:
    int[] elementos;   // o arranjo que guarda os números
    int tamanho;       // quantos elementos têm (próxima posição vazia)
    int capacidade;    // tamanho máximo do arranjo atual

    // 1. Construtor: cria arranjo com capacidade inicial de 10
    public Nao_foi_feito_por_ia_confia() {
        capacidade = 10;
        elementos = new int[capacidade];
        tamanho = 0;
    }

    // Cria lista vazia (reseta o tamanho para 0)
    public void criarListaVazia() {
        tamanho = 0;
    }

    // 2. Inserir no INÍCIO
    // Abre espaço na posição 0 movendo todos os elementos para a direita
    public void inserirNoInicio(int elemento) {
        if (tamanho == capacidade) redimensionar();  // se cheio, aumenta arranjo
        // Move todos os elementos uma posição para a direita
        for (int i = tamanho; i > 0; i--) {
            elementos[i] = elementos[i - 1];
        }
        elementos[0] = elemento;  // coloca novo elemento na posição 0
        tamanho++;
    }

    // 3. Inserir no FIM
    // Coloca elemento na próxima posição disponível (tamanho)
    public void inserirNoFim(int elemento) {
        if (tamanho == capacidade) redimensionar();  // se cheio, aumenta arranjo
        elementos[tamanho] = elemento;  // coloca na posição 'tamanho'
        tamanho++;
    }

    // 4. Inserir em POSIÇÃO específica
    // Move elementos da posição em diante para a direita, abre espaço
    public void inserirEmPosicao(int posicao, int elemento) {
        if (posicao < 0 || posicao > tamanho)
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        if (tamanho == capacidade) redimensionar();

        // Move elementos da posição em diante para a direita
        for (int i = tamanho; i > posicao; i--) {
            elementos[i] = elementos[i - 1];
        }
        elementos[posicao] = elemento;
        tamanho++;
    }

    // 5. Remover do INÍCIO
    // Pega elemento da posição 0, move todos para a esquerda
    public int removerDoInicio() {
        if (tamanho == 0) throw new IllegalStateException("Lista vazia");
        int elemento = elementos[0];  // guarda valor que será removido
        // Move todos os elementos uma posição para a esquerda
        for (int i = 0; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--;
        return elemento;
    }

    // 6. Remover do FIM
    // Simplesmente diminui o tamanho (última posição vira "vazia")
    public int removerDoFim() {
        if (tamanho == 0) throw new IllegalStateException("Lista vazia");
        tamanho--;  // diminui tamanho
        return elementos[tamanho];  // retorna o último elemento
    }

    // 7. Remover de POSIÇÃO específica
    // Move elementos da posição em diante para a esquerda, fechando o buraco
    public int removerEmPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho)
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        int elemento = elementos[posicao];  // guarda valor que será removido
        // Move elementos da posição em diante para a esquerda
        for (int i = posicao; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--;
        return elemento;
    }

    // 8. Remover ELEMENTO específico (pelo valor)
    // Procura o valor no arranjo e remove pela posição
    public boolean removerElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                removerEmPosicao(i);  // remove pela posição encontrada
                return true;
            }
        }
        return false;  // não achou
    }

    // 9. Exibir lista
    // Mostra: [1, 2, 3]
    public void exibirLista() {
        System.out.print("[");
        for (int i = 0; i < tamanho; i++) {
            System.out.print(elementos[i]);
            if (i < tamanho - 1) System.out.print(", ");
        }
        System.out.println("]");
    }

    // 10. Pesquisar elemento
    // Procura no arranjo, retorna a POSIÇÃO ou -1 se não achou
    public int pesquisarElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) return i;  // achou, retorna posição
        }
        return -1;  // não achou
    }

    // 11. Retornar tamanho
    public int tamanho() {
        return tamanho;
    }

    // Redimensionar: quando arranjo enche, dobra a capacidade
    // Cria novo arranjo maior e copia os elementos
    void redimensionar() {
        capacidade *= 2;  // dobra capacidade
        int[] novoArranjo = new int[capacidade];
        // Copia elementos do arranjo antigo para o novo
        for (int i = 0; i < tamanho; i++) {
            novoArranjo[i] = elementos[i];
        }
        elementos = novoArranjo;  // troca referência
    }
}