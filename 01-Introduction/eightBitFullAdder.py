from fullAdder import FullAdder
from typing import List
import re

class EightBitFullAdder: 
    """
    A class representing an 8-bit full adder, which performs binary addition of two 8-bit numbers.
    
    Attributes:
        label (str): The label for the 8-bit full adder.
        full_adders (List[FullAdder]): A list of FullAdder objects representing each bit of the addition.
    
    Methods:
        perform_logic(): Computes the sum of the two 8-bit binary inputs and returns the result as a string.
    """
    def __init__(self, 
                 label: str,
                 binary_input_a: str, 
                 binary_input_b: str) -> None: 
        """Initializes an EightBitFullAdder instance with two 8-bit binary inputs.
        
        Args:
            label (str): The label for the 8-bit full adder.
            binary_input_a (str): The first 8-bit binary input as a string.
            binary_input_b (str): The second 8-bit binary input as a string.
        
        Raises:
            AssertionError: If either of the binary inputs is not 8 bits long.
            AssertionError: If either of the binary inputs is not binary.
        """
        self.label = label
        self.full_adders: List[FullAdder] = []
        
        assert len(binary_input_a) == 8, "Input a is not of length 8!"
        assert len(binary_input_b) == 8, "INput b is not of length 8!"
        assert re.match(r'^[01]{8}$', binary_input_a), "Input a not in binary!"
        assert re.match(r'^[01]{8}$', binary_input_b), "Input b not in binary!"
        
        prev_carry = 0
        for i, (a, b) in enumerate(zip(binary_input_a[::-1], binary_input_b[::-1])): 
            fa = FullAdder(f"FA {i}", int(a), int(b), prev_carry)
            prev_carry = fa
            self.full_adders.append(fa)
            
            
    def perform_logic(self) -> str: 
        """Computes the sum and final carry of the 8-bit full adder.

        Returns:
            str: A string representation of the result, including the sum and the final carry.
        """
        result = []
        for fa in self.full_adders: 
            c,s = fa.perform_logic()
            result.append(str(s))
        
        result.extend(["|", str(c)])
        return "".join(result[::-1])
    
    
# Test Case 1: Add two binary numbers "00000001" and "00000001"
assert EightBitFullAdder("8 efa", "00000001", "00000001").perform_logic() == "0|00000010", "Test Case 1 Failed"

# Test Case 2: Add two binary numbers "11111111" and "00000001"
assert EightBitFullAdder("8 efa", "11111111", "00000001").perform_logic() == "1|00000000", "Test Case 2 Failed"

# Test Case 3: Add two binary numbers "11110000" and "00001111"
assert EightBitFullAdder("8 efa", "11110000", "00001111").perform_logic() == "0|11111111", "Test Case 3 Failed"

# Test Case 4: Add two binary numbers "01010101" and "10101010"
assert EightBitFullAdder("8 efa", "01010101", "10101010").perform_logic() == "0|11111111", "Test Case 4 Failed"

# Test Case 5: Add two binary numbers "00000000" and "00000000"
assert EightBitFullAdder("8 efa", "00000000", "00000000").perform_logic() == "0|00000000", "Test Case 5 Failed"

# Test Case 6: Add two binary numbers "11111111" and "11111111"
assert EightBitFullAdder("8 efa", "11111111", "11111111").perform_logic() == "1|11111110", "Test Case 6 Failed"

# Test Case 7: Add two binary numbers "01010101" and "01010101"
assert EightBitFullAdder("8 efa", "01010101", "01010101").perform_logic() == "0|10101010", "Test Case 7 Failed"