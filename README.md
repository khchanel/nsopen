# nsopen

[![build](https://github.com/khchanel/nsopen/actions/workflows/python-app.yml/badge.svg)](https://github.com/khchanel/nsopen/actions/workflows/python-app.yml)

A command-line tool to perform DNS lookups and open resolved IP addresses in a web browser.

Particularly useful when you want to test behind a load balancer that resolves into multiple server IPs.

## Installation
```sh
python -m pip install .
```

## Usage

Note: pip packages executable directory should be in your PATH environmental variable

```sh
# Open all IPs for google.com using HTTPS (default)
nsopen google.com

# Open specific path /elmah.axd on example.com using HTTP protocol
nsopen -p http example.com /elmah.axd
```

if you didnt install, you can run it via python -m
may need to add src folder to PYTHONPATH env var if you are in a different directory
```sh
python -m nsopen google.com
```

### Example

```sh
nsopen -p https example.com /about
```

### Command line options

```
usage: nsopen [-h] [-p {http,https}] hostname [path]

Perform DNS lookup and open IP addresses in a browser

positional arguments:
  hostname              The hostname to lookup
  path                  [Optional] path to append to the URL (e.g. /elmah.axd)

options:
  -h, --help            show this help message and exit
  -p, --protocol {http,https}
                        The URL protocol to use (default: https)
```

## Development

### Setup

```sh
# Install dev dependencies
pip install -r requirements-dev.txt

# (optional) install package in editable mode for CLI entry point
pip install -e .
```

### Test

If you didn't install the package, set `PYTHONPATH` so tests can import the `nsopen` package.

```powershell
# From the project root
$env:PYTHONPATH = "${PWD}\src"; pytest
```

### Tooling

Common tooling is configured in `pyproject.toml`:

- black (code formatting)
- isort (import sorting)
- flake8 (linting)
- pytest (test runner defaults)

Run them as needed, e.g.:

```powershell
black .
isort .
flake8
pytest
```
