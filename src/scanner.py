import socket


def is_tcp_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if a TCP connection to (host, port) succeeds within timeout."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            return sock.connect_ex((host, port)) == 0
        except (OSError, socket.timeout):
            return False


def scan_ports(host: str, ports: list[int], timeout: float = 0.5) -> dict[int, bool]:
    """
    Scan a list of TCP ports on a host.
    Returns a mapping of port -> open/closed.
    """
    results: dict[int, bool] = {}

    for port in ports:
        results[port] = is_tcp_port_open(host, port, timeout)

    return results


if __name__ == "__main__":
    host = "127.0.0.1"
    ports = [22, 80, 443]

    results = scan_ports(host, ports)

    for port in ports:
        status = "OPEN" if results[port] else "closed"
        print(f"{host}:{port} -> {status}")
