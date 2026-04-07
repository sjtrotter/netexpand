import ipaddress

def expand_network(network_str):
    """
    Takes a network string (CIDR, dashed, or splat) and yields ipaddress.IPv4Network objects.
    """
    # 1. SPLAT NOTATION (e.g., 192.168.1.*)
    if '*' in network_str:
        # Convert splat to dash format
        start = network_str.replace('*', '0')
        end = network_str.replace('*', '255')
        network_str = f"{start}-{end.split('.')[-1]}"

    # 2. DASH NOTATION (e.g., 192.168.1.10-50)
    if '-' in network_str:
        pre_dash, post_dash = network_str.split('-', 1)
        
        # Figure out the base network prefix (e.g., "192.168.1.")
        parts = pre_dash.split('.')
        base_prefix = '.'.join(parts[:-1]) + '.' if len(parts) > 1 else ''
        
        start_ip_str = pre_dash
        end_ip_str = f"{base_prefix}{post_dash}"

        start_ip = ipaddress.IPv4Address(start_ip_str)
        end_ip = ipaddress.IPv4Address(end_ip_str)
        
        # Summarize address range handles the heavy lifting!
        yield from ipaddress.summarize_address_range(start_ip, end_ip)
        return

    # 3. CIDR NOTATION (e.g., 192.168.1.0/24)
    # If no CIDR is provided, strict=False assumes it's a /32 host.
    yield ipaddress.IPv4Network(network_str, strict=False)


def get_components(networks, component_type, randomize=False):
    """
    Extracts the requested components (hosts, networks, etc.) from a list of IPv4Networks.
    """
    results = set()
    
    for net in networks:
        if component_type == 'hosts':
            for host in net.hosts():
                results.add(str(host))
        elif component_type == 'networks':
            results.add(str(net))
        elif component_type == 'broadcast':
            results.add(str(net.broadcast_address))

    results_list = sorted(list(results), key=lambda ip: ipaddress.IPv4Address(ip.split('/')[0]))
    
    if randomize:
        import random
        random.shuffle(results_list)
        
    return results_list