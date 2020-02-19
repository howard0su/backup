from twindb_backup.configuration import TwinDBBackupConfig


def test_azure(config_file):
    tbc = TwinDBBackupConfig(config_file=str(config_file))
    assert tbc.azure.azure_access_key == 'XXXXX'
    assert tbc.azure.azure_account == 'YYYYY'
    assert tbc.azure.endpoint == 'core.windows.net'
    assert tbc.azure.bucket == 'twindb-backups'


def test_no_azure_section(tmpdir):
    cfg_file = tmpdir.join('twindb-backup.cfg')
    with open(str(cfg_file), 'w') as fp:
        fp.write('')
    tbc = TwinDBBackupConfig(config_file=str(cfg_file))
    assert tbc.azure is None
