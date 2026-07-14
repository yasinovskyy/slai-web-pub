import csv


def read_csv_file(filename):
    with open(filename) as pokemon:
        return list(csv.DictReader(pokemon))


def main():
    data_from_file = read_csv_file("data/pokemon.csv")
    print(data_from_file)


if __name__ == "__main__":
    main()
