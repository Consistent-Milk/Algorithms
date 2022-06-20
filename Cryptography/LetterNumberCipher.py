"""
Letter to Number Cipher: Ciphertext is a list of unicode positions of each character in a string.
May be implemented with an addition or subtraction of a constant random number which may be used as a private key. 
"""
import random

def encode(plain_text: str, key: int) -> list[int]:
    encoded_list = [ord(elem) - key for elem in plain_text]
    return encoded_list


def decode(encoded: list[int], key: int) -> str:
    decoded_string = "".join(chr(elem + key) for elem in encoded)
    return decoded_string


def main() -> None:
    message = input("Enter a string to encrypt: ")
    a = int(input("Enter lower limit for the range of random key generator: "))
    b = int(input("Enter upper limit for the range of random key generator: "))
    private_key = random.randint(a, b)
    encoded_message = encode(plain_text=message, key=private_key)
    decoded_message = decode(encoded=encoded_message, key=private_key)

    print(f"Original Message: {message}")
    print(f"Ciphertext: {encoded_message}")
    print(f"Decrypted Message: {decoded_message}")


if __name__ == "__main__":
    main()
