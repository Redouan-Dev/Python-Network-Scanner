# Python Network Scanner

A Python command-line tool for scanning TCP ports on a target host or IP address.

This project was built step by step to demonstrate basic network programming,
command-line interface design, and clean Git workflow.

---

## Features

- Scan specific TCP ports on a target host
- Scan a range of ports
- Clear and simple CLI using argparse
- Uses Python’s built-in socket library
- No external dependencies

---

## Requirements

- Python 3.10 or higher

This project uses only the Python standard library.

---

##  Usage

Run commands from the project root.

### Scan specific ports
```bat
python -m src.scanner 127.0.0.1 --ports 22 80 443
```

### Scan a range of ports
```bat
python -m src.scanner 127.0.0.1 --range 1-1024
```

---

## Example Output

```text
127.0.0.1:22 -> open
127.0.0.1:80 -> closed
127.0.0.1:443 -> closed
```

---

## Project Structure

```text
python-network-scanner/
├── src/
│   ├── __init__.py
│   └── scanner.py
├── tests/
│   └── test_scanner.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## What This Project Demonstrates

- Basic TCP networking with sockets
- Input validation and error handling
- Writing clean, readable Python code
- Designing a command-line interface
- Incremental development with Git

---

## Notes

- This tool is intended for learning and testing purposes.
- Only scan hosts you own or have permission to test.

---

## License

This project is open for educational use.
