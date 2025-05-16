import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

with open("cert.pem", "rb") as f:
    server_pub_key = RSA.import_key(f.read())

encrypt_cipher = PKCS1_v1_5.new(server_pub_key)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 4445)

print("UDP RSA Client started. Type messages:")

while True:
    msg = input("You: ")
    if not msg:
        continue

    encrypted = encrypt_cipher.encrypt(msg.encode())
    sock.sendto(encrypted, server_address)

    data, _ = sock.recvfrom(4096)
    decrypted_b64 = data.decode()

    print(f"Encrypted response (Base64):\n{decrypted_b64}\n")
