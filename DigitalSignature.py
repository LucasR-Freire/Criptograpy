import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

#%%
# These are Alice's RSA keys:
#Public key (e,n): 7 252647
#Secret key (d) 53923
n = 252647
e = 7
d = 53923

# This is the message that Alice wants to sign and send to Bob
message = "Bob you are awesome".encode()

# Step 1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value: ", h)
# Step 2: decrypt the hash value (use secret exponent)
sign = h**d % n
#Step 3: send message with signature to Bob
print(message, sign)

print()
# This is Eve being evil and modifies the message
message = modify(message)
print(message)



print()
# Bob verifying the signature
# Step 1: Calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
b = sha256.digest()
b= int.from_bytes(b, "big") % n
stats = b == h
print("Hash are equal: ", stats)
# Step 2: Verify the signature
verification = sign**e % n
print(verification)