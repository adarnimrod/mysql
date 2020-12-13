MySQL
#####

.. image:: https://travis-ci.org/adarnimrod/mysql.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/mysql

Provision a MySQL server. This role will optionally configure SSL, an admin
account, unique server-id, log to syslog, daily backups and a mail alias.
Configuration templates can be placed inside :code:`templates/mysql/conf.d/`
either inside the role or relative to the playbook. Other configuration is out
of scope for this role and are left to user using the configuration templates.

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7, Tox, Vagrant and Virtualbox. To test simply run
:code:`tox`. `Pre-commit <http://pre-commit.com/>`_ is also setup for this
project.

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/explore/.

TODO
----

- More thorough, applicative tests.
- A backup script that saves each database in its own file but in a single
  transaction without locking.
