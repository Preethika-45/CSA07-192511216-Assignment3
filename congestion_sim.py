def simulate(losses,ssthresh=16,reno=True):
    cwnd,trace=1,[]
    for rtt in range(1,21):
        trace.append(cwnd)
        if rtt in losses:
            ssthresh=max(cwnd//2,2); cwnd=ssthresh if reno else 1
        elif cwnd<ssthresh: cwnd=min(cwnd*2,ssthresh)
        else: cwnd+=1
    return trace
if __name__=="__main__":
    for label,reno in (("Reno",True),("Tahoe",False)):
        tr=simulate({8,14},reno=reno)
        print(label," ".join(f"{w:2d}" for w in tr),f"| segments sent {sum(tr)}")
    try:
        import matplotlib.pyplot as plt
        for label,reno in (("Reno",True),("Tahoe",False)):
            plt.plot(range(1,21),simulate({8,14},reno=reno),marker="o",label=label)
        plt.xlabel("Round trip"); plt.ylabel("cwnd (segments)"); plt.grid(True); plt.legend()
        plt.savefig("Task02/congestion_window.png",dpi=160,bbox_inches="tight")
    except ImportError: print("Install matplotlib to create graph.")
