#Diego Maldonado
import networkx as nx
import matplotlib.pyplot as plt

# Definición de la función de Kruskal para encontrar el MST
def kruskal(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    ET = set()  # Conjunto de aristas en el MST
    ecounter = 0  # Contador de aristas
    total_weight = 0  # Peso total del MST

    while ecounter < len(G.nodes) - 1:
        edge = sorted_edges.pop(0)
        if not forms_cycle(ET, edge):
            ET.add((edge[0], edge[1]))
            total_weight += edge[2]['weight']
            ecounter += 1

    return ET, total_weight

# Función para verificar si agregar una arista crea un ciclo en el MST
def forms_cycle(tree, edge):
    temp_graph = nx.Graph(list(tree))
    temp_graph.add_edge(*edge[:2], weight=edge[2]['weight'])
    return not nx.is_forest(temp_graph)

# Crear un grafo vacío
G = nx.Graph()
ciudades = ['Monterrey', 'Guadalajara', 'Puebla', 'Villahermosa', 'Campeche', 'Merida']

# Agregar los nodos (ciudades) al grafo
for ciudad in ciudades:
    G.add_node(ciudad)

# Agregar aristas con pesos
G.add_edge('Monterrey', 'Guadalajara', weight=800)
G.add_edge('Monterrey', 'Puebla', weight=1000)
G.add_edge('Guadalajara', 'Puebla', weight=600)
G.add_edge('Guadalajara', 'Villahermosa', weight=1300)
G.add_edge('Puebla', 'Villahermosa', weight=600)
G.add_edge('Villahermosa', 'Campeche', weight=300)
G.add_edge('Villahermosa', 'Merida', weight=500)
G.add_edge('Campeche', 'Merida', weight=100)

# Dibujar el grafo original con sus respectivos pesos
pos = nx.spring_layout(G)
plt.figure()
plt.title("Grafo Original")
labels = {}
edge_labels = {}
for u, v, data in G.edges(data=True):
    edge_labels[(u, v)] = data['weight']
labels = {node: node for node in G.nodes()}
nx.draw(G, pos, with_labels=True, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Calcular el MST utilizando el algoritmo de Kruskal
minimum_spanning_tree, weight = kruskal(G)

# Crear una copia del grafo original para el MST
MST = G.copy()

# Eliminar las aristas que no están en el MST
for edge in G.edges:
    if edge not in minimum_spanning_tree:
        MST.remove_edge(*edge)

# Dibujar el MST
plt.figure()
plt.title("Árbol de Expansión Mínima")
labels = {}
edge_labels = {}
for u, v, data in MST.edges(data=True):
    edge_labels[(u, v)] = data['weight']
labels = {node: node for node in MST.nodes()}
nx.draw(MST, pos, with_labels=True, labels=labels)
nx.draw_networkx_edge_labels(MST, pos, edge_labels=edge_labels)

# Mostrar el peso total del MST
print("Peso total del Árbol de Expansión Mínima:", weight)
plt.show()
