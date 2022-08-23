import java.util.Scanner;

public class Main{

  public static void main(String[] args) {
    // receber o nome e p vertice para ser procurado
    System.out.println("Digite o nome do arquivo e o vértice separados por espaço");
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    String fileName = input.split(" ")[0];
    int vertice = Integer.parseInt(input.split(" ")[1]);
    sc.close();

    System.out.println("Arquivo: " + fileName);
    System.out.println("Vertice: " + vertice);
  }
}