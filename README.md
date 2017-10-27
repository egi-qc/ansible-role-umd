Unified Middleware Distribution (UMD)
=====================================

The role deploys the repository files needed to access the products
distributed by UMD, currently supported for Scientific Linux 6 and CentOS7.
This role optionally deploys the Interoperable Global Trust Federation (IGTF)
repository file.

Requirements
------------

This role requires Ansible 2.0 or higher. The only dependency is EPEL, included
in the metadata file.

Role Variables
--------------

Brief description of the variables used in the role:

    # RPM release package
    release_url: http://repository.egi.eu/sw/production/umd/4/centos7/x86_64/base/umd-release-4.0.0-1.el7.noarch.rpm

    # Path to repository files (defaults to '/etc/yum.repos.d')
    sources_dir: /etc/yum.repos.d/

    # Operating system's nickname ('sl6', 'centos7' allowed)
    nick: centos7

    # Enables the candidate repository, commonly used in the release candidate
    # verification (defaults to 'false')
    enable_candidate_repo: false

    # Enables the testing repository (defaults to 'false')
    enable_testing_repo: false

    # Enables the untested repository (defaults to 'false')
    enable_untested_repo: false

    # Enables the IGTF repository for trusted CAs (defaults to 'false')
    ca_verification: false

    # CA version (defaults to '1', only if 'ca_verification: true')
    ca_version: 1

    # CA branch (defaults to 'production', only if 'ca_verification: true')
    ca_branch: production

    # CA servers (defaults to 'repository.egi.eu', only if
    # 'ca_verification: true')
    ca_server: repository.egi.eu

    # Installs 'fetch-crl' package if enabled (defaults to 'false')
    crl_deploy: false


Dependencies
------------

- geerlingguy.repo-epel

Example Playbook
----------------

1) Installs UMD repository files (if current OS is supported)

    - hosts: all
      roles:
         - { role: ansible-umd }


2) Installs UMD repository files, enabling the candidate repository

    - hosts: all
      roles:
         - { role: ansible-umd, enable_candidate_repo: true }


3) Installs UMD repository files together with the IGTF repository of
   trusted CAs.

    - hosts: all
      roles:
         - { role: ansible-umd, ca_verification: true }
License
-------

Apache 2.0

Author Information
------------------

Pablo Orviz <orviz@ifca.unican.es>
