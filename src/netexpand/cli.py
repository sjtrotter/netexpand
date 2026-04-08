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
    
    # Generator expression to lazily evaluate inputted networks
    def generate_networks():
        for net_str in parsed.network:
            try:
                yield from expand_network(net_str)
            except ValueError as e:
                print(f"invalid network: {net_str} ({e})", file=sys.stderr)
                sys.exit(1)

    try:
        # outputs is now a generator yielding strings one by one
        outputs = get_components(generate_networks(), parsed.type, parsed.random)
        for out in outputs:
            print(out)
    except MemoryError as e:
        # Catch our custom memory limit error for the randomize flag
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        # Catch Ctrl+C to exit gracefully when streaming massive networks
        sys.exit(0)

if __name__ == "__main__":
    main()