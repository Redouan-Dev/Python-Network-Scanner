import socket
import argparse
import sys


def is_tcp_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if a TCP connection to (host, port) succeeds within timeout."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            # connect_ex returns 0 when the connection succeeds
            return sock.connect_ex((host, port)) == 0
        except (OSError, socket.timeout):
            return False


def expand_port_range(port_range: str) -> list[int]:
    """Expand a range like '1-1024' into a list of ports. Returns [] if invalid."""
    try:
        start_str, end_str = port_range.split("-", 1)
        start = int(start_str)
        end = int(end_str)
    except ValueError:
        return []

    if start < 1 or end > 65535 or start > end:
        return []

    return list(range(start, end + 1))


def scan_ports(host: str, ports: list[int], timeout: float = 0.5) -> dict[int, bool]:
    """Scan TCP ports on a host and return port -> open/closed."""
    results: dict[int, bool] = {}

    for port in set(ports):
        if not isinstance(port, int):
            continue
        if port < 1 or port > 65535:
            continue

        results[port] = is_tcp_port_open(host, port, timeout)

    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")

    parser.add_argument("host", help="Target hostname or IP address")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--ports",
        nargs="+",
        type=int,
        help="List of ports to scan (e.g. --ports 22 80 443)",
    )
    group.add_argument(
        "--range",
        dest="port_range",
        help="Port range to scan (e.g. --range 1-1024)",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=0.5,
        help="Connection timeout in seconds (default: 0.5)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.ports is not None:
        ports = args.ports
    else:
        ports = expand_port_range(args.port_range)
        if not ports:
            print(f"Error: invalid port range '{args.port_range}' (expected like 1-1024)")
            sys.exit(1)

    results = scan_ports(args.host, ports, timeout=args.timeout)

    for port in sorted(results):
        status = "OPEN" if results[port] else "closed"
        print(f"{args.host}:{port} -> {status}")
