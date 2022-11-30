from get_data import get_data
import networkx as nx

data_frame: dict = get_data()

# Velocidad media de los trenes de Atenas expresada en Kilómetros / Minutos

# Como los datos nos dicen el tiempo entre estaciones en minutos, calculamos
# una distancia aproximada usando la velocidad media
VELOCITY = 1.3333

G = nx.MultiGraph()
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
    ('akropoli','sygroy', VELOCITY*2),
    ('sygroy - fix','akropoli', VELOCITY*2),
    ('sygroy - fix','neos kosmos', VELOCITY*1),
    ('neos kosmos','sygroy - fix', VELOCITY*1),
    ('neos kosmos','aghios ioannis', VELOCITY*1),
    ('aghios ioannis','neos kosmos', VELOCITY*1),
    ('aghios ioannis','dafni', VELOCITY*2),
    ('dafni','aghios ioannis', VELOCITY*2),
    ('dafni','aghios dimitrios', VELOCITY*2),
    ('aghios dimitrios','dafni', VELOCITY*2),
    ('aghios dimitrios','ilioupoli', VELOCITY*2),
    ('ilioupoli','aghios dimitrios', VELOCITY*2),
    ('ilioupoli','alimos', VELOCITY*1),
    ('alimos','ilioupoli', VELOCITY*1),
    ('alimos','argyoupoli', VELOCITY*3),
    ('argyoupoli','alimos', VELOCITY*3),
    ('argyoupoli','elliniko', VELOCITY*1),
    ('elliniko','argyroupoli', VELOCITY*1),
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
    ('airport','peania - kantza', VELOCITY*5)
]

G.add_weighted_edges_from(aristas)

