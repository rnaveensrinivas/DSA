from LogicGate import XorGate, AndGate, OrGate
from typing import Tuple

class FullAdder(): 
    def __init__(self, 
                 label: str, 
                 input_a: int = None, 
                 input_b: int = None,
                 carry_in: int = None) -> None:
        
        self.label = label
        self.XORGate1 = XorGate("XOR 1", input_a, input_b)
        
        if isinstance(carry_in, FullAdder): 
            carry_in = carry_in.perform_logic()[0]
            
        self.sum = XorGate("XOR 2", self.XORGate1, carry_in)
        self.ANDGate1 = AndGate("AND 1", self.XORGate1, carry_in)
        self.ANDGate2 = AndGate("AND 2", input_a, input_b)
        self.carry = OrGate("OR 1", self.ANDGate1, self.ANDGate2)
        
    def get_label(self) -> str: 
        return self.label
    
    def perform_logic(self) -> Tuple[int, int]:
        """Compute the result."""
        return (self.carry.perform_gate_logic(), self.sum.perform_gate_logic())
    
if __name__ == "__main__": 
    print("A\tB\tC_in\tCarry\tSum")
    print("-"*38)
    for i in [0, 1]: 
        for j in [0, 1]: 
            for k in [0, 1]: 
                c, s = FullAdder("full adder", i, j, k).perform_logic()
                print(f"{i}\t{j}\t{k}\t{c}\t{s}")