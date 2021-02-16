import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_domain_save_disabled(host):
    f = host.file("/etc/default/xendomains")
    assert f.contains('^XENDOMAINS_SAVE=$')


def test_cred_service_exists(host):
    s = host.service("xen-sched-credit")
    assert s.is_enabled
