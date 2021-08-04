#%% Importing Libraries
import random
import sys

#%% Function code
def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range (n)])

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

# this is done by yout enemy
message = "DO ATTACK"
message = message.encode()
key = generate_key_stream(len(message))
cipher = xor_bytes(key, message)

# this is us trying to break it
print(cipher)
message= "NO ATTACK"
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
print(xor_bytes(guess_key_stream, cipher))

'''
print(key)
print(cipher)
print(xor_bytes(key, cipher))
print()
print("------------------------------------------------------------------------")
print()
print([key[i] for i in range(len(key))])
print(key)
print(hex(key[0]))
print()
print(bytes([124]))
'''
