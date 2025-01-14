class LogicGate:
    def __init__(self, label: str) -> None:
        self.label = label
        self.output = None
    
    def get_label(self):
        return self.label
    
    def get_output(self): 
        self.output = self.perform_gate_logic()
        return self.output
     
class BinaryGate(LogicGate): 
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin_a = None
        self.pin_b = None
    
    def get_pin_a(self):
        if self.pin_a == None: 
            return int(input(f"Enter pin A input for gate {self.get_label()}: "))
        else: 
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None: 
            return int(input(f"Enter pin B input for gate {self.get_label()}: "))
        else: 
            return self.pin_b.get_from().get_output()
    
    def set_next_pin(self, source):
        if self.pin_a == None: 
            self.pin_a = source
        elif self.pin_b == None: 
            self.pin_b = source
        else: 
            raise RuntimeError("Error: No Empty Pins!")
        
class UnaryGate(LogicGate):

    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input(f"Enter pin B input for gate {self.get_label()}: "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
        
class AndGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1
    
class NandGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        if self.get_pin_a() == 1 and self.get_pin_b() == 1: 
            return 0
        else:
            return 1
        
class NorGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        if self.get_pin_a() == 0 and self.get_pin_b() == 0: 
            return 1
        else:
            return 0
        
class XorGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        if (self.get_pin_a() == 1 and self.get_pin_b() == 1 or
            self.get_pin_a() == 0 and self.get_pin_b() == 0): 
            return 0
        else:
            return 1

class Connector: 
    def __init__(self, from_gate: LogicGate, to_gate: LogicGate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        
        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate
    
    
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