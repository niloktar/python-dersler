import math
import random
 
# from time import perf_counter
# burayı alttaki satırla değiştirdim
 
from timeit import default_timer as perf_counter
 
def monte_carlo(start, stop, num_points, f):
    hits = 0
    upp_bound = 0
    for i in range(num_points):
        x = random.uniform(start, stop)
        y = random.uniform(0, 4) # this is cheating since I already know it's 4
        if y <= f(x):
            hits += 1
        if y > upp_bound:
            upp_bound = y
    ans = (hits / num_points) * ((stop - start) * upp_bound)
    return ans
 
def riemann(start, stop, step, f):
    return sum(f(start+step*m)*step for m in range(int((stop - start)/step)))
 
f = lambda x: math.sqrt(16 - 16*x**2)
 
start = perf_counter()
a = monte_carlo(0, 1, 10000000, f)
m_time = perf_counter() - start
start = perf_counter()
b = riemann(0, 1, 1/15000, f)
r_time = perf_counter() - start
print('Monte Carlo: %s\nTime elapsed: %s' % (a, m_time))
print('Riemann sum: %s\nTime elapsed: %s' % (b, r_time))
