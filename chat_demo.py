import socket,sys
HOST,PORT="127.0.0.1",50508; mode=sys.argv[1] if len(sys.argv)>1 else "client"
if mode=="server":
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); s.bind((HOST,PORT)); s.listen(1)
        print("Chat server waiting..."); conn,_=s.accept()
        with conn:
            while True:
                data=conn.recv(1024)
                if not data: break
                print("Client:",data.decode(errors="replace")); conn.sendall(b"ACK: "+data)
elif mode=="client":
    with socket.create_connection((HOST,PORT)) as c:
        while True:
            msg=input("Message (quit to stop): ")
            if msg.lower()=="quit": break
            c.sendall(msg.encode()); print(c.recv(1024).decode(errors="replace"))
else: raise SystemExit("Use: python Task07/chat_demo.py server|client")
