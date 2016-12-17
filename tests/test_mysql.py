from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_mysql_socket(Socket):
    assert Socket('tcp://0.0.0.0:3306').is_listening


def test_mysql_service(Service):
    assert Service('mysql').is_enabled
    assert Service('mysql').is_running


def test_mysql_alias(File):
    assert File('/etc/aliases').contains('mysql:')


def test_mysql_ssl_group(User):
    assert 'ssl-cert' in User('mysql').groups


def test_mysql_admin_account(Command, Sudo):
    with Sudo():
        'localhost' in Command(
            '''mysql --defaults-file=/etc/mysql/debian.cnf --database mysql --execute 'select Host from user where User="admin"' ''').stdout  # noqa: E501


def test_mysql_backup_job(Command, Sudo):
    with Sudo('nobody'):
        'mysql-backup' in Command('crontab -l').stdout


def test_mysql_backup_account(Command, Sudo):
    with Sudo():
        'localhost' in Command(
            '''mysql --defaults-file=/etc/mysql/debian.cnf --database mysql --execute 'select Host from user where User="backup"' ''').stdout  # noqa: E501


def test_mysql_backup_config(File):
    backup_config = File('/etc/mysql/mysqldump.cnf')
    assert backup_config.user == 'nobody'
    assert backup_config.group == 'nogroup'
    assert backup_config.mode == 0o0400
    assert backup_config.contains('user = backup')


def test_mysql_backup_directory(File):
    backup_dir = File('/var/backups/mysql')
    assert backup_dir.is_directory
    assert backup_dir.user == 'nobody'
    assert backup_dir.group == 'nogroup'
    assert backup_dir.mode == 0o0700


def test_mysql_backup(Command, Sudo):
    with Sudo('nobody'):
        mysql_backup = Command('mysql-backup')
    assert mysql_backup.rc == 0
    assert mysql_backup.stderr == ''
