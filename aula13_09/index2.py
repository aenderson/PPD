from datetime import datetime
import concurrent.futures
from functools import reduce

def contagem(n):
    c = 0
    for i in range(n):
        c += 1
    return c

def reducer(c1,c2):
    reduced = c1 + c2
    return reduced

if __name__ == '__main__':
    start = datetime.now()
    print(start)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        mapped = executor.map(contagem, [500000, 500000])
        result = reduce(reducer, mapped)

    print(f'Result: {result}.\nTempo: {datetime.now() - start}')