import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class Main{

  public static void main(String[] args) throws IOException {

    String fileName = args[0];
    int vertice = Integer.parseInt(args[1]);

    //DEBUG_PRINT_FILE_NAME_AND_VERTICE(fileName, vertice)
    System.out.println("Arquivo: " + fileName);
    System.out.println("Vertice: " + vertice);
    

    BufferedReader buffRead = new BufferedReader(new FileReader(fileName));
		String linha = "";
  
    // pegar a primeira linha do arquivo e separar o numero de vertices e de arestas
    linha = buffRead.readLine();
    int numeroVertices = Integer.parseInt(linha.split(" ")[0]);
    int numeroArestas = Integer.parseInt(linha.split(" ")[2]);

    //DEBUG_PRINT_NUMBER_OF_VERTICES_AND_EDGES(numeroVertices, numeroArestas)
    System.out.println("Numero de vertices: " + numeroVertices);
    System.out.println("Numero de arestas: " + numeroArestas);

		
		buffRead.close();

  
  }

}