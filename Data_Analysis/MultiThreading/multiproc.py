import multiprocessing
import threading
import time
def square():
    for i in range(4):
        time.sleep(2)
        print(i*i)

def cube():
    for i in range(5):
        time.sleep(1.5)
        print(i*i*i)

if __name__ == "__main__":  
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    start = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(end-start)