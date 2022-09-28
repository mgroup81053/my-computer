from NAND import NAND

def WIRE(A):
    return NAND(True, NAND(True, A))

def NOT(A):
    return NAND(True, A)

def AND(A, B):
    return NAND(True, NAND(A, B))

def OR(A, B):
    return NAND(NAND(True, A), NAND(True, B))

def NOR(A, B):
    return NAND(True, NAND(NAND(True, A), NAND(True, B)))
open(file="a.txt", mode = "w")
def XOR(A, B):
    return NAND(NAND(A, NAND(A, B)), NAND(B, NAND(A, B)))

def XNOR(A, B):
    return NAND(True, NAND(NAND(A, NAND(A, B)), NAND(B, NAND(A, B))))

def IMPLY(A, B):
    return NAND(A, NAND(True, B))

def IMPLY_REV(A, B):
    return NAND(B, NAND(True, A))

def NIMPLY(A, B):
    return NAND(True, NAND(A, NAND(True, B)))

def NIMPLY_REV(A, B):
    return NAND(True, NAND(B, NAND(True, A)))



def mux(A, B, sel):
    return NAND(NAND(A, NAND(True, sel)), NAND(B, sel))

def dmux(IN, sel):
    A = NAND(True, NAND(IN, NAND(True, sel)))
    B = NAND(True, NAND(IN, sel))

    return A, B