from Crypto.Util.number import getPrime
from utils.padding import pad_message, unpad_message
import utils.helper as helper
from functools import reduce

class RSA:
    def __init__(self, key_size: int = 2048) -> None:
        self.__key_size = key_size
        self.__cipher_block_size = key_size // 8
        self.__message_block_size = self.__cipher_block_size - 1

    def generate_key_pair(self) -> dict[str, tuple[str, int]]:
        p = getPrime(self.__key_size // 2)
        q = getPrime(self.__key_size // 2)
        n = p * q
        e = 2 ** 16 + 1
        d = pow(e, -1, (p - 1) * (q - 1))
        return {
            'public': (n, e),
            'private': (n, d)
        }

    
    def __encrypt_number(self, m: int, e: int, n: int) -> int:
        return pow(m, e, n)

    def __decrypt_number(self, c: int, d: int, n: int) -> int:
        return pow(c, d, n)
    
    def __merge_bytes(self, message_bytes: bytearray, block: int) -> list[int]:
        message_numbers = []
        i = 0
        while i < len(message_bytes):
            message_numbers.append(
                    helper.merge_bytes(
                        message_bytes[i: i + block]
                    )
                )
            i += block
        return message_numbers

    def __unmerge_bytes(self, message_numbers: list[int], block: int) -> bytearray:
        return reduce(
            lambda a, b: a + b, 
            [helper.unmerge_bytes(num, block) for num in message_numbers], 
            bytearray()
        )

    def encrypt_bytes(self, message_bytes: bytearray, e: int, n: int) -> bytearray:
        # 1. Pad the message
        padded_message = pad_message(message_bytes, self.__message_block_size)
        # 2. Convert bytes into numbers
        message_numbers = self.__merge_bytes(padded_message, self.__message_block_size)
        # 3. Encrypt the converted numbers
        encrypted_numbers = [self.__encrypt_number(num, e, n) for num in message_numbers]
        # 4. Convert into bytes
        encrypted_bytes = self.__unmerge_bytes(encrypted_numbers, self.__cipher_block_size)
        
        return encrypted_bytes

    def decrypt_bytes(self, cipher_bytes: bytearray, d: int, n: int) -> bytearray:
        # 1. Convert bytes to numbers
        cipher_numbers = self.__merge_bytes(cipher_bytes, self.__cipher_block_size)
        # 2. Decrypt the numbers
        decrypted_numbers = [self.__decrypt_number(num, d, n) for num in cipher_numbers]
        # 3. Convert numbers into bytes
        decrypted_bytes = self.__unmerge_bytes(decrypted_numbers, self.__message_block_size)
        # 4. Remove the padding
        message = unpad_message(decrypted_bytes, self.__message_block_size)

        return message