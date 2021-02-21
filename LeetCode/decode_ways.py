def decode(s):
    keys = []
    values = []
    for i in range(65, 91):
        key = chr(i)
        value = ord(key)-65+1
        keys.append(key)
        values.append(str(value))
    
    count=1
    numbers = [s[i] for i in range(len(s))]
    for 

print(decode('11311'))