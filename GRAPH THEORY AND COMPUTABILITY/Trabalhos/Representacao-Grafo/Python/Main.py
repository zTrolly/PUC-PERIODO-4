import sys
import os.path

# global lists
listaPredecessores = []
listaSucessores = []

#utility
ultimoVertice = None
grauDeSaida = 0
grauDeEntrada = 0

#logica vertice
def verficaVertice(linha):
    global ultimoVertice

    if ultimoVertice == None:
      ultimoVertice = linha
      return 2
    elif ultimoVertice != linha:
      ultimoVertice = linha
      return 1
    else:
      ultimoVertice = linha
      return 0

#logica dos predecessores
def inicializaListaPredecessores(qtdPredecessores):
    global listaPredecessores
    listaPredecessores = [] * (qtdPredecessores -1)
    return listaPredecessores

def verficaPredecessores(predecessor):
    global listaPredecessores
    if predecessor in listaPredecessores:
        return True
    else:
        return False

def adicionaPredecessores(vertice, predecessor):
    if vertice.predecessor == None:
        vertice.predecessor = predecessor
        return
    else:
        adicionaPredecessores(vertice.predecessor, predecessor)

def pesquisaPredecessor(destino, predecessores):
  if destino.vertice != None:
    if destino.predecessor != None:
      predecessores.append(destino.predecessor.vertice)
      pesquisaPredecessor(destino.predecessor, predecessores)
  else:
    return

#logica dos sucessores
def verificaSucessores(sucessor):
    global listaSucessores
    if sucessor in listaSucessores:
        return True
    else:
        return False

def pesquisaSucessores(origem, sucessores):
  if origem.vertice != None:
    if origem.sucessor != None:
      sucessores.append(origem.sucessor.vertice)
      pesquisaSucessores(origem.sucessor, sucessores)
  else:
    return

#logica aresta / sucessor
def criaAresta(origem, destino):
  if origem.sucessor == None:
    origem.sucessor = destino
    return
  else:
    criaAresta(origem.sucessor, destino)

class predecessor:
    def __init__(self, predecessor, vertice):
        self.predecessor = predecessor
        self.vertice = vertice

class sucessor:
    def __init__(self, sucessor, vertice):
        self.sucessor = sucessor
        self.predecessor = vertice

def criarLista(linha):
  if verficaVertice(linha[0]) == 2 & linha != None:
    origemSucessor = sucessor()
    destino = sucessor()

    origemSucessor.vertice = linha[0]
    destino.vertice = linha[1]

    destino.sucessor = None
    origemSucessor.sucessor = destino

    sucessor.append(origemSucessor)    

   
    destinoPredecessor = predecessor()
    origemPredecessor = predecessor()

    destinoPredecessor.vertice = linha[1]
    origemPredecessor.vertice = linha[0]

    destinoPredecessor.predecessor = origemPredecessor
    predecessor.insert(int(linha[1])-1, origemPredecessor)   

  elif verficaVertice(linha[0]) == 0 & linha != None:
    destino = sucessor()
    destino.vertice = linha[1]

    origem = listaSucessores[len(listaSucessores)-1]
    criaAresta(origem, destino)

  else:
    origem = sucessor()
    destino = sucessor()

    origem.vertice = linha[0]
    destino.vertice = linha[1]

    origem.sucessor = destino
    listaSucessores.append(origem)
  
  if verficaVertice(linha[0]) != 	2 & linha != None:
      if verficaPredecessores(int(linha[1])):
       predecessor = predecessor()
       predecessor.vertice = linha[0]
       adicionaPredecessores(listaPredecessores[(int(linha[1])-1)], predecessor)
      else:
       destino = predecessor()
       origem = predecessor()
       origem.vertice = linha[0]
       destino.vertice = linha[1]
       destino.predecessor = origem
       listaPredecessores[(int(linha[1])-1)] = destino

def printGeral(vertice):
  global grauDeSaida
  global grauDeEntrada

  aux = listaPredecessores[int(vertice)-1]
  predecessores = []

  if verficaPredecessores(int(vertice)):
    pesquisaPredecessor(aux, predecessores)
    print("Predecessores -> ")
    for i in predecessores:
      print("-" + i + "-")
      print("")
  else:
    print("ERROR")
  grauDeSaida = len(predecessores) 
   #SUCESSORES
  aux = listaSucessores[int(vertice)-1]
  sucessores = []

  if verificaSucessores(int(vertice)):
    pesquisaSucessores(aux, sucessores)
    print("Sucessores -> ")
    for i in sucessores:
      print("-" + i + "-")
      print("")
  else:
    print("ERROR")
  grauDeEntrada = len(sucessores)





