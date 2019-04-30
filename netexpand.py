#!/usr/bin/env python3

import sys, argparse, ipaddress, random


def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument("network", nargs="+", \
        help="network to expand; CIDR only (dashed, splat to come")
    parser.add_argument("-r", "--random", action="store_true", \
        help="randomize output IP's")

    parsed = parser.parse_args()
    return parsed


def validate_args(parsed):

    # comments for splat & dashed formats
    #count = 0
    #control = []
    networks = []
    for net in parsed.network:
        #control.append(0)
        #if ("-" in net):
        #    control[count] = 1
        #    print("net has a - : {}".format(net))
        #    pass  # need to do some logic to...
              # get the net and to store the range

        #if ("*" in net):
        #    control[count] = 2
        #    print("net has a * : {}".format(net))
        #    pass  # need to do some logic to...
              # figure out where * is, more than one, etc

        #networks.append(net)
        #count += 1

        try:
            networks.append(ipaddress.IPv4Network(net))
        except ipaddress.AddressValueError:
            print("invalid network: {}".format(net))
            exit()

    return networks


def print_hosts(networks, args):

    hosts = []
    nets = []

    for net in networks:
        nets.append(net.hosts())

    for net in nets:
        for addr in net:
            hosts.append(str(addr))

    if (args.random):
        random.shuffle(hosts)

    for host in hosts:
        
        print(host)


def main(args):

    parsed = parse_args(args)
    validated = validate_args(parsed)
    print_hosts(validated, parsed)

if __name__ == "__main__":

    main(sys.argv)

