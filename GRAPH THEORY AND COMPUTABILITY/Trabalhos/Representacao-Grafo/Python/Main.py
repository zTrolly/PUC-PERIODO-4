import sys
import os.path

# global lists
listaPredecessores = []
listaSucessores = []

#variaveis globais
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

#logica dos sucessores
def verificaSucessores(sucessor):
    global listaSucessores
    if sucessor in listaSucessores:
        return True
    else:
        return False

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






