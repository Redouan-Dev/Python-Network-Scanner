import src.scanner as scanner


def test_expand_port_range_valid():
    assert scanner.expand_port_range("20-23") == [20, 21, 22, 23]


def test_expand_port_range_invalid_format():
    assert scanner.expand_port_range("abc") == []
    assert scanner.expand_port_range("20") == []
    assert scanner.expand_port_range("20-") == []
    assert scanner.expand_port_range("-25") == []


def test_expand_port_range_invalid_bounds():
    assert scanner.expand_port_range("0-10") == []
    assert scanner.expand_port_range("1-70000") == []
    assert scanner.expand_port_range("100-50") == []


def test_scan_ports_filters_invalid_ports(monkeypatch):
    # Make the test deterministic by replacing the network call
    def fake_is_open(host: str, port: int, timeout: float = 0.5) -> bool:
        return port == 80

    monkeypatch.setattr(scanner, "is_tcp_port_open", fake_is_open)

    ports = [80, 80, -1, 0, 1, 65535, 65536, "443"]
    results = scanner.scan_ports("example.com", ports, timeout=0.1)  # type: ignore[arg-type]

    assert set(results.keys()) == {80, 1, 65535}
    assert results[80] is True
    assert results[1] is False
    assert results[65535] is False
