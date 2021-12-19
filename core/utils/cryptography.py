from django.conf import settings


def encryption(plain_text):
    """Convert Plain Text into Encrypted Text"""
    ET = ''
    for i in plain_text:
        ET += chr(( ord(i) + settings.CIPHER_KEY ) % 127)
    return ET

def decryption(encrypted_text):
    """Convert Encrypted text into Plain Text"""
    PT = ''
    for i in encrypted_text:
        PT += chr(( ord(i) - settings.CIPHER_KEY) % 127)
    return PT
