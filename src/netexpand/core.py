import ipaddress
import random

def expand_network(network_str):
    """
    Takes a network string (CIDR, dashed, or splat) and yields ipaddress.IPv4Network objects.
    """
    if '*' in network_str:
        start = network_str.replace('*', '0')
        end = network_str.replace('*', '255')
        network_str = f"{start}-{end.split('.')[-1]}"

    if '-' in network_str:
        pre_dash, post_dash = network_str.split('-', 1)
        parts = pre_dash.split('.')
        base_prefix = '.'.join(parts[:-1]) + '.' if len(parts) > 1 else ''
        
        start_ip = ipaddress.IPv4Address(pre_dash)
        end_ip = ipaddress.IPv4Address(f"{base_prefix}{post_dash}")
        
        yield from ipaddress.summarize_address_range(start_ip, end_ip)
        return

    yield ipaddress.IPv4Network(network_str, strict=False)

def get_components(networks, component_type, randomize=False):
    """
    Yields the requested components (hosts, networks, etc.) from an iterable of IPv4Networks.
    """
    # Collapse overlapping networks to deduplicate without using a memory-heavy set()
    collapsed_nets = list(ipaddress.collapse_addresses(networks))

    if randomize:
        # Calculate total memory footprint before executing
        total_items = 0
        for net in collapsed_nets:
            if component_type == 'hosts':
                total_items += net.num_addresses if net.prefixlen in (31, 32) else net.num_addresses - 2
            else:
                total_items += 1

        # Hard limit: 65,536 (a /16 network) to prevent OOM
        if total_items > 65536:
            raise MemoryError(f"Cannot randomize {total_items} items in memory. Maximum allowed for -r is 65536 (a /16 network). Remove -r to stream output.")

        # If safe, load into memory, shuffle, and yield
        results = []
        for net in collapsed_nets:
            if component_type == 'hosts':
                results.extend(str(host) for host in net.hosts())
            elif component_type == 'networks':
                results.append(str(net))
            elif component_type == 'broadcast':
                results.append(str(net.broadcast_address))
                
        random.shuffle(results)
        yield from results
        return

    # STANDARD STREAMING MODE (Zero Memory Footprint)
    for net in collapsed_nets:
        if component_type == 'hosts':
            for host in net.hosts():
                yield str(host)
        elif component_type == 'networks':
            yield str(net)
        elif component_type == 'broadcast':
            yield str(net.broadcast_address)