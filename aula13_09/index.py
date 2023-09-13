from datetime import datetime

def contagem(n):
    c = 0
    for i in range(n):
        c += 1
    return c

if __name__ == '__main__':
    start = datetime.now()
    print(start)

    result = contagem(1000000000)

    print(f'Result: {result}.\nTempo: {datetime.now() - start}')