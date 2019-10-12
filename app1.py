import socket
import ssl
import json

try:
    print("Client connecting on port 8080 using SSL")
    diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(diamondSock,
                               ca_certs="server.crt",
                               cert_reqs=ssl.CERT_REQUIRED)
    ssl_sock.connect(('localhost', 8080))
    jsonString = """{"name": "Dylan","lastName": "Palaia","age": 25,"graduated": true, "balance": null}"""
    ssl_sock.send(bytes(jsonString, "utf-8"))
    
    outfile = open('jsonPayload.json', 'w')
    json.dump(jsonString, outfile)
    outfile.close()
    
except Exception as e:
    print(e)
    print(ssl_sock.cipher())
ssl_sock.close()
