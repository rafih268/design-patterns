from adapters.database_adapter import DatabaseAdapter
from adapters.mariadb_adapter import MariadbAdapter
from factories.database_adapter_factory import DatabaseAdapterFactory

class MariadbAdapterFactory(DatabaseAdapterFactory):

  def create_adapter(self, config) -> DatabaseAdapter:
    adapter = MariadbAdapter()
    adapter.set_config(config)
    adapter.connect()

    return adapter