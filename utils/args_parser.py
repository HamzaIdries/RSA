import argparse as ap

def get_args():
    parser = ap.ArgumentParser(
        prog='RSA',
        description='Encrypts and decrypts files using RSA, and generates valid key pairs'
    )
    subparsers = parser.add_subparsers(help='Supported commands', dest='commands')
    encrypt_parser = subparsers.add_parser('encrypt')
    decrypt_parser = subparsers.add_parser('decrypt')
    generate_parser = subparsers.add_parser('generate')
    encrypt_parser.add_argument('-i', '--input', metavar='INPUT', required=True, help='specify path to the input file', nargs=1, type=ap.FileType('rb'))
    encrypt_parser.add_argument('-o', '--output', metavar='OUTPUT', required=True, help='specify path to the output file', nargs=1, type=ap.FileType('wb'))
    encrypt_parser.add_argument('-k', '--key', metavar='KEY', required=True, help='specify path to the key file', nargs=1, type=ap.FileType('r'))
    decrypt_parser.add_argument('-i', '--input', metavar='INPUT', required=True, help='specify path to the input file', nargs=1, type=ap.FileType('rb'))
    decrypt_parser.add_argument('-o', '--output', metavar='OUTPUT', required=True, help='specify path to the output file', nargs=1, type=ap.FileType('wb'))
    decrypt_parser.add_argument('-k', '--key', metavar='KEY', required=True, help='specify path to the key file', nargs=1, type=ap.FileType('r'))
    generate_parser.add_argument('--private', metavar='PRIVATE_KEY', required=True, help='where to store private key file', nargs=1, type=ap.FileType('w'))
    generate_parser.add_argument('--public', metavar='PUBLIC_KEY', required=True, help='where to store public key file', nargs=1, type=ap.FileType('w'))
    return parser.parse_args()