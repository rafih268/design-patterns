import psycopg2
from adapters.database_adapter import DatabaseAdapter

class PostgresAdapter(DatabaseAdapter):

  def get_connector(self):
    return psycopg2

  def is_connected(self):
    return not self.connection.closed

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