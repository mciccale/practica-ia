'''
HANDMADE MODULE for A* Project, using haversine module
'''

import haversine as hs

data = {
    'piraeus': (37.948060, 23.643610),
    'faliro': (37.945000, 23.66528),
    'moschato': (37.955280, 23.680560),
    'kallithea': (37.96056, 23.69722),
    'tavros': (37.96250, 23.70333),
    'petralona': (37.96861, 23.70917),
    'thissio': (37.97721, 23.71954),
    'monastiraki': (37.972281, 23.721902),
    'omonia': (37.983787, 23.723607),
    'victoria': (37.993056, 23.730556),
    'attiki': (37.993096, 23.753713),
    'aghios nikolaos': (38.006900, 23.727700),
    'kato patissia': (38.011944, 23.728611),
    'aghios eleftherios': (38.019722, 23.731667),
    'ano patissia': (38.020949, 23.734997),
    'perissos': (38.032778, 23.744722),
    'pefkakia': (38.036944, 23.750000),
    'nea ionia': (38.041528, 23.75500),
    'iraklio': (38.046300, 23.766200),
    'irini': (38.043200, 23.783400),
    'neratziotissa': (38.040333, 23.788996),
    'maroussi': (38.056200, 23.805000),
    'kat': (38.064800, 23.809500),
    'kifissia': (38.073700, 23.808300),
    'anthoupoli': (38.016944, 23.691667),
    'peristeri': (38.012981, 23.695731),
    'aghios antonios': (38.006111, 23.699722),
    'sepolia': (38.002786, 23.713583),
    'larissa st.': (37.992289, 23.720556),
    'metaxourghio': (37.9858, 23.721),
    'panepistimio': (37.980278, 23.733056),
    'syntagma': (37.97499, 23.73556),
    'akropoli': (37.96875, 23.729583),
    'sygroy - fix': (37.964605, 23.726800),
    'neos kosmos': (37.95778, 23.72861),
    'aghios ioannis': (37.9565, 23.7342),
    'dafni': (37.949236, 23.737222),
    'aghios dimitrios': (37.940278, 23.740694),
    'ilioupoli': (37.929583, 23.744514),
    'alimos': (37.918056, 23.744514),
    'argyroupoli': (37.903056, 23.745903),
    'elliniko': (37.892569, 23.747153),
    'egaleo': (37.991300, 23.677200),
    'eleonas': (37.987800, 23.692500),
    'kerameikos': (37.978600, 23.711500),
    'evangelismos': (37.976388, 23.746944),
    'megaro moussikis': (37.978610, 23.752500),
    'ambelokipi': (37.987220, 23.757500),
    'panormou': (37.993100, 23.763700),
    'katehaki': (37.995400, 23.772700),
    'ethniki amyna': (38.000000, 23.785555),
    'holargos': (38.001666, 23.812222),
    'nomismatokopio': (38.009170, 23.805830),
    'aghia paraskevi': (38.017222, 23.812500),
    'halandri': (38.021670, 23.820830),
    'douk. plakentias': (38.023361, 23.833055),
    'pallini': (38.005280, 23.869720),
    'peania - kantza': (37.984170, 23.870000),
    'koropi': (37.912780, 23.895830),
    'airport': (37.936900, 23.944800)
}

data_frame = {}

def get_data() -> dict:
    '''
    Function that calculates distance between the coordinates
    of the stations collected in the data TAD
    '''
    for i in range(0, len(data)):
        coordinates_from = list(data.values())[i]
        from_station = list(data.keys())[i]
        data_frame[from_station] = {}
        for j in range(0, len(data)):
            to_station = list(data.keys())[j]
            coordinates_to = list(data.values())[j]
            data_frame[from_station][to_station] = hs.haversine(coordinates_from, coordinates_to)


    return data_frame
