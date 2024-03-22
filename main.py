# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad
#
#
# def encrypt_AES(message, key):
#     cipher = AES.new(key, AES.MODE_ECB)
#     ciphertext = cipher.encrypt(pad(message, AES.block_size))
#     return ciphertext
#
# def decrypt_AES(ciphertext, key):
#     cipher = AES.new(key, AES.MODE_ECB)
#     decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
#     return decrypted_message
#
# message = b"Hello, AES!"
# key = get_random_bytes(16)
# print("Исходное сообщение:", message)
#
# encrypted_message = encrypt_AES(message, key)
# print("Зашифрованное сообщение:", encrypted_message)
#
# decrypted_message = decrypt_AES(encrypted_message, key)
# print("Расшифрованное сообщение:", decrypted_message)

from aesCiphers.aesCipher import aesCipher
aesCipher = aesCipher(4, 4, 10)
key = "My key"
plaintext = "Hello"
padded_plaintext = aesCipher.pad_message(plaintext)
print("Text:", padded_plaintext)
ciphertext = aesCipher.encrypt(padded_plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = aesCipher.decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)