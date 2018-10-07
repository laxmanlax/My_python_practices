import multiprocessing


def calc_square(number, q):
    for n in number:
        q.put(n*n)

        
def main():
    number = [1, 2, 3, 4, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(number, q))

    p.start()
    p.join()

    while not q.empty():
        print q.get()

if __name__ == "__main__":
    main()
