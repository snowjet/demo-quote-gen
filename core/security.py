from cryptography.fernet import Fernet

def encryt(cleartext_string, secret_key):
    key = secret_key.encode("utf-8")
    cipher_suite = Fernet(key)
    cipher_text_bytes = cipher_suite.encrypt(cleartext_string.encode("utf-8"))

    return cipher_text_bytes

def decrypt(cipher_text_string, secret_key):
    key = secret_key.encode("utf-8")
    cipher_suite = Fernet(key)
    cleartext_string = cipher_suite.decrypt(cipher_text_string.encode("utf-8")).decode("utf-8")
    
    return cleartext_string
