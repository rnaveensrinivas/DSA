from LogicGate import AndGate, XorGate, BinaryGate
from typing import Tuple

class HalfAdder(BinaryGate): 
    """A class representing a half adder circuit, which performs binary addition of two bits.
    Inherits from the BinaryGate class."""
    
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        """Initializes a HalfAdder instance with two input bits.

        Args:
            label (str): The label for the half adder gate.
            input_a (int, optional): The first input bit. Defaults to None.
            input_b (int, optional): The second input bit. Defaults to None.
        """ 
        super().__init__(label, input_a, input_b)
        self.carry = AndGate("Carry", input_a, input_b)
        self.sum = XorGate("Sum", input_a, input_b)
        
    def perform_gate_logic(self) -> Tuple[int, int]:
        """Computes the carry and sum of the half adder.

        Returns:
            tuple: A tuple containing the carry and sum of the two input bits.
        """
        
        carry = self.carry.perform_gate_logic()
        sum = self.sum.perform_gate_logic()
        
        return (carry, sum)
    
ha = HalfAdder("half adder", 0, 1)
print(ha.perform_gate_logic())