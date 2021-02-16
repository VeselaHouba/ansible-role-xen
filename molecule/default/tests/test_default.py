import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_xen_is_installed(host):
    f = host.file("/etc/xen")
    assert f.exists
    assert f.is_directory
