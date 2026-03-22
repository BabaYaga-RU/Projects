import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        try{
            Random random = new Random();
            int[] vetor_um = new int[100];
            int indice = 0;
            while(true){
                int valor_atual = random.nextInt(100);
                boolean contem = false;
                boolean final_vetor = true;
                for (int i = 0; i < 100; i++){
                    if (vetor_um[i] == valor_atual + 1){
                        contem = true;
                    }
                    if (vetor_um[i] == 0){
                        final_vetor = false;
                    }
                }
                if (final_vetor == true){
                    break;
                }
                if (contem == false){
                    vetor_um[indice] = valor_atual + 1;
                    indice ++;
                }
            }
            System.out.println("Primeiro vetor: " + Arrays.toString(vetor_um));
            int[] vetor_dois = new int[100];
            indice = 0;
            for (int i = 100; i > 0; i--){
                vetor_dois[indice] = i;
                indice ++;
            }
            System.out.println("Segundo vetor: " + Arrays.toString(vetor_dois));

        }catch(Exception e){}
    }
}