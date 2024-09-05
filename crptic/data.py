import random
from Crypto.Cipher import AES, DES, DES3, PKCS1_OAEP, Blowfish, ChaCha20
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64
import pandas as pd

# Helper functions to encrypt using different algorithms

def encrypt_aes(plaintext, key, mode=AES.MODE_CBC):
    cipher = AES.new(key, mode)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = cipher.iv
    return base64.b64encode(iv + ct_bytes).decode('utf-8')

def encrypt_des(plaintext, key, mode=DES.MODE_CBC):
    cipher = DES.new(key, mode)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), DES.block_size))
    iv = cipher.iv
    return base64.b64encode(iv + ct_bytes).decode('utf-8')

def encrypt_3des(plaintext, key, mode=DES3.MODE_CBC):
    cipher = DES3.new(key, mode)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), DES3.block_size))
    iv = cipher.iv
    return base64.b64encode(iv + ct_bytes).decode('utf-8')

def encrypt_blowfish(plaintext, key, mode=Blowfish.MODE_CBC):
    cipher = Blowfish.new(key, mode)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), Blowfish.block_size))
    iv = cipher.iv
    return base64.b64encode(iv + ct_bytes).decode('utf-8')

def encrypt_chacha20(plaintext, key):
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    nonce = cipher.nonce
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def encrypt_rsa(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

# Generate dataset

num_samples = 1000
data = []

for _ in range(num_samples):
    plaintext = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(5, 20)))

    # Randomly select an algorithm
    algo_choice = random.choice(['AES', 'DES', '3DES', 'Blowfish', 'Camellia', 'ChaCha20', 'RSA'])

    if algo_choice == 'AES':
        key = get_random_bytes(16)  # 128-bit key
        mode = AES.MODE_CBC
        ciphertext = encrypt_aes(plaintext, key, mode)
        iv = base64.b64encode(key[:16]).decode('utf-8')
        mode = "CBC"

    elif algo_choice == 'DES':
        key = get_random_bytes(8)  # 64-bit key
        mode = DES.MODE_CBC
        ciphertext = encrypt_des(plaintext, key, mode)
        iv = base64.b64encode(key[:8]).decode('utf-8')
        mode = "CBC"

    elif algo_choice == '3DES':
        key = DES3.adjust_key_parity(get_random_bytes(24))  # 192-bit key
        mode = DES3.MODE_CBC
        ciphertext = encrypt_3des(plaintext, key, mode)
        iv = base64.b64encode(key[:8]).decode('utf-8')
        mode = "CBC"

    elif algo_choice == 'Blowfish':
        key = get_random_bytes(16)  # Blowfish allows variable key size
        mode = Blowfish.MODE_CBC
        ciphertext = encrypt_blowfish(plaintext, key, mode)
        iv = base64.b64encode(key[:8]).decode('utf-8')
        mode = "CBC"


    elif algo_choice == 'ChaCha20':
        key = get_random_bytes(32)  # 256-bit key
        ciphertext = encrypt_chacha20(plaintext, key)
        iv = base64.b64encode(key[:12]).decode('utf-8')
        mode = "ChaCha20"

    elif algo_choice == 'RSA':
        key = RSA.generate(2048)
        public_key = key.publickey()
        ciphertext = encrypt_rsa(plaintext, public_key)
        iv = "N/A"
        mode = "N/A"

    data.append({
        'Plaintext': plaintext,
        'Ciphertext': ciphertext,
        'Algorithm': algo_choice,
        'Key': base64.b64encode(key.export_key(format='PEM')).decode('utf-8') if algo_choice == 'RSA' else base64.b64encode(key).decode('utf-8') if isinstance(key, bytes) else "N/A",
        'Mode': mode,
        'IV': iv
    })

# Convert to DataFrame
df = pd.DataFrame(data)
df.to_csv('crypto_dataset.csv', index=False)  # Save dataset to CSV file
