def pad_message(message_bytes: bytearray, block_size: int) -> bytearray:
    if len(message_bytes) > block_size:
        return message_bytes[:block_size] + pad_message(message_bytes[block_size:], block_size)
    elif len(message_bytes) == block_size:
        return message_bytes + bytearray([0])
    else:
        padding_ammount = block_size - len(message_bytes)
        return message_bytes + bytearray([0] * padding_ammount) + bytearray([0] * (block_size - 1) + [padding_ammount])

def unpad_message(padded_message_bytes: bytearray, block_size: int) -> bytearray:
    return padded_message_bytes[:len(padded_message_bytes) - padded_message_bytes[-1] - 255]
