from scan import parser, scanner
import time
import concurrent.futures


if __name__ == "__main__":
    args = parser.parse()
    start_time = time.time()
    first_port = int(args.ports[0])
    last_port = int(args.ports[1])
    max_threads = int(args.max)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in range(first_port, last_port + 1):
            if args.tcp_ports:
                # print('tcp')
                executor.submit(scanner.scan_tcp_port, args.host, i)
            if args.udp_ports:
                executor.submit(scanner.scan_udp_port, args.host, i)