graph = {
    'piraeus': {
        'faliro': VELOCITY*4
    },
    'faliro': {
        'piraeus': VELOCITY*3,
        'moschato': VELOCITY*3
    },
    'moschato': {
        'faliro': VELOCITY*3,
        'kallithea': VELOCITY*2
    },
    'kallithea': {
        'moschato': VELOCITY*2,
        'tavros': VELOCITY*2
    },
    'tavros': {
        'kallithea': VELOCITY*2,
        'petralona': VELOCITY*2
    },
    'petralona': {
        'tavros': VELOCITY*2,
        'thissio': VELOCITY*2
    },
    'thissio': {
        'petralona': VELOCITY*2,
        'monastiraki': VELOCITY*2
    },
    'monastiraki': {
        'thissio': VELOCITY*2,
        'omonia': VELOCITY*2,
        'kerameikos': VELOCITY*2,
        'syntagma': VELOCITY*3
    },
    'omonia': {
        'monastiraki': VELOCITY*2,
        'victoria': VELOCITY*2,
        'metaxourghio': VELOCITY*2,
        'panepistimio': VELOCITY*1
    },
    'victoria': {
        'omonia': VELOCITY*2,
        'attiki': VELOCITY*3
    },
    'attiki': {
        'victoria': VELOCITY*3,
        'aghios nikolaos': VELOCITY*2,
        'sepolia': VELOCITY*1,
        'larissa st.': VELOCITY*2
    },
    'aghios nikolaos': {
        'attiki': VELOCITY*2,
        'kato patissia': VELOCITY*2
    },
    'kato patissia': {
        'aghios nikolaos': VELOCITY*2,
        'aghios eleftherios': VELOCITY*2
    },
    'aghios eleftherios': {
        'kato patissia': VELOCITY*2,
        'ano patissia': VELOCITY*1
    },
    'ano patissia': {
        'aghios eleftherios': VELOCITY*1,
        'perissos': VELOCITY*3
    },
    'perissos': {
        'ano patissia': VELOCITY*3,
        'pefkakia': VELOCITY*1
    },
    'pefkakia': {
        'perissos': VELOCITY*1,
        'nea ionia': VELOCITY*2
    },
    'nea ionia': {
        'pefkakia': VELOCITY*2,
        'iraklio': VELOCITY*2
    },
    'iraklio': {
        'nea ionia': VELOCITY*2,
        'irini': VELOCITY*3
    },
    'irini': {
        'iraklio': VELOCITY*3,
        'neratziotissa': VELOCITY*2
    },
    'neratziotissa': {
        'irini': VELOCITY*2,
        'maroussi': VELOCITY*3
    },
    'maroussi': {
        'neratziotissa': VELOCITY*3,
        'kat': VELOCITY*2
    },
    'kat': {
        'maroussi': VELOCITY*2,
        'kifissia': VELOCITY*2
    },
    'kifissia': {
        'kat': VELOCITY*2
    },
    'anthoupoli': {
        'peristeri': VELOCITY*1
    },
    'peristeri': {
        'anthoupoli': VELOCITY*1,
        'aghios antonios': VELOCITY*1
    },
    'aghios antonios': {
        'peristeri': VELOCITY*1,
        'sepolia': VELOCITY*2
    },
    'sepolia': {
        'aghios antonios': VELOCITY*2,
        'attiki': VELOCITY*1
    },
    'larissa st.': {
        'attiki': VELOCITY*2,
        'metaxourghio': VELOCITY*1
    },
    'metaxourghio': {
        'larissa st.': VELOCITY*1,
        'omonia': VELOCITY*2
    },
    'panepistimio': {
        'omonia': VELOCITY*1,
        'syntagma': VELOCITY*2
    },
    'syntagma': {
        'panepistimio': VELOCITY*2,
        'akropoli': VELOCITY*1,
        'monastiraki': VELOCITY*3,
        'evangelismos': VELOCITY*1
    },
    'akropoli': {
        'syntagma': VELOCITY*1,
        'sygroy - fix': VELOCITY*2
    },
    'sygroy - fix': {
        'akropoli': VELOCITY*2,
        'neos kosmos': VELOCITY*1
    },
    'neos kosmos': {
        'sygroy - fix': VELOCITY*1,
        'aghios ioannis': VELOCITY*1
    },
    'aghios ioannis': {
        'neos kosmos': VELOCITY*1,
        'dafni': VELOCITY*2
    },
    'dafni': {
        'aghios ioannis': VELOCITY*2,
        'aghios dimitrios': VELOCITY*2
    },
    'aghios dimitrios': {
        'dafni': VELOCITY*2,
        'ilioupoli': VELOCITY*2
    },
    'ilioupoli': {
        'aghios dimitrios': VELOCITY*2,
        'alimos': VELOCITY*1
    },
    'alimos': {
        'ilioupoli': VELOCITY*1,
        'argyoupoli': VELOCITY*3
    },
    'argyoupoli': {
        'alimos': VELOCITY*3,
        'elliniko': VELOCITY*1
    },
    'elliniko': {
        'argyroupoli': VELOCITY*1
    },
    'egaleo': {
        'eleonas': VELOCITY*2
    },
    'eleonas': {
        'egaleo': VELOCITY*2,
        'kerameikos': VELOCITY*2
    },
    'kerameikos': {
        'eleonas': VELOCITY*2,
        'monastiraki': VELOCITY*2
    },
    'evangelismos': {
        'syntagma': VELOCITY*1,
        'megaro moussikis': VELOCITY*1
    },
    'megaro moussikis': {
        'evangelismos': VELOCITY*1,
        'ambelokipi': VELOCITY*2
    },
    'ambelokipi': {
        'megaro moussikis': VELOCITY*2,
        'panormou': VELOCITY*1
    },
    'panormou': {
        'ambelokipi': VELOCITY*1,
        'katehaki': VELOCITY*2
    },
    'katehaki': {
        'panormou': VELOCITY*2,
        'ethniki amyna': VELOCITY*2
    },
    'ethniki amyna': {
        'katehaki': VELOCITY*2,
        'holargos': VELOCITY*2
    },
    'holargos': {
        'ethniki amyna': VELOCITY*2,
        'nomismatokopio': VELOCITY*1
    },
    'nomismatokopio': {
        'holargos': VELOCITY*1,
        'aghia paraskevi': VELOCITY*2
    },
    'aghia paraskevi': {
        'nomismatokopio': VELOCITY*2,
        'halandri': VELOCITY*2
    },
    'halandri': {
        'aghia paraskevi': VELOCITY*2,
        'douk. plakentias': VELOCITY*1
    },
    'douk. plakentias': {
        'halandri': VELOCITY*1,
        'pallini': VELOCITY*6
    },
    'pallini': {
        'douk. plakentias': VELOCITY*6,
        'peania - kantza': VELOCITY*3
    },
    'peania - kantza': {
        'pallini': VELOCITY*3,
        'koropi': VELOCITY*6
    },
    'koropi': {
        'peania - kantza': VELOCITY*6,
        'airport': VELOCITY*5
    },
    'airport': {
        'peania - kantza': VELOCITY*5
    }
}


def algorithm(from_location: str, to_location: str) -> int:
    '''
    METHOD THAT IMPLEMENTS A* ALGORITHM FOR ATHENAS METRO NET
    '''

    # INITIALIZE OPEN AND CLOSED LISTS
    open_list: list = []
    closed_list: list = []
    g_value: float = 0
    h_value: float = 0
    open_list.append((0,0, from_location))
    while len(open_list) != 0:
        station = min(open_list)
        open_list.remove(station)
        closed_list.append(station)
        if station[2] == to_location:
            #* Success!!!
            print(closed_list)
            return 1

        next_stations = list(graph[station[2]])
        for new_station in next_stations:
            result = [ x for x in closed_list if x[2] == new_station]
            if result != []:
                continue
            g_value = g_value + graph[station[2]][new_station]
            h_value = data_frame[new_station][to_location]
            f_value = g_value + h_value
            if new_station in open_list:
                index: int = open_list.index(new_station)
                if g_value > open_list[index][1]:
                    continue
            open_list.append((f_value,g_value, new_station))
    return 0


def main():
    '''
    MAIN METHOD
    '''
    print(algorithm('thissio', 'evangelismos'))


if __name__ == '__main__':
    main()
