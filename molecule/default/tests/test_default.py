import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


# Test that UMD release is there and that it has the right version
def test_umd_version(host):
    umd_package = host.package('umd-release')
    assert umd_package.is_installed
    assert umd_package.version.startswith("4")


# Test that repositories are properly configured
def test_repositories(host):

    if (host.system_info.distribution == 'debian'):
        print "it's a debian daddy"
        # debian stuff

    if(host.system_info.distribution == 'redhat'):
        print "it's a redhat daddy"
        if(host.system_info.release >= '6'):
            print str(host.system_info.release)

    print str(host.system_info.distribution)
