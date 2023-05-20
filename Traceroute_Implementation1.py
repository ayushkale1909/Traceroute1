from scapy.all import *

def traceroute(destination, max_hops):
    # Setting the destination and maximum number of hops
    dport = 33434  # Destination port for traceroute
    ttl = 1

    while True:
        # ICMP echo request packet with ttl
        packet = IP(dst=destination, ttl=ttl) / ICMP()

      
        reply = sr1(packet, verbose=False, timeout=1)

        if reply is None:
            # No response received
            print(f"{ttl}. *")
        elif reply.type == 3:
            # Destination reached, print IP address 
            print(f"{ttl}. {reply.src}")
            break
        else:
            # Intermediate hop reached, print IP address
            print(f"{ttl}. {reply.src}")

        # Increment TTL
        ttl += 1

        if ttl > max_hops:
            # Maximum number of hops reached
            break

#example
traceroute("www.example.com", 30)