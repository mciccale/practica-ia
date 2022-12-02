import networkx as nx
from get_data import get_data

data_frame: dict = get_data()

# Velocidad media de los trenes de Atenas expresada en Kilómetros / Minutos

# Como los datos nos dicen el tiempo entre estaciones en minutos, calculamos
# una distancia aproximada usando la velocidad media
VELOCITY = 1.3333

G = nx.Graph()
nodos = [
    'piraeus','faliro','moschato','kallithea','tavros','petralona','thissio','monastiraki',
    'omonia', 'victoria', 'aghios nikolaos', 'kato patissia',
    'aghios eleftherios', 'ano patissia', 'perissos', 'pefkakia', 'nea ionia', 'iraklio',
    'irini', 'neratziotissa', 'maroussi', 'kat', 'kifissia',
    'aghios antonios', 'sepolia', 'attiki', 'larissa st.', 'metaxourghio', 'panepistimio',
    'syntagma', 'akropoli', 'sygroy - fix', 'neos kosmos', 'aghios ioannis',
    'dafni', 'aghios dimitrios', 'egaleo', 'eleonas', 'kerameikos', 'evangelismos',
    'megaro moussikis', 'ambelokipi',
    'panormou', 'katehaki', 'ethniki amyna', 'holargos', 'nomismatokopio',
    'aghia paraskevi',
    'halandri', 'douk. plakentias', 'pallini', 'peania - kantza', 'koropi', 'airport',
]
aristas = [
    ('piraeus','faliro',VELOCITY*4),
    ('faliro','piraeus',VELOCITY*3),
    ('faliro','moschato',VELOCITY*3),
    ('moschato','faliro',VELOCITY*3),
    ('moschato','kallithea',VELOCITY*2),
    ('kallithea','moschato',VELOCITY*2),
    ('kallithea','tavros',VELOCITY*2),
    ('tavros','kallithea',VELOCITY*2),
    ('tavros','petralona',VELOCITY*2),
    ('petralona','tavros',VELOCITY*2),
    ('petralona','thissio',VELOCITY*2),
    ('thissio','petralona',VELOCITY*2),
    ('thissio','monastiraki',VELOCITY*2),
    ('monastiraki','thissio',VELOCITY*2),
    ('monastiraki','omonia',VELOCITY*2),
    ('monastiraki','kerameikos',VELOCITY*2),
    ('monastiraki','syntagma',VELOCITY*3),
    ('omonia','monastiraki',VELOCITY*2),
    ('omonia','victoria',VELOCITY*2),
    ('omonia','metaxourghio',VELOCITY*2),
    ('omonia','panepistimio',VELOCITY*1),
    ('victoria','omonia',VELOCITY*2),
    ('victoria','attiki',VELOCITY*3),
    ('attiki', 'victoria',VELOCITY*3),
    ('attiki', 'aghios nikolaos',VELOCITY*2),
    ('attiki', 'sepolia',VELOCITY*1),
    ('attiki', 'larissa st.',VELOCITY*2),
    ('aghios nikolaos', 'attiki',VELOCITY*2),
    ('aghios nikolaos', 'kato patissia',VELOCITY*2),
    ('kato patissia', 'aghios nikolaos',VELOCITY * 2),
    ('kato patissia', 'aghios eleftherios',VELOCITY * 2),
    ('aghios eleftherios', 'kato patissia',VELOCITY * 2),
    ('aghios eleftherios', 'ano patissia',VELOCITY * 1),
    ('ano patissia', 'aghios eleftherios',VELOCITY * 1),
    ('ano patissia', 'perissos',VELOCITY * 3),
    ('perissos', 'ano patissia',VELOCITY * 3),
    ('perissos', 'pefkakia',VELOCITY * 1),
    ('pefkakia', 'perissos',VELOCITY * 1),
    ('pefkakia', 'nea ionia',VELOCITY * 2),
    ('nea ionia', 'pefkakia',VELOCITY * 2),
    ('nea ionia', 'iraklio',VELOCITY * 2),
    ('iraklio', 'nea ionia',VELOCITY * 2),
    ('iraklio', 'irini',VELOCITY * 3),
    ('irini', 'iraklio',VELOCITY * 3),
    ('irini', 'neratziotissa',VELOCITY * 2),
    ('neratziotissa', 'irini',VELOCITY * 2),
    ('neratziotissa', 'maroussi',VELOCITY * 3),
    ('maroussi', 'neratziotissa',VELOCITY * 3),
    ('maroussi', 'kat',VELOCITY * 2),
    ('kat', 'maroussi',VELOCITY * 2),
    ('kat', 'kifissia',VELOCITY * 2),
    ('sepolia','aghios antonios', VELOCITY*2),
    ('sepolia','attiki', VELOCITY*1),
    ('larissa st.','attiki', VELOCITY*2),
    ('larissa st.','metaxourghio', VELOCITY*1),
    ('metaxourghio','larissa st.', VELOCITY*1),
    ('metaxourghio','omonia', VELOCITY*2),
    ('panepistimio','omonia', VELOCITY*1),
    ('panepistimio','syntagma', VELOCITY*2),
    ('syntagma','panepistimio', VELOCITY*2),
    ('syntagma','akropoli', VELOCITY*1),
    ('syntagma','monastiraki', VELOCITY*3),
    ('syntagma','evangelismos', VELOCITY*1),
    ('akropoli','syntagma', VELOCITY*1),
    ('akropoli','sygroy - fix', VELOCITY*2),
    ('sygroy - fix','akropoli', VELOCITY*2),
    ('sygroy - fix','neos kosmos', VELOCITY*1),
    ('neos kosmos','sygroy - fix', VELOCITY*1),
    ('neos kosmos','aghios ioannis', VELOCITY*1),
    ('aghios ioannis','neos kosmos', VELOCITY*1),
    ('aghios ioannis','dafni', VELOCITY*2),
    ('dafni','aghios ioannis', VELOCITY*2),
    ('dafni','aghios dimitrios', VELOCITY*2),
    ('aghios dimitrios','dafni', VELOCITY*2),
    ('egaleo','eleonas', VELOCITY*2),
    ('eleonas','egaleo', VELOCITY*2),
    ('eleonas','kerameikos', VELOCITY*2),
    ('kerameikos','eleonas', VELOCITY*2),
    ('kerameikos','monastiraki', VELOCITY*2),
    ('evangelismos','syntagma', VELOCITY*1),
    ('evangelismos','megaro moussikis', VELOCITY*1),
    ('megaro moussikis','evangelismos', VELOCITY*1),
    ('megaro moussikis','ambelokipi', VELOCITY*2),
    ('ambelokipi','megaro moussikis', VELOCITY*2),
    ('ambelokipi','panormou', VELOCITY*1),
    ('panormou','ambelokipi', VELOCITY*1),
    ('panormou','katehaki', VELOCITY*2),
    ('katehaki','panormou', VELOCITY*2),
    ('katehaki','ethniki amyna', VELOCITY*2),
    ('ethniki amyna','katehaki', VELOCITY*2),
    ('ethniki amyna','holargos', VELOCITY*2),
    ('holargos','ethniki amyna', VELOCITY*2),
    ('holargos','nomismatokopio', VELOCITY*1),
    ('nomismatokopio','holargos', VELOCITY*1),
    ('nomismatokopio','aghia paraskevi', VELOCITY*2),
    ('aghia paraskevi','nomismatokopio', VELOCITY*2),
    ('aghia paraskevi','halandri', VELOCITY*2),
    ('halandri','aghia paraskevi', VELOCITY*2),
    ('halandri','douk. plakentias', VELOCITY*1),
    ('douk. plakentias','halandri', VELOCITY*1),
    ('douk. plakentias','pallini', VELOCITY*6),
    ('pallini','douk. plakentias', VELOCITY*6),
    ('pallini','peania - kantza', VELOCITY*3),
    ('peania - kantza','pallini', VELOCITY*3),
    ('peania - kantza','koropi', VELOCITY*6),
    ('koropi','peania - kantza', VELOCITY*6),
    ('koropi','airport', VELOCITY*5),
]
G.add_nodes_from(nodos)
G.add_weighted_edges_from(aristas)

