SERVERS={"root":{"in.":"tld-in","com.":"tld-com"},"tld-in":{"ac.in.":"ns-ac"},"tld-com":{"example.com.":"ns-example"},"ns-ac":{"simats.ac.in.":"ns-simats"},"ns-simats":{"results.simats.ac.in.":"10.20.30.40"},"ns-example":{"www.example.com.":"93.184.216.34"}}
cache={}
def resolve(name):
    if name in cache: return cache[name],0
    server,queries="root",0
    while True:
        queries+=1; records=SERVERS[server]
        matches=[k for k in records if name.endswith(k)]
        if not matches: raise LookupError(f"No delegation for {name} at {server}")
        hop=records[max(matches,key=len)]
        if any(ch.isdigit() for ch in hop): cache[name]=hop; return hop,queries
        server=hop
if __name__=="__main__":
    for n in ("results.simats.ac.in.","www.example.com.","results.simats.ac.in."):
        ip,q=resolve(n); print(f"{n:<24} {ip:<15} queries sent: {q}")
