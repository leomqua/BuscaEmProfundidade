class GrafoListaAdjacencia:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)

        if destino not in self.adjacencias[origem]:
            self.adjacencias[origem].append(destino)
        if origem not in self.adjacencias[destino]:
            self.adjacencias[destino].append(origem)

    def vizinhos(self, vertice):
        if vertice not in self.adjacencias:
            raise KeyError(f"Vértice inexistente: {vertice}")
        return list(self.adjacencias[vertice])

    def busca_em_profundidade(self, inicio):
        if inicio not in self.adjacencias:
            raise KeyError(f"Vértice inexistente: {inicio}")

        visitados = []
        pilha = [inicio]
        visitados_set = set()

        while pilha:
            vertice = pilha.pop()

            if vertice in visitados_set:
                continue

            visitados.append(vertice)
            visitados_set.add(vertice)

            for vizinho in reversed(self.adjacencias[vertice]):
                if vizinho not in visitados_set:
                    pilha.append(vizinho)

        return visitados

    def possui_ciclo(self, inicio=None):
        if not self.adjacencias:
            return False

        if inicio is not None:
            if inicio not in self.adjacencias:
                raise KeyError(f"Vértice inexistente: {inicio}")
            vertices = [inicio]
        else:
            vertices = list(self.adjacencias)

        visitados = set()

        for raiz in vertices:
            if raiz in visitados:
                continue

            pilha = [{"vertice": raiz, "pai": None}]

            while pilha:
                item = pilha.pop()
                vertice = item["vertice"]
                pai = item["pai"]

                if vertice in visitados:
                    continue

                visitados.add(vertice)

                for vizinho in self.adjacencias[vertice]:
                    if vizinho not in visitados:
                        pilha.append({"vertice": vizinho, "pai": vertice})
                    elif vizinho != pai:
                        return True

        return False


def grafo_da_atividade():
    grafo = GrafoListaAdjacencia()
    arestas = [
        ("V1", "V2"),
        ("V1", "V3"),
        ("V1", "V6"),
        ("V2", "V3"),
        ("V2", "V4"),
        ("V2", "V6"),
        ("V2", "V7"),
        ("V4", "V5"),
        ("V5", "V6"),
        ("V5", "V8"),
        ("V6", "V7"),
        ("V7", "V8"),
    ]

    for origem, destino in arestas:
        grafo.adicionar_aresta(origem, destino)

    return grafo


if __name__ == "__main__":
    grafo = grafo_da_atividade()
    print("Ordem da busca em profundidade:", grafo.busca_em_profundidade("V1"))
    print("O grafo possui ciclo:", grafo.possui_ciclo())
