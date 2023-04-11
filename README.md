# RSA

Simple RSA implemtion.

## How to use

First you have to install the requrirements 

```bash
pip install -r requirements.txt
```

Then, you have to generate the public and private key by using this command:

```bash
python main.py generate --private <PRIVATE-KEY> --public <PUBLIC-KEY>
```

Now you have private and public key so you can encrypt and decrypt

### Encrypt
To encrypt use this command
```bash
python main.py encrypt -i <INPUT-FILE> -o <OUTPUT-FILE> -k <PUBLIC-KEY>
```
* INPUT-FILE: Is the name file (message) you want to encrypt (message.txt).
* OUTPUT-FILE: Is the name of the file that will store the encrypted message
(ciphertext.txt).
* PUBLIC-KEY: Is the public key already saved in the folder (pb.key).

### Decrypt 
To decrypt use this command
```bash
python main.py decrypt -i <INPUT-FILE> -o <OUTPUT-FILE> -k <PRIVATE-KEY>
```
* INPUT-FILE: Is the name of the file you want to decrypt (ciphertext.txt).
* OUTPUT-FILE: Is the name of the file you want to store the decrypted message at
(a.txt).
* PRIVATE-KEY: Is the private key already saved in the folder (pr.key).
