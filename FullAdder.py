from LogicGate import *

def fullAdder(A, B, C):
    sum = XOR(XOR(A, B), C)
    carry = OR(AND(A, B), AND(C, XOR(A, B)))

    return sum, carry