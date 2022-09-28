from Transistor import transistor

def NAND(A, B):
    VCC = True
    GND = transistor(transistor(VCC, A), B)

    if GND:
        return False
    else:
        return True