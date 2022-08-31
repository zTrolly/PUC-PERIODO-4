import java.io.*;
import java.util.*;
public class Tratamento {
  public Boolean verificaArquivo (String nomeArquivo) throws IOException {
    File arquivo = new File(nomeArquivo);
    if (arquivo.exists()) return true;
    else return false;
  }

  public String[] pegaNumeros (String linha)  { 
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < linha.length(); i++){
      if(linha.charAt(i) != ' '){
        sb.append(linha.charAt(i));
      } else if (i < linha.length() - 1 && linha.charAt(i + 1) != ' ' && sb.length() > 0){
        sb.append(" ");
      }
    }
    return sb.toString().split(" ");
  } 

  public List<Integer> teste(BufferedReader file) throws IOException {
    String[] arestasVertices = pegaNumeros(file.readLine());
    Integer origem[];
    Integer destino[];

  origem = new Integer[Integer.parseInt(arestasVertices[0])+1];
  destino = new Integer[Integer.parseInt(arestasVertices[1])];

  origem[0] = 0;
  origem[origem.length-1] = destino.length + 1;

  




    return valores;
  }

}
