from base64 import b64decode

text: str

# read the file content
with open('b64.txt', 'r') as file:  
    text = file.readline()

# Decode 50 times 
for i in range(50):
    text = b64decode(text)
    
print(text.decode())
