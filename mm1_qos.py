def mm1(lam,mu):
    if lam>=mu: return None
    rho=lam/mu; return rho,rho/(1-rho),1/(mu-lam)
if __name__=="__main__":
    mu=1000
    for lam in (500,800,900,950,990,1000):
        r=mm1(lam,mu)
        if r is None: print(f"load {lam:4d} pkt/s: unstable, queue grows without limit")
        else:
            rho,L,W=r; print(f"load {lam:4d} pkt/s: rho {rho:.2f} L {L:6.1f} pkts W {W*1000:6.1f} ms")
    try:
        import matplotlib.pyplot as plt
        loads=list(range(100,1000,25)); plt.plot(loads,[mm1(x,mu)[2]*1000 for x in loads])
        plt.xlabel("Arrival rate (packets/s)"); plt.ylabel("Average delay (ms)"); plt.grid(True)
        plt.savefig("Task05/mm1_delay.png",dpi=160,bbox_inches="tight")
    except ImportError: print("Install matplotlib to create graph.")
