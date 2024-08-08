from abc import ABC, abstractmethod
from adapters.database_adapter import DatabaseAdapter

class DatabaseAdapterFactory(ABC):

  @abstractmethod
  def create_adapter(self, config) -> DatabaseAdapter:
    pass