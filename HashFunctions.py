import hashlib

m = "This is the hash value message".encode()

sha256 = hashlib.sha256()
sha256.update(m)
d = sha256.digest()

print(d)

sha256 = hashlib.sha256()
sha256.update(d)
d = sha256.hexdigest()

print(d)
