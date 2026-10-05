import time, signal, sys

def graceful_shutdown(signum, frame):
    print(f"\n [+] Reveived SIGTERM ({signum}).Flushing I/O buffer and tearing down DB connections...")
    time.sleep(2)
    print("[+] System offline ")
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)

print("[+] Mock server initialized on port 8080.")
while True:
    print("[+] Processing task queue ...")
    time.sleep(3)