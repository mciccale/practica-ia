from get_data import get_data

data_frame: dict = get_data()

velocity = 1.3333

graph = {
    #* INICIO DE LA LÍNEA 1
    'piraeus': {
        'faliro': velocity*4
    },
    'faliro': {
        'piraeus': velocity*3,
        'moschato': velocity*3
    },
    'moschato': {
        'faliro': velocity*3,
        'kallithea': velocity*2
    },
    'kallithea': {
        'moschato': velocity*2,
        'tavros': velocity*2
    },
    'tavros': {
        'kallithea': velocity*2,
        'petralona': velocity*2
    },
    'petralona': {
        'tavros': velocity*2,
        'thissio': velocity*2
    },
    'thissio': {
        'petralona': velocity*2,
        'monastiraki': velocity*2
    },
    'monastiraki': {
        'thissio': velocity*2,
        'omonia': velocity*2
    },
    'omonia': {
        'monastiraki': velocity*2,
        'victoria': velocity*2
    },
    'victoria': {
        'omonia': velocity*2,
        'attiki': velocity*3
    },
    'attiki': {
        'victoria': velocity*3,
        'aghios nikolaos': velocity*2
    },
    'aghios nikolaos': {
        'attiki': velocity*2,
        'kato patissia': velocity*2
    },
    'kato patissia': {
        'aghios nikolaos': velocity*2,
        'aghios eleftherios': velocity*2
    },
    'aghios eleftherios': {
        'kato patissia': velocity*2,
        'ano patissia': velocity*1
    },
    'ano patissia': {
        'aghios eleftherios': velocity*1,
        'perissos': velocity*3
    },
    'perissos': {
        'ano patissia': velocity*3,
        'pefkakia': velocity*1
    },
    'pefkakia': {
        'perissos': velocity*1,
        'nea ionia': velocity*2
    },
    'nea ionia': {
        'pefkakia': velocity*2,
        'iraklio': velocity*2
    },
    'iraklio': {
        'nea inonia': velocity*2,
        'irini': velocity*3
    },
    'irini': {
        'iraklio': velocity*3,
        'neratziotissa': velocity*2
    },
    'neratziotissa': {
        'irini': velocity*2,
        'maroussi': velocity*3
    },
    'maroussi': {
        'neratziotissa': velocity*3,
        'kat': velocity*2
    },
    'kat': {
        'maroussi': velocity*2,
        'kifissia': velocity*2
    },
    'kifissia': {
        'kat': velocity*2
    }
    #! INICIO DE LA LÍNEA 2
}

def algorithm(from_location: str, to_location: str) -> int:
    open_list: list = []
    closed_list: list = []
    g: int = 0
    h: int = 0
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
            g = g + graph[station[1]][new_station[1]]
            h = data_frame[new_station[1]][to_location]
            f = g + h
            #if new_station in open_list:
            #    index: int = open_list.index(new_station)
            #    if g > open_list[index][]
        pass

    return None


def main():
    print(algorithm('piraeus', 'irini'))


if __name__ == '__main__':
    main()
