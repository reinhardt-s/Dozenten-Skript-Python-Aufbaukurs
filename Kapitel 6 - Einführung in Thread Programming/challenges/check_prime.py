# Erstelle ein Programm das die Zahlen in numbers_to_check auf Primzahlen prüft.
# Nutze hierzu multiprocessing.

numbers_to_check = [125446513, 1562256737, 325447061, 46848278561624631, 325444949,
                    125447503, 747285, 545446283, 125446513]

import multiprocessing


def check_if_prime(number):
    print(f'Checking if {number} is a prime number')
    for pos, i in enumerate(range(2, number)):
        if number % i == 0:
            print(f'{number} is not a prime number')
            return False
    print(f'{number} is a prime number')
    return True


if __name__ == '__main__':
    processes = []
    for number in numbers_to_check:
        p = multiprocessing.Process(target=check_if_prime, args=(number,))
        processes.append(p)
        p.start()

    print('Finished')
