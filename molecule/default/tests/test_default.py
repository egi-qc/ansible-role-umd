import os
import pytest
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


@pytest.mark.parametrize("repo_file,os_major_version", [
    ("CentOS-Base.repo", "6"),
    ("CentOS-Base.repo", "7"),
    ("UMD-4-testing.repo", "7"),
    ("EGI-trustanchors.repo", "6"),
    ("EGI-trustanchors.repo", "7"),
    ("epel.repo", "6"),
    ("epel.repo", "7"),
    ("UMD-4-base.repo", "6"),
    ("UMD-4-base.repo", "7"),
    ("UMD-4-updates.repo", "6"),
    ("UMD-4-updates.repo", "7")
    ]
)
# Test that repositories are properly configured
def test_repositories_enabled(host, repo_file, os_major_version):
    f = host.file("/etc/yum.repos.d/"+repo_file)
    assert f.exists
    assert f.uid == 0
    assert f.group == 'root'
    assert f.contains('enabled(\s)*=(\s)*1$')
