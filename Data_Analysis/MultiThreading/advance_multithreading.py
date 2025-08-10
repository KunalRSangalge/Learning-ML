from concurrent.futures import ThreadPoolExecutor
import time
def show(a):
    time.sleep(1)
    return a

numbers = [1,2,3,4,5,6,7,9,10]
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(show,numbers)

start = time.time()
for i in results:
    print(i)
end = time.time()
print(end-start)