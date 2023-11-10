import concurrent.futures
from multiprocessing import cpu_count
import time

def factorize_single(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factorize_parallel(*numbers):
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        result = list(executor.map(factorize_single, numbers))

    return result

if __name__ == "__main__":
    start_time = time.time()

    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Time taken:", elapsed_time)
    print("Results:")
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
