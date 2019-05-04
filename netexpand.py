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
        print("net is:{}".format(net))
        i = parsed.network.index(net)
        print("parsed.network[i] is: {}".format(parsed.network[i]))

        while ('-' in net):
#            print(net)
            net = dashed_net_checker(net)
            if (type(net) == list):
                for n in net:
                    if (net.index(n) != 0):
                       parsed.network.append(n)
                net = net[0]
            parsed.network[i] = net
#        if (type(net) == list):
#            parsed.network.append(net[1:])
#            print(i)
#            print(net)
#            print(net[0])
#            print(parsed.network[i])
#            parsed.network[i] = net[0]
#        else:
#            print(type(net))
#            parsed.network[i] = net
    print("parsed.network is now: {}".format(parsed.network))

    for net in parsed.network:

        if (len(net.split('.')) != 4):
            invalid_net(net)

        if ('-' in net):
            dashed_net_checker(net)

        try:
            new_net, cidr = net.split('/')
        except ValueError:
            new_net = net
            cidr = 0

        if ((type(cidr) == str) and ('-' in net or '*' in net)) \
            or ('-' in net and '*' in net):
            print('more than one notation used in network')
            invalid_net(net)

##        # NOTE: should we allow mixung of notations?
#        # like... 192.168.1-3.*  ...?
#        # or...   192.168.1-6.0/30 ...?
#        # or...   192.168.*.0/30 ...?
#        # or...   192.168.*.1-7 ...?
#        #... idk...

        # case for - in net.

        # case for * in net.
        # works, but may be more efficient way
        if ("*" in net):

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
            networks.append(ipaddress.IPv4Network(net, \
                strict=False))
        except ipaddress.AddressValueError:
            invalid_net(net)

    for net in networks:
        print("net: {} - type: {}".format(net, type(net)))

    return networks


def invalid_net(network):

    print("invalid network: {}".format(network))
    print("try: {} -h for help".format(__file__))
    exit()


def dashed_net(pre_net, start, end, post_net=''):
    '''
    pre-net: prefix of the nets with ending dot (i.e. "192.168.")
    start: start of range (int)
    end: end of range (int)
    post_net: end of net
    cidr: (?) cidr of net
    '''

    nets = [ pre_net + str(x) + post_net \
        for x in range(start, end+1) ]

    #dashed_net_check(nets)

    return nets

def dashed_net_checker(net):
    pre_net, post_net = net.split('-', 1)

    start = pre_net.split('.')[-1]
    pre_net = pre_net[:-(len(start))]

    try:
        end = post_net.split('.')[0]
        post_net = post_net[len(end):]
    except ValueError:
        end = post_net

    new_net = dashed_net(pre_net, int(start), \
        int(end), post_net)
    return new_net


def dashed_net_check(net):

    octets = net.split('.')
    octet_count = 0
    starts = []
    ends = []
    indices = []
    pre_net = ''
    dash_status = 0
    for octet in octets:
        if ('-' in octet):
            start, end = octet.split('-')
            starts.append(int(start))
            ends.append(int(end))
            indices.append(octet_count)
        #TODO

        #else
        


def print_hosts(networks, args):

    hosts = []
    nets = []

    networks.sort()

    for net in networks:
        print(type(net))
        if (type(net) == ipaddress.IPv4Network):
            for host in list(net.hosts()):
                hosts.append(str(host))
        elif (type(net) == ipaddress.IPv4Address):
            hosts.append(str(net))

#    for net in nets:
#        for addr in net:
#            hosts.append(str(addr))

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

