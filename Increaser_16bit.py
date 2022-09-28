from HalfAdder import halfAdder
from FullAdder import fullAdder

def increaser_16bit(A: list[bool]):
    out = [False]*16
    out[0], temp_carry = halfAdder(A[0], True)
    out[1], temp_carry = fullAdder(A[1], False, temp_carry)
    out[2], temp_carry = fullAdder(A[2], False, temp_carry)
    out[3], temp_carry = fullAdder(A[3], False, temp_carry)
    out[4], temp_carry = fullAdder(A[4], False, temp_carry)
    out[5], temp_carry = fullAdder(A[5], False, temp_carry)
    out[6], temp_carry = fullAdder(A[6], False, temp_carry)
    out[7], temp_carry = fullAdder(A[7], False, temp_carry)
    out[8], temp_carry = fullAdder(A[8], False, temp_carry)
    out[9], temp_carry = fullAdder(A[9], False, temp_carry)
    out[10], temp_carry = fullAdder(A[10], False, temp_carry)
    out[11], temp_carry = fullAdder(A[11], False, temp_carry)
    out[12], temp_carry = fullAdder(A[12], False, temp_carry)
    out[13], temp_carry = fullAdder(A[13], False, temp_carry)
    out[14], temp_carry = fullAdder(A[14], False, temp_carry)
    out[15], temp_carry = fullAdder(A[15], False, temp_carry)

    return out