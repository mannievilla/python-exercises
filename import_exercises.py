def calculate_tip(bill, tip_perc):
    '''
    This function takes in total bill and tip percentage
    Then it returns what the actual tip should be
    '''
    return bill * tip_perc


def get_letter_grade():
    grade = int(input('Your grade: '))
    letter = ['A', 'B', 'C', 'D', 'F']
    while True:
    # for letter in ['A', 'B', 'C', 'D', 'F']:
        if grade in range(88, 101):
            print(f'{grade} is an {letter[0]}')
            break
        elif grade in range(80, 88):
            print(f'Your grade {grade} is a {letter[1]}')
            break
        elif grade in range(67, 80):
            print(f'{grade} is a {letter[2]}')
            break
        elif grade in range(60, 66):
            print(f'{grade} is a {letter[3]}')
            break
        else:
            print(f'{grade} is a {letter[4]}')
            break


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)