graph = {
    'piraeus': [
        ('faliro', VELOCITY*4)
    ],
    'faliro': [
        ('piraeus', VELOCITY*3),
        ('moschato', VELOCITY*3)
    ],
    'moschato': [
        ('faliro', VELOCITY*3),
        ('kallithea', VELOCITY*2)
    ],
    'kallithea': [
        ('moschato', VELOCITY*2),
        ('tavros', VELOCITY*2)
    ],
    'tavros': [
        ('kallithea', VELOCITY*2),
        ('petralona', VELOCITY*2)
    ],
    'petralona': [
        ('tavros', VELOCITY*2),
        ('thissio', VELOCITY*2)
    ],
    'thissio': [
        ('petralona', VELOCITY*2),
        ('monastiraki', VELOCITY*2)
    ],
    'monastiraki': [
        ('thissio', VELOCITY*2),
        ('omonia', VELOCITY*2),
        ('kerameikos', VELOCITY*2),
        ('syntagma', VELOCITY*3)
    ],
    'omonia': [
        ('monastiraki', VELOCITY*2),
        ('victoria', VELOCITY*2),
        ('metaxourghio', VELOCITY*2),
        ('panepistimio', VELOCITY*1)
    ],
    'victoria': [
        ('omonia', VELOCITY*2),
        ('attiki', VELOCITY*3)
    ],
    'attiki': [
        ('victoria', VELOCITY*3),
        ('aghios nikolaos', VELOCITY*2),
        ('sepolia', VELOCITY*1),
        ('larissa st.', VELOCITY*2)
    ],
    'aghios nikolaos': [
        ('attiki', VELOCITY*2),
        ('kato patissia', VELOCITY*2)
    ],
    'kato patissia': [
        ('aghios nikolaos', VELOCITY*2),
        ('aghios eleftherios', VELOCITY*2)
    ],
    'aghios eleftherios': [
        ('kato patissia', VELOCITY*2),
        ('ano patissia', VELOCITY*1)
    ],
    'ano patissia': [
        ('aghios eleftherios', VELOCITY*1),
        ('perissos', VELOCITY*3)
    ],
    'perissos': [
        ('ano patissia', VELOCITY*3),
        ('pefkakia', VELOCITY*1)
    ],
    'pefkakia': [
        ('perissos', VELOCITY*1),
        ('nea ionia', VELOCITY*2)
    ],
    'nea ionia': [
        ('pefkakia', VELOCITY*2),
        ('iraklio', VELOCITY*2)
    ],
    'iraklio': [
        ('nea ionia', VELOCITY*2),
        ('irini', VELOCITY*3)
    ],
    'irini': [
        ('iraklio', VELOCITY*3),
        ('neratziotissa', VELOCITY*2)
    ],
    'neratziotissa': [
        ('irini', VELOCITY*2),
        ('maroussi', VELOCITY*3)
    ],
    'maroussi': [
        ('neratziotissa', VELOCITY*3),
        ('kat', VELOCITY*2)
    ],
    'kat': [
        ('maroussi', VELOCITY*2),
        ('kifissia', VELOCITY*2)
    ],
    'kifissia': [
        ('kat', VELOCITY*2)
    ],
    'anthoupoli': [
        ('peristeri', VELOCITY*1)
    ],
    'peristeri': [
        ('anthoupoli', VELOCITY*1),
        ('aghios antonios', VELOCITY*1)
    ],
    'aghios antonios': [
        ('peristeri', VELOCITY*1),
        ('sepolia', VELOCITY*2)
    ],
    'sepolia': [
        ('aghios antonios', VELOCITY*2),
        ('attiki', VELOCITY*1)
    ],
    'larissa st.': [
        ('attiki', VELOCITY*2),
        ('metaxourghio', VELOCITY*1)
    ],
    'metaxourghio': [
        ('larissa st.', VELOCITY*1),
        ('omonia', VELOCITY*2)
    ],
    'panepistimio': [
        ('omonia', VELOCITY*1),
        ('syntagma', VELOCITY*2)
    ],
    'syntagma': [
        ('panepistimio', VELOCITY*2),
        ('akropoli', VELOCITY*1),
        ('monastiraki', VELOCITY*3),
        ('evangelismos', VELOCITY*1)
    ],
    'akropoli': [
        ('syntagma', VELOCITY*1),
        ('sygroy - fix', VELOCITY*2)
    ],
    'sygroy - fix': [
        ('akropoli', VELOCITY*2),
        ('neos kosmos', VELOCITY*1)
    ],
    'neos kosmos': [
        ('sygroy - fix', VELOCITY*1),
        ('aghios ioannis', VELOCITY*1)
    ],
    'aghios ioannis': [
        ('neos kosmos', VELOCITY*1),
        ('dafni', VELOCITY*2)
    ],
    'dafni': [
        ('aghios ioannis', VELOCITY*2),
        ('aghios dimitrios', VELOCITY*2)
    ],
    'aghios dimitrios': [
        ('dafni', VELOCITY*2)
    ],
    'egaleo': [
        ('eleonas', VELOCITY*2)
    ],
    'eleonas': [
        ('egaleo', VELOCITY*2),
        ('kerameikos', VELOCITY*2)
    ],
    'kerameikos': [
        ('eleonas', VELOCITY*2),
        ('monastiraki', VELOCITY*2)
    ],
    'evangelismos': [
        ('syntagma', VELOCITY*1),
        ('megaro moussikis', VELOCITY*1)
    ],
    'megaro moussikis': [
        ('evangelismos', VELOCITY*1),
        ('ambelokipi', VELOCITY*2)
    ],
    'ambelokipi': [
        ('megaro moussikis', VELOCITY*2),
        ('panormou', VELOCITY*1)
    ],
    'panormou': [
        ('ambelokipi', VELOCITY*1),
        ('katehaki', VELOCITY*2)
    ],
    'katehaki': [
        ('panormou', VELOCITY*2),
        ('ethniki amyna', VELOCITY*2)
    ],
    'ethniki amyna': [
        ('katehaki', VELOCITY*2),
        ('holargos', VELOCITY*2)
    ],
    'holargos': [
        ('ethniki amyna', VELOCITY*2),
        ('nomismatokopio', VELOCITY*1)
    ],
    'nomismatokopio': [
        ('holargos', VELOCITY*1),
        ('aghia paraskevi', VELOCITY*2)
    ],
    'aghia paraskevi': [
        ('nomismatokopio', VELOCITY*2),
        ('halandri', VELOCITY*2)
    ],
    'halandri': [
        ('aghia paraskevi', VELOCITY*2),
        ('douk. plakentias', VELOCITY*1)
    ],
    'douk. plakentias': [
        ('halandri', VELOCITY*1),
        ('pallini', VELOCITY*6)
    ],
    'pallini': [
        ('douk. plakentias', VELOCITY*6),
        ('peania - kantza', VELOCITY*3)
    ],
    'peania - kantza': [
        ('pallini', VELOCITY*3),
        ('koropi', VELOCITY*6)
    ],
    'koropi': [
        ('peania - kantza', VELOCITY*6),
        ('airport', VELOCITY*5)
    ],
    'airport': [
        ('koropi', VELOCITY*5)
    ]
}

