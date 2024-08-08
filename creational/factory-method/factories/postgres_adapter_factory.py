from adapters.database_adapter import DatabaseAdapter
from adapters.postgres_adapter import PostgresAdapter
from factories.database_adapter_factory import DatabaseAdapterFactory


class PostgresAdapterFactory(DatabaseAdapterFactory):

  def create_adapter(self, config) -> DatabaseAdapter:
    adapter = PostgresAdapter()
    adapter.set_config(config)
    adapter.connect()

    return adapter