import socket

def is_tcp_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    """
    Check whether a TCP port is reachable by attempting a connection.
    Returns True on success, otherwise False.
    """
    # Using a context manager ensures the socket is always closed.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)

        # connect_ex returns 0 when the connection succeeds.
        try:
            return sock.connect_ex((host, port)) == 0
        except (OSError, socket.timeout):
            return False


if __name__ == "__main__":
    # Quick local test while building (we'll replace this with a proper CLI soon).
    host = "127.0.0.1"
    ports = [22, 80, 443]

    for port in ports:
        status = "OPEN" if is_tcp_port_open(host, port) else "closed"
        print(f"{host}:{port} -> {status}")
