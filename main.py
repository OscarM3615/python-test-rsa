from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

key_pair = RSA.generate(3072) # cantidad de bits

# clave pública
public_key = key_pair.publickey()
public_key_pem = public_key.exportKey()
print(public_key_pem.decode('ascii'), end='\n\n')

# clave privada
private_key_pem = key_pair.exportKey()
print(private_key_pem.decode('ascii'), end='\n\n')

# cifrado de un mensaje
message = input('Ingrese el mensaje a cifrar: ')
encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(message.encode('utf-8'))
print(f'Mensaje cifrado: {binascii.hexlify(encrypted).decode("utf-8")}', end='\n\n')

# descifrado de un mensaje
input('Presione Enter para descifrar el mensaje...')
recipient_key = RSA.import_key(private_key_pem)
decryptor = PKCS1_OAEP.new(recipient_key)
decrypted = decryptor.decrypt(encrypted)
print(f'Mensaje descifrado: {decrypted.decode("utf-8")}')
