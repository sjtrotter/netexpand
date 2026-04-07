import sys
import argparse
from .core import expand_network, get_components

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown (not installed via pip/git)"

def parse_args(args):
    parser = argparse.ArgumentParser(
        description="Expands networks given in CIDR, dashed, or splat format."
    )
    
    parser.add_argument('network', nargs='+', help="Network(s) to expand")
    parser.add_argument('-r', '--random', action='store_true', help="Randomize output IPs")
    parser.add_argument(
        '-t', '--type', 
        choices=['hosts', 'networks', 'broadcast'], 
        default='hosts',
        help="Specify what component of the network to output (default: hosts)"
    )
    parser.add_argument('-V', '--version', action='version', version=f"%(prog)s version {__version__}")

    return parser.parse_args(args)

def main(args=None):
    if args is None:
        args = sys.argv[1:]
        
    parsed = parse_args(args)
    
    all_networks = []
    for net_str in parsed.network:
        try:
            # Call the generator from core.py
            all_networks.extend(expand_network(net_str))
        except ValueError as e:
            print(f"invalid network: {net_str} ({e})", file=sys.stderr)
            sys.exit(1)

    outputs = get_components(all_networks, parsed.type, parsed.random)
    
    for out in outputs:
        print(out)

if __name__ == "__main__":
    main()