ansible-mysql
#############

An Ansible role to install and configure a MySQL server. The role creates an
admin account, force SSL usage, configures UFW and daily backup.

Requirements
------------

Debian Wheezy or later (Ubuntu Precise or later should probably work, but it's
untested).

Role Variables
--------------
::

    mysql_admin_password: #The password for the admin account.

Dependencies
------------

`Common role <https://www.shore.co.il/cgit/ansible-common/>`_

Example Playbook
----------------
::

    - hosts: servers
      roles:
      - role: mysql
        mysql_admin_password: qwerty123

Example requirements.yml
------------------------
::

    - src: https://www.shore.co.il/cgit/ansible-common
      scm: git
      path: roles/
      name: common

    - src: https://www.shore.co.il/cgit/ansible-mysql
      scm: git
      path: roles/
      name: mysql

License
-------

This software is licnesed under the MIT licese (see the ``LICENSE.txt`` file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/cgit/.

TODO
----

- Don't set a password for the root account, it's only accessible from the
  machine itself. Instead create an admin account, without root priviliges and
  with mandatory SSL for connecting. Also, other roles will set mandatory SSL
  for their connections.
