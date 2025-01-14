from timeit import Timer
import random

NUMBER_OF_REPETITIONS = 1000


print(f"{"Size":>12s}\t{"Get Time":12s}\t{"Set Time":12s}")


for i in range(1_000_000, 10_000_001, 1_000_000):
    
    t1 = Timer(f"x.get(random.randrange({i}))", 
           "from __main__ import random, x")
    t2 = Timer(f"x[random.randrange({i})]={i}", 
            "from __main__ import random, x")
    x = {j: j for j in range(i)}
    time_taken_get = t1.timeit(number=NUMBER_OF_REPETITIONS)
    time_taken_set = t2.timeit(number=NUMBER_OF_REPETITIONS)
    
    print(f"{i:12,d}\t{time_taken_get:2.10f}\t{time_taken_set:2.10f}")

Output = """
        Size    Get Time        Set Time    
   1,000,000    0.0012752900    0.0011236000
   2,000,000    0.0013884020    0.0012241650
   3,000,000    0.0014363080    0.0013322950
   4,000,000    0.0015045370    0.0013052000
   5,000,000    0.0011304710    0.0010539140
   6,000,000    0.0011438570    0.0010380810
   7,000,000    0.0011272220    0.0010317870
   8,000,000    0.0011185330    0.0010367560
   9,000,000    0.0011972620    0.0011094130
  10,000,000    0.0011884320    0.0011088610
"""