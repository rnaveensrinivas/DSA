class LogicGate:
    """A base class representing a logic gate.
    
    Attributes:
        label (str): The label for the logic gate.
    
    Methods:
        get_label(): Returns the label of the logic gate.
        get_output(): Computes and returns the output of the logic gate by 
                      calling the perform_gate_logic method.
    """
    def __init__(self, label: str) -> None:
        """Initializes a LogicGate instance with a given label.
        
        Args:
            label (str): The label for the logic gate.
        """
        self.label = label
    
    def get_label(self):
        """Returns the label of the logic gate."""
        return self.label
    
    def get_output(self): 
        """
        Computes and returns the output of the logic gate.
        The output is determined by the perform_gate_logic method, 
        which should be implemented by subclasses.
        
        Returns:
            Any: The computed output of the logic gate.
        """
        return self.perform_gate_logic()

     
class BinaryGate(LogicGate):
    """
    A class representing a binary logic gate that operates on two inputs.
    Inherits from the LogicGate class.

    Attributes:
        label (str): The label for the logic gate.
        pin_a (int, None, or Connector): The first input to the gate, which can 
                                          be an integer or a connector. Defaults to None.
        pin_b (int, None, or Connector): The second input to the gate, which can 
                                          be an integer or a connector. Defaults to None.

    Methods:
        get_pin_a(): Returns the value of pin A. If pin A is not set, prompts the 
                     user for input. If pin A is a connector, retrieves the output 
                     from the connected gate.
        get_pin_b(): Returns the value of pin B. If pin B is not set, prompts the 
                     user for input. If pin B is a connector, retrieves the output 
                     from the connected gate.
        set_next_pin(source_gate): Connects the output of another gate to the first 
                                    available pin (A or B). Raises an error if both 
                                    pins are already occupied.
    """
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        """
        Initializes a BinaryGate instance with a given label and optional inputs.
        
        Args:
            label (str): The label for the logic gate.
            input_a (int or None, optional): The first input to the gate. Defaults to None.
            input_b (int or None, optional): The second input to the gate. Defaults to None.
        """
        LogicGate.__init__(self, label)
        self.pin_a = input_a
        self.pin_b = input_b
    
    def get_pin_a(self):
        """
        Returns the value of pin A. If pin A is not set, prompts the user for input.
        If pin A is a connector, retrieves the output from the connected gate.
        
        Returns:
            int: The value of pin A.
        """
        if self.pin_a is None: 
            return int(input(f"Enter pin A input for gate {self.get_label()}: "))
        elif isinstance(self.pin_a, int): 
            return self.pin_a
        elif isinstance(self.pin_a, LogicGate): 
            return self.pin_a.get_output()
        else:  # is a connector
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        """
        Returns the value of pin B. If pin B is not set, prompts the user for input.
        If pin B is a connector, retrieves the output from the connected gate.
        
        Returns:
            int: The value of pin B.
        """
        if self.pin_b is None: 
            return int(input(f"Enter pin B input for gate {self.get_label()}: "))
        elif isinstance(self.pin_b, int): 
            return self.pin_b
        elif isinstance(self.pin_b, LogicGate): 
            return self.pin_b.get_output()
        else:  # is a connector
            return self.pin_b.get_from().get_output()
    
    def set_next_pin(self, source_gate):
        """
        Connects the output of another gate to the first available pin (A or B).
        
        Args:
            source_gate: The gate whose output will be connected to the current gate's pin.
        
        Raises:
            RuntimeError: If both pins (A and B) are already occupied.
        """
        if self.pin_a is None: 
            self.pin_a = source_gate
        elif self.pin_b is None: 
            self.pin_b = source_gate
        else: 
            raise RuntimeError("Error: No Empty Pins!")

        
