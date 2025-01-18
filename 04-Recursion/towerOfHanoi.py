from typing import List

def solve_toi(disks: List[int], 
                   from_pole: str = "Pole A", 
                   to_pole: str = "Pole C", 
                   intermediary_pole: str = "Pole B"
                   ) -> None: 
    """Recursively solve Tower of Hanoi problem."""
    
    if len(disks) == 1: 
        print(f"Move disk {disks[0]} from {from_pole} to {to_pole}")
        return
    
    # move 1 to n-1 disks 
    solve_toi(disks[:-1], from_pole, intermediary_pole, to_pole)
    
    # move nth disk (biggest disk at hand) to its correct pole.
    solve_toi(disks[-1:], from_pole, to_pole, intermediary_pole)
    
    # move 1 to n-1 disks
    solve_toi(disks[:-1], intermediary_pole, to_pole, from_pole)
    

if __name__ == "__main__": 
    
    for i in range(1,5): 
        print(f"Solving Tower of Hanoi Problem for {i} disks:")
        disks = list(range(1,i+1))
        solve_toi(disks)
        print()