reconst_path = []

class Graph:
    '''CLASE QUE IMPLEMENTA UN GRAFO PARA HACER A*'''
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.h_values = data_frame


    def adjacents(self, node):
        '''METODO QUE OBTIENE LOS NODOS ADYACENTES DE NODE'''
        return self.adjacency_list[node]


    def h_function(self, from_node, to_node):
        '''GET H_VALUE'''
        return self.h_values[from_node][to_node]


    def a_star(self, from_node, to_node):
        '''IMPLEMENTATION OF A*'''
        open_list = set([from_node])
        close_list = set([])

        # Se inicializa diccionario para los g_value
        g_value = {}
        g_value[from_node] = 0

        # Se inicializa diccionario para guardar el recorrido
        parents = {}
        parents[from_node] = from_node

        # Bucle principal
        while len(open_list) > 0:
            # Nodo que se evalúa
            node = None

            # Se busca el nodo con menor f value de la open list
            # Siendo f = g + h
            for next_node in open_list:
                if node is None or \
                    g_value[next_node] + self.h_function(next_node, to_node) \
                        < \
                    g_value[node] + self.h_function(node, to_node):

                    node = next_node

            # Si es el nodo meta, se reconstruye el camino seguido
            # y termina la ejecución
            if node == to_node:
                while parents[node] != node:
                    reconst_path.append(node)
                    node = parents[node]

                reconst_path.append(from_node)
                reconst_path.reverse()
                return reconst_path

            # Se evalúan los nodos adyacentes al nodo
            for (child, cost) in self.adjacents(node):
                # Si no está en open ni closed significa que no se ha expandido
                if child not in open_list and child not in close_list:
                    open_list.add(child)
                    parents[child] = node
                    g_value[child] = g_value[node] + cost

                # Si está, se evalúa si se ha encontrado un mejor camino hacia él
                else:
                    if g_value[child] > g_value[node] + cost:
                        g_value[child] = g_value[node] + cost
                        parents[child] = node

                        # Si ya estaba en la closed, se quita, es necesario volver a evaluar
                        if child in close_list:
                            close_list.remove(child)
                            open_list.add(child)


            open_list.remove(node)
            close_list.add(node)


        print('Path does not exist!')
        return None
