import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2** 31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2** random.randrange(0, 8)
        b.append(c)
    return bytes(b)

key = KeyStream(10)
message = "Hellow, World! I am here to declare that I will take over the universe and become the supreme emperor".encode()
print("Message: ", message)
cipher = encrypt(key, message)
print("Cipher: ", cipher)

cipher = transmit(cipher, 12)
#print(cipher)

key = KeyStream(10)
message = encrypt(key, cipher)
print(message)

