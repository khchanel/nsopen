import socket
import webbrowser


def lookup(hostname):
    try:
        ip_addresses = socket.gethostbyname_ex(hostname)[2]
        return ip_addresses

    except socket.gaierror as e:
        print("Error: Unable to resolve hostname")
        print(e)
        return None


def browser_open(ip_addresses, protocol, path=""):
    for ip in ip_addresses:
        url = f"{protocol}://{ip}"
        if path:
            url += f"/{path}"

        print(f"Opening: '{url}'")
        webbrowser.open(url)
