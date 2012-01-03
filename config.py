import ConfigParser

file = 'config.ini'
config = ConfigParser.RawConfigParser()
config.read(file)


class platform:
    type = ""
    def __init__(self):
        self.type = config.get('PLATFORM','type')

class database:
    db_host = ""
    db_port = 3306
    db_name = ""
    db_user = ""
    db_password = ""
    def __init__(self):
        self.db_host = config.get('DATABASE','db_host')
        self.db_port = config.getint('DATABASE','db_port')
        self.db_name = config.get('DATABASE','db_name')
        self.db_user = config.get('DATABASE','db_user')
        self.db_password = config.get('DATABASE','db_password')