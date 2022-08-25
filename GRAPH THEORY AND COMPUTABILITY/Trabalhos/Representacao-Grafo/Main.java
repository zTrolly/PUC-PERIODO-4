import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class Grafo<T> {
  private Map<T, List<T> > map = new HashMap<>(); // Hash para armazenar os arestas

  public void adicionaVertice(T s){
    map.put(s, new LinkedList<T>());
  }

  /**
   * Logica para adicinar as relações da aresta
   * @param origem
   * @param destino
   */
  public void adicionaAresta(T origem, T destino){
    if (!map.containsKey(origem)) adicionaVertice(origem); 
    if (!map.containsKey(destino)) adicionaVertice(destino);

    map.get(origem).add(destino);
  }

  @Override
	public String toString()
	{
		StringBuilder builder = new StringBuilder();

		for (T v : map.keySet()) {
			builder.append(v.toString() + ": ");
			for (T w : map.get(v)) {
				builder.append(w.toString() + " ");
			}
			builder.append("\n");
		}

		return (builder.toString());
	}

}


public class Main{
  public static void main(String[] args) throws IOException {
		Grafo<Integer> grafo = new Grafo<Integer>();

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

    linha = buffRead.readLine();
    int i = 0;
    while(true){
      if (linha != null){
        String teste = linha.replace("      ", " ").trim().replace("    ", " ").replace("  ", " ").replace("   ", " ").replace("  ", " ");
        i++;
        grafo.adicionaAresta(Integer.parseInt(teste.split(" ")[0]),Integer.parseInt(teste.split(" ")[1]));
      }else
        break;
      linha = buffRead.readLine();
      }
    
  
System.out.println(grafo.toString());
  
  
  }

}