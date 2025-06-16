# TLS Encryption
This repository contains practicum materials for the "Introduction to Computer Networks" course. It provides a hands-on demonstration of how Transport Layer Security (TLS) is crucial for securing network communications against Man-in-the-Middle (MITM) attacks.

Using the provided python client and certificates, you can simulate and observe the difference between encrypted and unencrypted traffic with a packet sniffer like Wireshark. You can also import the private key directly into Wireshark to see how it can decrypt the message even when you're using TLS.
This demonstrates that even with TLS, there is still a possibility that an attacker might intercept the data transmitted if they have the private key.
There is also a UDP client that is encrypted manually using RSA with the same key that you may try.

In order to run this repository, you will need to install python and run the file accordingly with a bit of modification to the server IP.
You do not need to modify the file structure; otherwise, it might cause further errors in the client program. Ensure that the server IP is reachable within your current network. If you're outside the campus network, please use a VPN tunnel to access the server's private IP.

> [!CAUTION]
> The current implementation of TLS has some known issues, which are outlined below.
> - Concurrent connection issues with the HTTPS server. Kindly ask your practicum assistant to restart the server if the connection takes too long.
> - For the practicum assistant or the person in charge, consider using DTLS instead of basic RSA encryption when sending data over a UDP connection.
