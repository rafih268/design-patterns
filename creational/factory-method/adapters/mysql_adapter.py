import mysql.connector
from adapters.database_adapter import DatabaseAdapter

class MysqlAdapter(DatabaseAdapter):

  def get_connector(self):
    return mysql.connector
  
  def is_connected(self):
    return self.connection.is_connected()
  
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