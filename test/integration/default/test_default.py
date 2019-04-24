def test_mlocate_is_installed(host):
    package = host.package("mlocate")
    assert package.is_installed

def test_apache_installed(host):
    package = host.package("httpd")
    assert package.is_installed

def test_ssh_is_listening(host):
    assert host.socket("tcp://:::22").is_listening

def test_http_is_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening