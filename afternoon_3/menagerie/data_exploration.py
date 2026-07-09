import csv


def read_csv_file(filename):
    with open(filename) as pokemon_file:
        return [pokemon for pokemon in csv.DictReader(pokemon_file)]


def main():
    data_from_file = read_csv_file("data/menagerie.csv")
    print(data_from_file)


if __name__ == "__main__":
    main()
