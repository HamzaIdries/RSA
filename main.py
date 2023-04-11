from utils.args_parser import get_args
from rsa.rsa import RSA
import json

if __name__ == "__main__":
    args = get_args()
    rsa = RSA()
    if 'generate' in args.commands:
        key_pair = rsa.generate_key_pair()
        json.dump(key_pair['private'], args.private[0])
        json.dump(key_pair['public'], args.public[0])
        
    elif 'encrypt' in args.commands:
        n, e = json.load(args.key[0])
        args.output[0].write(
            rsa.encrypt_bytes(args.input[0].read(), e, n)
        )
    else:
        n, d = json.load(args.key[0])
        args.output[0].write(
            rsa.decrypt_bytes(args.input[0].read(), d, n)
        )