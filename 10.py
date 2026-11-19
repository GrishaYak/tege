from ipaddress import ip_network

for n in range(32):
    print(ip_network(f'195.154.162.96/{n}', strict=0))
    