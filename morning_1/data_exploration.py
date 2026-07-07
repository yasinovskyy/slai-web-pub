import csv


def read_data_file(filename):
    with open(filename) as pokemon:
        pokemon.readline()
        data = []
        for line in pokemon.readlines():
            data.append(line.strip().split(","))
        return data


def read_csv_file(filename):
    with open(filename) as pokemon:
        return [eye for eye in csv.DictReader(pokemon)]


def main():
    data_from_file = read_csv_file("pokemon.csv")
    print(data_from_file)


if __name__ == "__main__":
    main()
