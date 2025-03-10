from nsopen.nsopen import lookup, browser_open
import webbrowser


def test_lookup_valid_hostname():
    ip_addresses = lookup("google.com")
    assert ip_addresses is not None
    assert len(ip_addresses) > 0


def test_lookup_invalid_hostname():
    ip_addresses = lookup("invalid.hostname")
    assert ip_addresses is None


def test_browser_open(mocker):
    mocker.patch('webbrowser.open')
    ip_addresses = ["127.0.0.1"]
    browser_open(ip_addresses, "http", "test")
    webbrowser.open.assert_called_with("http://127.0.0.1/test")


def test_browser_open_no_path(mocker):
    mocker.patch('webbrowser.open')
    ip_addresses = ["127.0.0.1"]
    browser_open(ip_addresses, "http")
    webbrowser.open.assert_called_with("http://127.0.0.1")
