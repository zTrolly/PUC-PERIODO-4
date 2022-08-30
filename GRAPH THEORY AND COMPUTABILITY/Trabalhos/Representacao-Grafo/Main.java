import java.io.IOException;

public class Main{

  public static void main(String[] args) throws IOException {
    Tratamento tratamento = new Tratamento();
    String fileName = args[0];
      try {
        if (tratamento.verificaArquivo(fileName)) {
          
        } else {
          System.out.println("Arquivo não existe");
        }
      } catch (IOException e) {
        System.out.println("Erro ao abrir arquivo");
      }

  }
}