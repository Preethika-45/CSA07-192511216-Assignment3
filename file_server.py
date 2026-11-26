import socket,hashlib
HOST,PORT="127.0.0.1",50507; out="Task07/received_file.bin"
with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); s.bind((HOST,PORT)); s.listen(1)
    print("Waiting on",HOST,PORT); conn,addr=s.accept()
    with conn,open(out,"wb") as f:
        print("Connected:",addr)
        while True:
            block=conn.recv(4096)
            if not block: break
            f.write(block)
data=open(out,"rb").read()
print("Received bytes:",len(data)); print("SHA-256:",hashlib.sha256(data).hexdigest())
