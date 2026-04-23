# backend.py

def cesar_cipher(message: str, key: int) -> str:
    crypted_message = ""
    for char in message:
        crypted_message += chr((ord(char) + key) % 1_114_112)
    return crypted_message


def cesar_uncipher(crypted_message: str, key: int) -> str:
    return cesar_cipher(crypted_message, -key)