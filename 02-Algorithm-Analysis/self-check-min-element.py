_ = """
Self Check: 

Write two Python functions to find the minimum number in a list. The first 
function should compare each number to every other number on the list O(n^2). 
The second function should be linear O(n).
"""
import random
import time

random.seed(3)
cases = {
    0: ["Best","first"],
    1: ["Average", "any"],
    2: ["Worst", "last"],
}

def big_O_of_n_squared_solution(size: int = 1_000_000, case: int = 1) -> None: 
    
    print("O(n^2) Solution: {0} Case - min at {1} index".format(*cases[case]))
    random_list = [random.random() for _ in range(size)]
    
    match case: 
        case 0: random_list[0] = 0
        case 2: random_list[-1] = 0

    starting_time = time.perf_counter()
    for number1 in random_list: 
        for number2 in random_list: 
            if number1 > number2: 
                break
        else:
            print(f"The smallest number in random_list is {number1:2.20f}")
            break
    ending_time = time.perf_counter()
    print(f"Time taken: {(ending_time - starting_time):2.20f}")


def big_O_of_n_solution(size: int = 1_000_000, case: int = 1) -> None: 
    
    print("O(n) Solution: {0} Case - min at {1} index".format(*cases[case]))
    random_list = [random.random() for _ in range(size)]
    
    match case: 
        case 0: random_list[0] = 0
        case 2: random_list[-1] = 0

    starting_time = time.perf_counter()
    min_number = random_list[0]

    for number in random_list: 
        min_number = min(min_number, number)

    print(f"The smallest number in random_list is {min_number:2.20f}")
    ending_time = time.perf_counter()
    print(f"Time taken: {(ending_time - starting_time):2.20f}")
    
    
def simulate(size_of_list: int = 1_000_000, case: int = 1) -> None: 
    big_O_of_n_squared_solution(size=size_of_list, case=case)
    big_O_of_n_solution(size=size_of_list, case=case)
    print()
    

if __name__ == "__main__": 
    simulate(size_of_list=10_000_000, case=0)
    simulate(size_of_list=10_000_000, case=1)
    simulate(size_of_list=10_000_000, case=2)

    
_ = """
Ouptut: 
O(n^2) Solution: Best Case - min at first index
The smallest number in random_list is 0.00000000000000000000
Time taken: 0.34228944778442382812
O(n) Solution: Best Case - min at first index
The smallest number in random_list is 0.00000000000000000000
Time taken: 2.03503322601318359375

O(n^2) Solution: Average Case - min at any index
The smallest number in random_list is 0.00000000432950852947
Time taken: 0.83890390396118164062
O(n) Solution: Average Case - min at any index
The smallest number in random_list is 0.00000004312133738971
Time taken: 1.93779945373535156250

O(n^2) Solution: Worst Case - min at last index
The smallest number in random_list is 0.00000000000000000000
Time taken: 2.33105778694152832031
O(n) Solution: Worst Case - min at last index
The smallest number in random_list is 0.00000000000000000000
Time taken: 1.20272159576416015625
"""