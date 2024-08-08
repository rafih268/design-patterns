import sqlite3
from adapters.database_adapter import DatabaseAdapter

class SqliteAdapter(DatabaseAdapter):
    
  def get_connector(self):
    return sqlite3

  def is_connected(self):
    return True
  
  def set_config(self, config):
    self.database = config["database"]
    self.placeholder = config["placeholder"]

  def get_connection_params(self):  
    return {
      'database': self.database,
    }