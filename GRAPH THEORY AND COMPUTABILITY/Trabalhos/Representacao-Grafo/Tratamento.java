import java.io.*;
public class Tratamento {
  public  Boolean verificaArquivo (String nomeArquivo) throws IOException {
    File arquivo = new File(nomeArquivo);
    if (arquivo.exists()) {
      return true;
    } else {
      return false;
    }
  }
}
