from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

# Known values
key = b'SecretKey1234567'
encoded_flag = bytes.fromhex('96a0299d6c60cd0f40218b73ab5fc4b710b8951bd0ed8977a1382328454a2ce68106660bb48808c2fa7a141ac863732f66f9032d00cf2c0ecc3a6871683911a6')
known_plaintext = b'Here is the flag for you: SIVBGR'

# Pad the plaintext to match the block size
padded_known_plaintext = pad(known_plaintext, AES.block_size)

# The first block of ciphertext
first_block_ciphertext = encoded_flag[:AES.block_size]

# Reverse the first block to guess the IV
cipher = AES.new(key, AES.MODE_ECB)
guessed_iv = cipher.decrypt(first_block_ciphertext)[:AES.block_size]

# Print the guessed IV
print("Guessed IV:", binascii.hexlify(guessed_iv))

# Use the guessed IV to decrypt the entire message
cipher = AES.new(key, AES.MODE_CBC, guessed_iv)
decrypted_msg = cipher.decrypt(encoded_flag)

# Unpad the decrypted message
try:
    decrypted_msg = unpad(decrypted_msg, AES.block_size)
    print("Decrypted message:", decrypted_msg.decode())
except ValueError:
    print("Failed to unpad the decrypted message. The guessed IV might be incorrect.")
