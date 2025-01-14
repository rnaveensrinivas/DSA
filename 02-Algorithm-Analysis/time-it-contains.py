import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")

for i in range(100_000, 1_000_001, 100_000):

    t = timeit.Timer(f"random.randrange({i}) in x",
                     "from __main__ import random, x")

    x = list(range(i))
    list_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)

    print(f"{i:<10,}{list_time:>10.3f}{dict_time:>10.3f}")
    
Output = """
n               list      dict
100,000        0.510     0.001
200,000        1.015     0.001
300,000        1.550     0.001
400,000        2.064     0.001
500,000        2.301     0.001
600,000        1.956     0.001
700,000        2.445     0.001
800,000        2.647     0.001
900,000        3.032     0.001
1,000,000      3.230     0.001
"""