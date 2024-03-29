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
layout = {
            'piraeus':[0,2],'faliro':[5,3],'moschato':[7,5],'kallithea':[8,6],'tavros':[10,7],'petralona':[12, 9],'thissio':[12.25, 11],'monastiraki':[12.25, 13],
            'omonia':[12.25, 15], 'victoria':[12.25,17], 'aghios nikolaos':[10,21], 'kato patissia':[11,22],
            'aghios eleftherios':[12,24], 'ano patissia':[14.5,25], 'perissos':[16,26], 'pefkakia':[17.5,27], 'nea ionia':[19,28], 'iraklio':[20,29],
            'irini':[20.5,34], 'neratziotissa':[21,36], 'maroussi':[23,38], 'kat': [25,40], 'kifissia': [27,42],
            'aghios antonios': [5, 24], 'sepolia': [7, 22], 'attiki': [9, 20], 'larissa st.': [9, 18], 'metaxourghio': [9, 16], 'panepistimio': [13.5, 13],
            'syntagma': [14.5, 12], 'akropoli': [14.5, 10], 'sygroy - fix': [14.5, 8], 'neos kosmos': [14.5, 6], 'aghios ioannis': [14.5, 4],
            'dafni': [14.5, 2], 'aghios dimitrios': [14.5, 0],
            'egaleo': [2,18], 'eleonas': [5,15], 'kerameikos': [7,13], 'evangelismos':[19, 12], 'megaro moussikis': [20.5,13], 'ambelokipi': [22,14], 'panormou': [23,15],
            'katehaki': [24,16], 'ethniki amyna': [25,17], 'holargos': [26,18], 'nomismatokopio': [27,19], 'aghia paraskevi': [28,20],
            'halandri': [29,21], 'douk. plakentias': [31,23], 'pallini': [34,21.5], 'peania - kantza': [34,19], 'koropi': [34,13], 'airport':[38,11]
        }
label_layout = {
            'piraeus':[0,1],'faliro':[5,2],'moschato':[6.5,5],'kallithea':[7.8,6.5],'tavros':[9.7,7.3],'petralona':[11.6, 9],'thissio':[12, 11],'monastiraki':[12.1, 13.5],
            'omonia':[12.1, 15], 'victoria':[12.1,17], 'aghios nikolaos':[14,20.5], 'kato patissia':[11,22.8],
            'aghios eleftherios':[12,25], 'ano patissia':[14.5,26], 'perissos':[16,27], 'pefkakia':[17.5,28], 'nea ionia':[19,29], 'iraklio':[20,30],
            'irini':[20,34], 'neratziotissa':[20.5,36], 'maroussi':[22.5,38], 'kat': [24.5,40], 'kifissia': [26.5,42],
            'aghios antonios': [4.6, 24], 'sepolia': [6.5, 22], 'attiki': [8.5, 20], 'larissa st.': [8.8, 18], 'metaxourghio': [8.8, 16], 'panepistimio': [16, 14],
            'syntagma': [14.5, 12], 'akropoli': [14.5, 10], 'sygroy - fix': [14.5, 8], 'neos kosmos': [14, 6], 'aghios ioannis': [14, 4],
            'dafni': [14, 2], 'aghios dimitrios': [14, 0],
            'egaleo': [1.6,18], 'eleonas': [4.6,15], 'kerameikos': [6.6,13], 'evangelismos':[19, 11], 'megaro moussikis': [20.2,13.5], 'ambelokipi': [22,15], 'panormou': [23,16],
            'katehaki': [24,17], 'ethniki amyna': [25,18], 'holargos': [26,19], 'nomismatokopio': [27,20], 'aghia paraskevi': [28,21],
            'halandri': [29,22], 'douk. plakentias': [31,24], 'pallini': [33.5,21], 'peania - kantza': [33.5,19], 'koropi': [33.3,13], 'airport':[38,10]
        }
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
    def __init__(self, adyacentes_lista):
        self.adjacentes_lista = adyacentes_lista
        self.h_values = data_frame


    def adyacentes(self, node):
        '''METODO QUE OBTIENE LOS NODOS ADYACENTES DE NODE'''
        return self.adjacentes_lista[node]


    def funcion_h(self, from_node, to_node):
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
        padres = {}
        padres[from_node] = from_node

        # Bucle principal
        while len(open_list) > 0:
            # Nodo que se evalúa
            node = None

            # Se busca el nodo con menor f value de la open list
            # Siendo f = g + h
            for next_node in open_list:
                if node is None or \
                    g_value[next_node] + self.funcion_h(next_node, to_node) \
                        < \
                    g_value[node] + self.funcion_h(node, to_node):

                    node = next_node

            # Si es el nodo meta, se reconstruye el camino seguido
            # y termina la ejecución
            if node == to_node:
                while padres[node] != node:
                    reconst_path.append(node)
                    node = padres[node]

                reconst_path.append(from_node)
                reconst_path.reverse()
                return reconst_path

            # Se evalúan los nodos adyacentes al nodo
            for (hijo, coste) in self.adyacentes(node):
                # Si no está en open ni closed significa que no se ha expandido
                if hijo not in open_list and hijo not in close_list:
                    open_list.add(hijo)
                    padres[hijo] = node
                    g_value[hijo] = g_value[node] + coste

                # Si está, se evalúa si se ha encontrado un mejor camino hacia él
                else:
                    if g_value[hijo] > g_value[node] + coste:
                        g_value[hijo] = g_value[node] + coste
                        padres[hijo] = node

                        # Si ya estaba en la closed, se quita, es necesario volver a evaluar
                        if hijo in close_list:
                            close_list.remove(hijo)
                            open_list.add(hijo)

            open_list.remove(node)
            close_list.add(node)


        print('Path does not exist!')
        return None
