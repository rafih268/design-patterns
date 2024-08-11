import mariadb
from adapters.database_adapter import DatabaseAdapter

class MariadbAdapter(DatabaseAdapter):

  def get_connector(self):
    return mariadb
  
  def is_connected(self):
    return True
  
  def set_config(self, config):
    self.host = config["host"]
    self.user = config["user"]
    self.password = config["password"]
    self.database = config["database"]
    self.port = config["port"]
    self.placeholder = config["placeholder"]
  
  def get_connection_params(self):
    return {
      'database': self.database,
      'user': self.user,
      'password': self.password,
      'host': self.host,
      'port': self.port
    }