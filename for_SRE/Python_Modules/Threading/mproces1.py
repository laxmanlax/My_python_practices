import time
import multiprocessing


def calc_square(numbers):
    print "Result Square......"

    for n in numbers:
        time.sleep(0.3)
        print "Square :", n*n


def calc_cube(numbers):
    print "Result Cube....."

    for n in numbers:
        time.sleep(0.3)
        print "Cube :", n*n*n


#calc_square(arr)
#calc_cube(arr)

def main():
    arr = [2, 3, 4, 5, 6, 7, 8, 9]
    t = time.time()

    t1 = multiprocessing.Process(target=calc_square, args=(arr,))
    t2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print "Time :", time.time()-t


if __name__ == "__main__":
    main()
