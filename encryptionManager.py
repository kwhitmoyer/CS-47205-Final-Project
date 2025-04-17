import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def hashPassword(userPassword):
    passwordBytes = userPassword.encode('utf-8')
    hashedPassword = hashlib.sha256(passwordBytes).digest()
    return hashedPassword

def encrypt(plaintext):
    aes_key = get_random_bytes(32)
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    print("The message was encrypted successfully: " + plaintext.decode('utf-8'))
    return(aes_key, cipher.nonce, ciphertext, tag)

def decrypt(aes_key, nonce, ciphertext, tag):
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try: 
        cipher.verify(tag)
        print("The message was decrypted successfully: " + plaintext.decode('utf-8'))
        return plaintext
    except ValueError:
        print("Message is corrupted.")
            

if __name__ == "__main__":
    print("Testing encryption mangager...")
    password = "testPassword"
    print("The unhashed password is: " + password)
    hashedPassword = hashPassword(password)
    print("The hashed password is: " + hashedPassword.hex())

    aes_key, nonce, ciphertext, tag = encrypt(hashedPassword)
    print("The encrypted text is: " + ciphertext.hex())
    decrypted = decrypt(aes_key, nonce, ciphertext, tag)
    print("The decrypted text is: " + decrypted.hex())

