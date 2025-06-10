# TLS Encryption
This repository contains practicum materials for the "Introduction to Computer Networks" course. It provides a hands-on demonstration of how Transport Layer Security (TLS) is crucial for securing network communications against Man-in-the-Middle (MITM) attacks.

Using the provided python client and certificates, you can simulate and observe the difference between encrypted and unencrypted traffic with a packet sniffer like Wireshark. You can also import the private key directly into Wireshark to see how it can decrypt the message even when you're using TLS.
This demonstrates that even with TLS, there is still a possibility that an attacker might intercept the data transmitted if they have the private key.
There is also a UDP client that is encrypted manually using RSA with the same key that you may try.

In order to run this repository, you will need to install python and run the file accordingly with a bit of modification to the server IP.
You do not need to modify the file structure; otherwise, it might cause further errors in the client program.
