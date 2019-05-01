#!/usr/bin/env python3

import sys, argparse, ipaddress, random


def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument("network", nargs="+", \
        help="network to expand; CIDR, dashed, or splat format")
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
            new_net, cidr = net.split('/')
        except ValueError:
            new_net = net
            cidr = 0

        # case for * in net.
        # works, but may be more efficient way
        if ("*" in net):
            if (type(cidr) == str):
                invalid_net(net)

            octets = net.split('.')
            oct_val = 0
            new_net = []
            for octet in octets:
                if (octet != '*' and oct_val > 0):
                    invalid_net(net)
                elif (octet == '*'):
                    oct_val += 1
                    new_net.append(0)
                else:
                    new_net.append(octet)

            new_net_joined = ''
            for octet in new_net:
                if (new_net_joined != ''):
                    new_net_joined += '.'
                if (octet != 0):
                    cidr += 8
                new_net_joined += str(octet)
            new_net = new_net_joined

        net = new_net + '/' + str(cidr)

        try:
            networks.append(ipaddress.IPv4Network(net))
        except ipaddress.AddressValueError:
            invalid_net(net)

    return networks


def invalid_net(network):

    print("invalid network: {}".format(network))
    print("try: {} -h for help".format(__file__))
    exit()


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

