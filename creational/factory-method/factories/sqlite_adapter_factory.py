from adapters.database_adapter import DatabaseAdapter
from adapters.sqlite_adapter import SqliteAdapter
from factories.database_adapter_factory import DatabaseAdapterFactory

class SqliteAdapterFactory(DatabaseAdapterFactory):

  def create_adapter(self, config) -> DatabaseAdapter:
    adapter = SqliteAdapter()
    adapter.set_config(config)
    adapter.connect()

    return adapter