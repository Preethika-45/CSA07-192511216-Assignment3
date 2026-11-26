import socket,hashlib
from pathlib import Path
HOST,PORT="127.0.0.1",50507; p=Path("Task07/sample_file.bin")
if not p.exists(): p.write_bytes(b"Non-sensitive sample transfer data.\n"*100)
data=p.read_bytes(); print("Sending bytes:",len(data)); print("SHA-256:",hashlib.sha256(data).hexdigest())
with socket.create_connection((HOST,PORT)) as c: c.sendall(data)
print("Transfer completed; compare hashes.")
