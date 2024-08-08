from factories.mysql_adapter_factory import MysqlAdapterFactory
from factories.postgres_adapter_factory import PostgresAdapterFactory
from factories.sqlite_adapter_factory import SqliteAdapterFactory

class Application:

  db_adapter = None

  def __init__(self, config) -> None:
    if config["adapter"] == 'mysql':
      self.db_adapter = MysqlAdapterFactory().create_adapter(config)
    elif config["adapter"] == 'postgres':
      self.db_adapter = PostgresAdapterFactory().create_adapter(config)
    elif config["adapter"] == 'sqlite':
      self.db_adapter = SqliteAdapterFactory().create_adapter(config)
    else:
      raise Exception('Unknown adapter')

  def insert(self, table, data):
    self.db_adapter.insert(table, data)