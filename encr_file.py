# import required module
from cryptography.fernet import Fernet

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to encrypt
with open('sysk.txt', 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
 
# opening the file in write mode and
# writing the encrypted data
with open('sysk.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
 
# opening the encrypted file
with open('sysk.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('sysk.txt', 'wb') as dec_file:
    dec_file.write(decrypted)