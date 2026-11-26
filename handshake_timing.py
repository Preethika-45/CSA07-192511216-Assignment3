rtt_ms=100
for name,n in [("TCP + TLS 1.2",3),("TCP + TLS 1.3",2),("QUIC first connection",1),("QUIC 0-RTT eligible early data",0)]:
    print(f"{name:<36} {n} RTT = {n*rtt_ms} ms")
print("Excludes DNS, radio wake-up, processing and packet transmission.")
