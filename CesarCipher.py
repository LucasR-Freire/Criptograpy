def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt +=1
    return key

def get_decryption_key(key):
    dkey ={}
    for c in key:
        dkey[key[c]]= c
    return dkey


def encrypt(key, message):
    cipher =""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

key = generate_key(3)
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key,message)
print(cipher)


#dkey = generate_key(-3)
dkey = get_decryption_key((key))
dcipher = encrypt(dkey,cipher)
print(dcipher)

#this is us breaking the cipher
for i in range(27):
    dkey =generate_key(-i)
    messagex= encrypt(dkey,cipher)
    print(i)
    print(messagex)
