#!/usr/bin/env python3

import sys, argparse, ipaddress


def parse_args(args):

    parser = argparse.ArgumentParser() # starts a parset
    parser.add_argument("network", nargs="+", help="network to expand; CIDR, dashed, or splat format")
    parser.add_argument("-r", "--random", action="store_true")

    parsed = parser.parse_args()
    return parsed


def validate_args(parsed):

    if ("-" in parsed.network):
        pass  # need to do some logic to...
              # get the net and to store the range




def main(args):

    parsed = parse_args(args)
    print('hi')


if __name__ == "__main__":

    main(sys.argv)

