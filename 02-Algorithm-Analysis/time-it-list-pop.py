from timeit import Timer

NUMBER_OF_REPETITION = 1_000

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
print(f"{'n':12s}{'pop(0)':>15s}{'pop()':>15s}")

for i in range(1_000_000, 10_000_001, 1_000_000):
    
    x = [1] * i
    pop_zero_time = pop_zero.timeit(number=NUMBER_OF_REPETITION)
    
    x = [1] * i
    pop_end_time = pop_end.timeit(number=NUMBER_OF_REPETITION)
    print(f"{i:<12,d}{pop_zero_time:>15.5f}{pop_end_time:>15.5f}")


output = """
n                    pop(0)          pop()
1,000,000           1.40267        0.00003
2,000,000           1.83876        0.00003
3,000,000           2.47382        0.00003
4,000,000           3.29768        0.00003
5,000,000           3.67210        0.00002
6,000,000           4.31244        0.00002
7,000,000           5.01690        0.00002
8,000,000           5.73844        0.00002
9,000,000           6.48995        0.00002
10,000,000          7.14650        0.00002
"""