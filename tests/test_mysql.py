from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_mysql_socket(Socket):
    assert Socket('tcp://0.0.0.0:3306').is_listening


def test_mysql_service(Service):
    assert Service('mysql').is_enabled
    assert Service('mysql').is_running


def test_mysql_alias(File):
    pass


def test_mysql_ssl_group(User):
    pass


def test_mysql_admin_account(Command, Sudo):
    pass


def test_mysql_backup_job(Command, Sudo):
    pass


def test_mysql_backup_account(Command, Sudo):
    pass


def test_mysql_backup_config(File):
    pass


def test_mysql_backup_directory(File):
    pass


def test_mysql_backup(Command, Sudo):
    pass
