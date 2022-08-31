import sys
import os.path

# global lists
listaPredecessores = []
listaSucessores = []

#variaveis globais
ultimoVertice = None

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


