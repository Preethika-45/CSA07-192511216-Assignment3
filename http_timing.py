import math
rtt=.050; n=80
print(f"Non-persistent sequential: {(n+1)*2*rtt:.2f} s")
print(f"Persistent no pipelining: {(2+n)*rtt:.2f} s")
print(f"Persistent pipelining: {3*rtt:.2f} s")
print(f"Six parallel non-persistent: {2*rtt+math.ceil(n/6)*2*rtt:.2f} s")
print(f"Bundled non-persistent: {9*2*rtt:.2f} s")
print(f"Bundled persistent: {(2+8)*rtt:.2f} s")
