from math import gcd

def is_relatively_prime(a: int, b: int) -> bool:
    return gcd(a, b) == 1

def merge_bytes(bytes: bytearray) -> int:
    result = 0
    for byte in bytes:
        result = (result << 8) | byte
    return result

def unmerge_bytes(num: int, size: int) -> bytearray:
    result = bytearray()
    for _ in range(size):
        result.append(num & 0xFF)
        num >>= 8
    return result[::-1]