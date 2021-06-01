import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='hostname in network')
    parser.add_argument('-t', '--tcp_ports',
                        help='Scan TCP ports',
                        action='store_true')
    parser.add_argument('-u', '--udp_ports',
                        help='Scan UDP ports',
                        action='store_true')
    parser.add_argument('-p', '--ports', nargs=2,
                        default=[1, 65535],
                        metavar='PORT', help='Port range')
    parser.add_argument("-m", "--max", default=4,
                        help="max threads")
    # parser.add_argument("--timeout", default=1,
    #                     help="timeout in seconds")
    return parser.parse_args()
