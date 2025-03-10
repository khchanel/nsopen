
import argparse
from .nsopen import *


def main():
    parser = argparse.ArgumentParser(description="Perform DNS lookup and open IP addresses in a browser")
    parser.add_argument("hostname", help="The hostname to lookup")
    parser.add_argument("-p", "--protocol",
                        choices=['http','https'],
                        default="https",
                        help="The URL protocol to use (default: https)"
                        )
    parser.add_argument("path", nargs="?", default=None, help="[Optional] path to append to the URL (e.g. /elmah.axd)")
    args = parser.parse_args()


    ip_addresses = lookup(args.hostname)
    if ip_addresses is not None:
        browser_open(ip_addresses, args.protocol, args.path)


if __name__ == "__main__":
    main()
