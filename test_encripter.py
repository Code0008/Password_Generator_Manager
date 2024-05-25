import base64

count=0
hexed = []
x="me gusta ...." #Mensaje encriptar 
hexed = [hex(ord(i)+5) for i in x]
hexed = ''.join([''.join(hexede.split("0x")).upper() for hexede in hexed])

text = hexed.encode()
print(hexed)

printe= base64.b16decode(text)
print(printe)
