from fibonacci import fibonacci_iterative, fibonacci_recursive
from timeit import Timer

NUMBER_OF_REPETITIONS=1000
NTH_TERM = 30

print(f"{"Size":>12s}\t{"Recursive":12s}\t{"Iterative":12s}")
for i in range(NTH_TERM):
    
    t_iter = Timer(f"fibonacci_iterative({i})", 
                   "from __main__ import fibonacci_iterative") 

    t_rec = Timer(f"fibonacci_recursive({i})", 
                  "from __main__ import fibonacci_recursive")

    time_taken_iter = t_iter.timeit(number=NUMBER_OF_REPETITIONS)
    time_taken_rec = t_rec.timeit(number=NUMBER_OF_REPETITIONS)
    
    print(f"{i:12,d}\t{time_taken_rec:2.10f}\t{time_taken_iter:2.10f}")

Output = """
        Size	Recursive   	Iterative   
           0	0.0000521460	0.0000553730
           1	0.0000626770	0.0000638490
           2	0.0002071950	0.0002553950
           3	0.0004010170	0.0002783980
           4	0.0006889420	0.0002918730
           5	0.0012208410	0.0003152660
           6	0.0020607050	0.0003413850
           7	0.0033763130	0.0003739250
           8	0.0055545750	0.0003986620
           9	0.0090261150	0.0004300700
          10	0.0146955250	0.0004657470
          11	0.0237699710	0.0004825080
          12	0.0384926680	0.0005054200
          13	0.0623129520	0.0005320400
          14	0.1007444950	0.0006070700
          15	0.1634654260	0.0006259450
          16	0.2660672770	0.0006835220
          17	0.4289291530	0.0007181260
          18	0.6974603920	0.0007670670
          19	1.1228811510	0.0007995380
          20	1.8206848050	0.0008585170
          21	2.9562673120	0.0008975500
          22	3.5857607400	0.0009246310
          23	4.6840430530	0.0005867620
          24	7.6172315020	0.0006275680
          25	12.3843130360	0.0006370160
          26	19.8606259690	0.0006604090
          27	32.0737360000	0.0006760900
          28	52.0913598940	0.0006912880
          29	84.3680724300	0.0007229680
          30	139.0588914740	0.0007488080

Notice the pattern in Recursive column. 
Time taken for a row is roughly the sum of previous two rows. 
"""