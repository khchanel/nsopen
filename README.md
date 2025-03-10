# nsopen

A command-line tool to perform DNS lookups and open resolved IP addresses in a web browser.

particularly useful when you have want to test stuff behind load-balancer which resolves into multiple server IP


## Installation
```sh
# Install in dev mode
pip install -e .

# install
pip install .
```

## Usage

Note: pip packages executable directory should be in your PATH environmental variable

```sh
# Open all IPs for google.com using HTTPS (default)
nsopen google.com

# Open specific path /elmah.axd on example.com using HTTP protocol
nsopen -p http example.com /elmah.axd
```

### Example:
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

