from HalfAdder import halfAdder
from FullAdder import fullAdder

def adder_16bit(A: list[bool], B: list[bool]):
    out = [False]*16
    out[0], temp_carry = halfAdder(A[0], B[0])
    out[1], temp_carry = fullAdder(A[1], B[1], temp_carry)
    out[2], temp_carry = fullAdder(A[2], B[2], temp_carry)
    out[3], temp_carry = fullAdder(A[3], B[3], temp_carry)
    out[4], temp_carry = fullAdder(A[4], B[4], temp_carry)
    out[5], temp_carry = fullAdder(A[5], B[5], temp_carry)
    out[6], temp_carry = fullAdder(A[6], B[6], temp_carry)
    out[7], temp_carry = fullAdder(A[7], B[7], temp_carry)
    out[8], temp_carry = fullAdder(A[8], B[8], temp_carry)
    out[9], temp_carry = fullAdder(A[9], B[9], temp_carry)
    out[10], temp_carry = fullAdder(A[10], B[10], temp_carry)
    out[11], temp_carry = fullAdder(A[11], B[11], temp_carry)
    out[12], temp_carry = fullAdder(A[12], B[12], temp_carry)
    out[13], temp_carry = fullAdder(A[13], B[13], temp_carry)
    out[14], temp_carry = fullAdder(A[14], B[14], temp_carry)
    out[15], temp_carry = fullAdder(A[15], B[15], temp_carry)

    return out
