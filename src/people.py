import random

PATH_TO_FIRST_NAMES = 'first-names.txt'
PATH_TO_SURNAMES = 'surnames/uk.txt'

def import_database(fn):

    with open('./name-database/' + fn, 'r') as datafile:
        try:
            names = datafile.read().splitlines()
        except IOError:
            print('File does not exist')

    return names

def random_names(n):
    first_names = import_database(PATH_TO_FIRST_NAMES)
    surnames = import_database(PATH_TO_SURNAMES)

    names = []

    for name in range(0, n):
        names.append((random.choice(surnames), random.choice(first_names)))

    return names

if __name__ == "__main__":
    print(random_names(30))