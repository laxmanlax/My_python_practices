import multiprocessing

def calc_square(number, result, v):
    v.value=5.67
    for idx, n in enumerate(number):
        result[idx] = n*n 

def main():
    number = [1,2,3,4,5]
    result = multiprocessing.Array('i',5)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(number, result, v))

    p.start()
    p.join()

    print result[:], v.value


if __name__=="__main__":
    main()

