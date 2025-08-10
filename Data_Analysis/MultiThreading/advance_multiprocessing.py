from concurrent.futures import ProcessPoolExecutor
import time 
def square(a):
    time.sleep(2)
    return a * a
def main():
    numbers = [1, 2, 33, 23, 35, 3, 34, 32, 3]

    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

        for i in results:
            print(i)
    end = time.time()
    print("Elapsed:", end - start)

if __name__ == "__main__":
    main()
