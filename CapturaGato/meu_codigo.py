import importlib
import heapq
import sys

class Mod: 
    cat    = eval(sys.argv[1])
    blocks = eval(sys.argv[2])
    exits  = eval(sys.argv[3])


class Campo:
    def __init__(self, Mod):
        self.edges = {}
        
        for x in range(11):
            for y in range(11):
                if self.verify_blocked((x,y)):
                    a = (x,y)
                    self.edges[a] = a
        
    def verify_blocked (self, a) :
        if ((a in Mod.blocks) or (a[0] > 10) or (a[1] > 10) or (a[0] < 0) or (a[1] < 0)):
            return True
        return False
    
    def vizinhos(self, cat):
        vizinhos = []
        if cat[0] % 2 == 0 :
            candidatos = [
            (cat[0] - 1, cat[1] - 1, "NW"),
            (cat[0] - 1, cat[1],     "NE"),
            (cat[0], cat[1] - 1,     "W"),
            (cat[0], cat[1] + 1,     "E"),
            (cat[0] + 1, cat[1] - 1, "SW"),
            (cat[0] + 1, cat[1],     "SE")
        ]
        else :
            candidatos = [
            (cat[0] - 1, cat[1],     "NW"),
            (cat[0] - 1, cat[1] + 1, "NE"),
            (cat[0], cat[1] - 1,     "W"),
            (cat[0], cat[1] + 1,     "E"),
            (cat[0] + 1, cat[1],     "SW"),
            (cat[0] + 1, cat[1]+1,   "SE")
        ]
        
        for el in candidatos :
            a = (el[0] , el[1])
            if not (self.verify_blocked(a)):
                vizinhos.append((el[0], el[1], el[2]))
        ##print(vizinhos)
        return vizinhos


class GridWithWeights(Campo):
    def __init__(self):
       Campo.__init__(self, Mod)
       self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    

def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        cat = (current[0], current[1])
       
        if cat == goal:
            break
        
        for next in graph.vizinhos(cat):                 
            prox = (next[0],next[1])
            new_cost = cost_so_far[cat] + graph.cost(cat, prox)
            if prox not in cost_so_far or new_cost < cost_so_far[prox]:
                cost_so_far[prox] = new_cost
                priority = new_cost
                frontier.put(prox, priority)
                came_from[prox] = cat

    return came_from


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []

    while current != start:
        try:    
            path.append(current)
            current = came_from[current]
        except Exception:
            path = []
            return path
    path.append(start) # optional
    path.reverse() # optional
    return path
           
       
def calculoMenorCaminho (grafo, cat, saidas):
    tamanhoMenorCaminho = 999
    melhorCaminho = {}
    for el in list(saidas):
        caminho = reconstruct_path(dijkstra_search(grafo, cat, el), cat, el)
        if len(caminho) > 0:
            if (len(caminho)-1) < tamanhoMenorCaminho:
                tamanhoMenorCaminho = (len(caminho)-1)
                melhorCaminho = caminho

    return melhorCaminho                


def bloquearCasa (grafo, caminho, outrasSaidas):
    cat = caminho[0]
    melhorBlock = caminho[-1]
    proximoProximo = calculoMenorCaminho(grafo, cat, outrasSaidas)


    for el in caminho: #verificando o melhor caminho a partir de cada casa, para marcar no mesmo
        aux = calculoMenorCaminho(grafo, el, outrasSaidas)
        if (len(aux) < len(proximoProximo)):
            proximoProximo = aux
            melhorBlock = proximoProximo[0]    
            

    
    Mod.blocks.append(melhorBlock)
    print (melhorBlock)    
    #executarDJKSearch() #chamada recursiva para teste
        

def executarDJKSearch():
    grafo = GridWithWeights()
    b = (Mod.cat[0], Mod.cat[1])
    saidas = Mod.exits
    melhorCaminho = calculoMenorCaminho(grafo, b, Mod.exits)
    if len(melhorCaminho) == 0:
       # print("Gato preso")
        return 0
    else:
        saidas.remove(melhorCaminho[-1])
        bloquearCasa(grafo, melhorCaminho, saidas)
     



executarDJKSearch()