class UnaryGate(LogicGate):
    """
    A class representing a unary logic gate that operates on a single input.
    Inherits from the LogicGate class.

    Attributes:
        label (str): The label for the logic gate.
        pin (int, None, or Connector): The input to the gate, which can be an 
                                        integer or a connector. Defaults to None.

    Methods:
        get_pin(): Returns the value of the pin. If the pin is not set, prompts 
                   the user for input. If the pin is a connector, retrieves the 
                   output from the connected gate.
        set_next_pin(source): Connects the output of another gate to the pin. 
                               Raises an error if the pin is already occupied.
    """
    
    def __init__(self, label: str, input_: int = None) -> None:
        """Initializes a UnaryGate instance with a given label and optional input.
        
        Args:
            label (str): The label for the logic gate.
            input_ (int or None, optional): The input to the gate. Defaults to None.
        """
        LogicGate.__init__(self, label)
        self.pin = input_

    def get_pin(self):
        """
        Returns the value of the pin. If the pin is not set, prompts the user for input.
        If the pin is a connector, retrieves the output from the connected gate.
        
        Returns:
            int: The value of the pin.
        """
        if self.pin is None:
            return int(input(f"Enter pin input for gate {self.get_label()}: "))
        elif isinstance(self.pin, int): 
            return self.pin
        elif isinstance(self.pin, LogicGate): 
            return self.pin.get_output()
        else:  # is a connector
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        """Connects the output of another gate to the pin.
        
        Args:
            source: The gate whose output will be connected to the current gate's pin.
        
        Raises:
            RuntimeError: If the pin is already occupied.
        """
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

 
class Connector:
    """
    A class representing a connector that links two gates in a logic circuit.

    Attributes:
        from_gate (LogicGate): The gate that provides the output.
        to_gate (LogicGate): The gate that receives the input.

    Methods:
        get_from(): Returns the gate that provides the output.
        get_to(): Returns the gate that receives the input.
    """
    
    def __init__(self, from_gate: LogicGate, to_gate: LogicGate) -> None:
        """Initializes a Connector instance that connects two gates.
        
        Args:
            from_gate (LogicGate): The gate that provides the output.
            to_gate (LogicGate): The gate that receives the input.
        
        This constructor automatically connects the 'from_gate' output to the 'to_gate' input.
        """
        self.from_gate = from_gate
        self.to_gate = to_gate
        
        # Automatically connects the 'to_gate' input pin to the connector
        to_gate.set_next_pin(self)

    def get_from(self) -> LogicGate:
        """Returns the gate that provides the output to this connector."""
        return self.from_gate

    def get_to(self) -> LogicGate:
        """Returns the gate that receives the input from this connector."""
        return self.to_gate
   
    
        
class AndGate(BinaryGate):
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        BinaryGate.__init__(self, label, input_a, input_b)

    def perform_gate_logic(self):
        if self.get_pin_a() == 1 and self.get_pin_b() == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        BinaryGate.__init__(self, label, input_a, input_b)

    def perform_gate_logic(self):
        if self.get_pin_a() == 1 or self.get_pin_b() == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, label: str, input_: int = None) -> None:
        UnaryGate.__init__(self, label, input_)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1
    
class NandGate(BinaryGate):
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        BinaryGate.__init__(self, label, input_a, input_b)
    
    def perform_gate_logic(self):
        if self.get_pin_a() == 1 and self.get_pin_b() == 1: 
            return 0
        else:
            return 1
        
class NorGate(BinaryGate):
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        BinaryGate.__init__(self, label, input_a, input_b)
    
    def perform_gate_logic(self):
        if self.get_pin_a() == 0 and self.get_pin_b() == 0: 
            return 1
        else:
            return 0
        
class XorGate(BinaryGate):
    def __init__(self, label: str, input_a: int = None, input_b: int = None) -> None:
        BinaryGate.__init__(self, label, input_a, input_b)
    
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if ((a==1 and b==0) or (a==0 and b==1)):
            return 1
        else:
            return 0
        

    
if __name__ == "__main__":
    # g1 = AndGate("G1 - And")
    # g2 = AndGate("G2 - And")
    # g3 = OrGate("G3 - Or")
    # g4 = NotGate("G4 - Not")
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    # print(g4.get_output())
    
    
    # g1 = AndGate("G1 - And")
    # g2 = AndGate("G2 - And")
    # g3 = OrGate("G3 - Or")
    # g4 = NotGate("G4 - Not")   
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    # print(f"Result of NOT (( A and B) or (C and D)): {g4.get_output()}\n")
    
    # g5 = AndGate("G5 - And")
    # g6 = NotGate("G6 - Not")
    # g7 = NotGate("G7 - Not")
    # c4 = Connector(g1, g6)
    # c5 = Connector(g2, g7)
    # c6 = Connector(g6, g5)
    # c7 = Connector(g7, g5)
    # print(f"Result of NOT( A and B ) and NOT (C and D): {g5.get_output()}\n")
    
    # Half Adder
    g1 = XorGate("G1 - Xor")
    g2 = AndGate("G2 - Carry")