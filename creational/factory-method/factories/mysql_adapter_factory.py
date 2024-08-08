from adapters.database_adapter import DatabaseAdapter
from adapters.mysql_adapter import MysqlAdapter
from factories.database_adapter_factory import DatabaseAdapterFactory


class MysqlAdapterFactory(DatabaseAdapterFactory):

  def create_adapter(self, config) -> DatabaseAdapter:
    adapter = MysqlAdapter()
    adapter.set_config(config)
    adapter.connect()

    return adapter