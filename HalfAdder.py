from LogicGate import *

def halfAdder(A, B):
    sum = XOR(A, B)
    carry = AND(A, B)

    return sum, carry
