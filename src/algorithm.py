from get_data import get_data

data_frame: dict = get_data()

def algorithm(from_location: str, to_location: str) -> int:
    h: int = data_frame[from_location][to_location]
    return h


def main():
    print(algorithm('piraeus', 'irini'))


if __name__ == '__main__':
    main()
