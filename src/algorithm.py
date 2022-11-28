from get_data import get_data

data_frame: dict = get_data()

# Velocidad media de los trenes de Atenas expresada en Kilómetros / Minutos

# Como los datos nos dicen el tiempo entre estaciones en minutos, calculamos
# una distancia aproximada usando la velocidad media
VELOCITY = 1.3333

graph = {
    'piraeus': {
        'faliro': VELOCITY*4,
        'dimotiko theatro': VELOCITY*2,
        'maniatika': VELOCITY*1
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
        'nea inonia': VELOCITY*2,
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
        'perosteri': VELOCITY*1
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
    'dimotiko theatro': {
        'piraeus': VELOCITY*2
    },
    'maniatika': {
        'piraeus': VELOCITY*1,
        'nikea': VELOCITY*2
    },
    'nikea': {
        'maniatika': VELOCITY*2,
        'korydallos': VELOCITY*2
    },
    'korydallos': {
        'nikea': VELOCITY*2,
        'aghia varvara': VELOCITY*2
    },
    'aghia varvara': {
        'korydalos': VELOCITY*2,
        'aghis marina': VELOCITY*2
    },
    'aghia marina': {
        'aghia varvara': VELOCITY*2,
        'egaleo': VELOCITY*2
    },
    'egaleo': {
        'aghia marina': VELOCITY*2,
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
        'amberlokipi': VELOCITY*2
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
    open_list: list = []
    closed_list: list = []
    g_value: float = 0
    h_value: float = 0
    open_list.append((0, from_location))
    while len(open_list) != 0:
        station = min(open_list)
        open_list.remove(station)
        closed_list.append(station)
        if station[1] == to_location:
            #* Success!!!
            return 1

        next_stations = list(graph[station[1]])
        for new_station in next_stations:
            if new_station in closed_list:
                continue
            g_value = g_value + graph[station[1]][new_station]
            h_value = data_frame[new_station][to_location]
            f_value = g_value + h_value
            #if new_station in open_list:
            #    index: int = open_list.index(new_station)
            #    if g > open_list[index][]m

    return 0


def main():
    '''
    MAIN METHOD
    '''
    print(algorithm('piraeus', 'irini'))


if __name__ == '__main__':
    main()
