import sys
import os.path

#Lista global
listaPredecessores = []
listaSucessores = []

#utility
ultimoVertice = None

#retorno
grauEntrada = 0
grauSaida = 0

#FOI
def inicializador(tamanho):
  global listaPredecessores 
  listaPredecessores = [None] * (tamanho-1)

# vai verificar se o vertice de origem ja foi trocado 
def verificaVertice(linha):
  global ultimoVertice

  if ultimoVertice == None:
    ultimoVertice = linha
    resp = 3   
    return resp
  elif ultimoVertice == linha:
    ultimoVertice = linha  
    resp = False  
    return resp
  else:
    ultimoVertice = linha
    resp = True    
    return resp

#FOI
def verificaPredecessores(vertice):
   resp = False
   aux = listaPredecessores[vertice-1]
   if aux != None:
     resp = True       
   return resp 

#FOI
def criarPredecessor(destino, origem):
  if destino.predecessor == None:
    destino.predecessor = origem
    return
  else:
    criarPredecessor(destino.predecessor, origem)
 
 #FOI
def pesquisaDosPredecessores(aux, predecessores):
  if aux.vertice != None:
    if aux.predecessor != None:
      predecessores.append(aux.predecessor.vertice)
      pesquisaDosPredecessores(aux.predecessor, predecessores)
  else:
    return

 #logica dos sucessores
#FOI
def verificaSucessores(vertice):
  resp = False
  aux = listaSucessores[vertice-1]
  if aux != None:
    resp = True       
  return resp 

#FOI
def criarAresta(origem, destino):
  if origem.sucessor == None:
    origem.sucessor = destino
    return
  else:
    criarAresta(origem.sucessor, destino)

    #FOI
def pesquisaDosSucessores(aux, sucessores):
  if aux.vertice != None:
    if aux.sucessor != None:
      sucessores.append(aux.sucessor.vertice)
      pesquisaDosSucessores(aux.sucessor, sucessores)
  else:
    return
    
#FOI
def criar(linha):
  temp = verificaVertice(linha[0])
  if temp == 3:

    origem = sucessor()
    destino = sucessor()

    origem.vertice = linha[0]
    destino.vertice = linha[1]

    destino.sucessor = None
    origem.sucessor = destino

    listaSucessores.append(origem)    
    
    destinoII = predecessor()
    origemII = predecessor()

    destinoII.vertice = linha[1]
    origemII.vertice = linha[0]

    destinoII.predecessor = origemII
    listaPredecessores.insert(int(linha[1])-1, destinoII)   
    
  #FOI
  elif temp == False:
    destino = sucessor()
    destino.vertice = linha[1] 

    origem = listaSucessores[len(listaSucessores)-1]
    criarAresta(origem, destino)    

  #FOI
  else:
    origem = sucessor()
    destino = sucessor()

    origem.vertice = linha[0]
    destino.vertice = linha[1]
    
    origem.sucessor = destino
    listaSucessores.append(origem)

  #FOI
  if temp != 	3:
      if verificaPredecessores(int(linha[1])):
       teste = predecessor()
       teste.vertice = linha[0]
       criarPredecessor(listaPredecessores[(int(linha[1])-1)], teste)
      else:
       destinoTeste = predecessor()
       teste = predecessor()
       teste.vertice = linha[0]
       destinoTeste.vertice = linha[1]
       destinoTeste.predecessor = teste
       listaPredecessores[(int(linha[1])-1)] = destinoTeste

#FOI
def imprimir(vertice):
   global grauSaida, grauEntrada

   aux = listaSucessores[int(vertice)-1]
   sucessores = []

   if verificaSucessores(int(vertice)):
     pesquisaDosSucessores(aux, sucessores)
     print("Sucessores -> ")
     for sucessor in sucessores:
      print("- " + sucessor + " -")
   else:
      print("erro")
   grauSaida = len(sucessores)
   
   #predecessores
   aux = listaPredecessores[int(vertice)-1]
   predecessores = []

   if verificaPredecessores(int(vertice)):
     pesquisaDosPredecessores(aux, predecessores)
     print("Predecessores -> ")
     for predecessor in predecessores:
      print("- " + predecessor + " -")
   else:
      print("erro")
   grauEntrada  = len(predecessores) 
   

class sucessor:
  sucessor = None
  vertice = None

class predecessor:
  vertice = None
  predecessor = None


path = sys.argv[1]
vertice = sys.argv[2]
with open(path) as file:
  linha = file.readlines()

trigger = False
for i in range(0, len(linha)-1):
  trim = linha[i].strip()
  linhaLimpa = trim.split()
  if trigger == False:
    inicializador(int(linhaLimpa[1]))
    trigger = True
  else:
    criar(linhaLimpa)

print("informações para o vertice " + vertice)
imprimir(vertice)
print("Grau de Saida: " + str(grauSaida))
print("Grau de Entrada: " + str(grauEntrada))
