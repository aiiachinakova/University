import multiprocessing
import time
import random

num = 50

def pi_сalculate(x):
    circle_size = 0
    for i in range(100000):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            point_amount += 1
    return point_amount

def test_all(pool):
    l = pool.map(pi_сalculate, [0]*num)
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(4*sum(test_all(pool))/100000/num)
    print("Time spent:", time.time() - t0)
