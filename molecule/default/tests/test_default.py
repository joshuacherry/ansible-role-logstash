"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    """
    Tests that the hosts file exists
    """
    file = host.file('/etc/hosts')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_logstash_is_installed(host):
    """
    Tests that logstash is installed
    """
    logstash_package = "logstash"

    logstash = host.package(logstash_package)
    assert logstash.is_installed


def test_logstash_running_and_enabled(host):
    """
    Tests that logstash is running and enabled
    """
    logstash = host.service("logstash")
    assert logstash.is_running
    assert logstash.is_enabled
