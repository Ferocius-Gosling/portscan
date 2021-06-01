import socket


udp_to_send = b'0' * 255 + b'1' * 255


def scan_tcp_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        try:
            sock.connect((ip, port))
            sock.send(b' '*250 + b'\r\n\r\n')
            try:
                data = sock.recv(2048)
                print('TCP ', port, get_protocol(data, port, 'tcp'))
            except socket.timeout:
                print('TCP ', port)
        except (socket.timeout, ConnectionRefusedError):
            pass
        except OSError as err:
            if 10013 == err.errno:
                print('Port ', port, ' requires permission ')


def scan_udp_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(0.5)
        try:
            sock.sendto(udp_to_send, (ip, port))
            data, addr = sock.recvfrom(2048)
        except (socket.timeout, OSError):
            pass
        except PermissionError:
            print('Port ', port, ' requires permission')
        else:
            print('UDP', port, get_protocol(data, port, "udp"))


def get_protocol(data, port, transport):
    if len(data) > 4 and b'HTTP' in data:
        return 'HTTP'
    if b'SMTP' in data or b'EHLO' in data:
        return 'SMTP'
    if b'POP3' in data or data.startswith(b'+OK') or data.startswith(b'+'):
        return 'POP3'
    if b'IMAP' in data:
        return 'IMAP'
    try:
        return socket.getservbyport(port, transport).upper()
    except OSError:
        return ''
