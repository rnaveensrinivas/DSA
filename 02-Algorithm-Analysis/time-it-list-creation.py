from timeit import Timer

SIZE_OF_LIST = 1_000_000_000
NUMBER_OF_REPETITION = 10000

def test1(size: int=SIZE_OF_LIST):
    """Creating a list using for loop and concatenation operator."""
    l = []
    for i in range(1000):
        l = l + [i]


def test2(size: int=SIZE_OF_LIST):
    """Creating a list using for loop and append method."""
    l = []
    for i in range(1000):
        l.append(i)


def test3(size: int=SIZE_OF_LIST):
    """Creating a list using list comprehension."""
    l = [i for i in range(1000)]


def test4(size: int=SIZE_OF_LIST):
    """Creating a list using range function."""
    l = list(range(1000))
    
    
def test5(size: int=SIZE_OF_LIST):
    """Creating a list using repitition operator."""
    l = [0] * size
    

def empty_function(): 
    pass


t0 = Timer("empty_function()", "from __main__ import empty_function")
overhead_time = t0.timeit(number=NUMBER_OF_REPETITION)
# print(f"Overhead time for a function call is {(overhead_time):2.20f} \
# milliseconds\n")

print(f"Time taken to create list {SIZE_OF_LIST:,} in size, \
{NUMBER_OF_REPETITION:,} times using")

t1 = Timer("test1()", "from __main__ import test1")
print(f"- concatenation is\t\
{(t1.timeit(number=NUMBER_OF_REPETITION)-overhead_time):2.20f} \
milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print(f"- appending is\t\t\
{(t2.timeit(number=NUMBER_OF_REPETITION)-overhead_time):2.20f} \
milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print(f"- comprehension is\t\
{(t3.timeit(number=NUMBER_OF_REPETITION)-overhead_time):2.20f} \
milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print(f"- range is\t\t\
{(t4.timeit(number=NUMBER_OF_REPETITION)-overhead_time):2.20f} \
milliseconds")

t5 = Timer("test5()", "from __main__ import test5")
print(f"- repititon is\t\t\
{(t4.timeit(number=NUMBER_OF_REPETITION)-overhead_time):2.20f} \
milliseconds")

Output = """
Time taken to create list 1,000,000,000 in size, 10,000 times using
- concatenation is      13.84000286599984974600 milliseconds
- appending is          0.20838639000066905282 milliseconds
- comprehension is      0.15916914599984011147 milliseconds
- range is              0.09835640900018916000 milliseconds
- repititon is          0.09896656700038874988 milliseconds
"""

