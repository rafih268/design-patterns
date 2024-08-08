from abc import ABC, abstractmethod

class DatabaseAdapter(ABC):
  
  #config details
  host = 'localhost'
  user = ''
  password = ''
  database = ''
  connection = None
  port = 0
  placeholder = '%s'

  def __init__(self):
    if self.__class__ == DatabaseAdapter:
      raise Exception("Can't instantiate an abstract class")

  @abstractmethod
  def get_connection_params(self):
    pass

  @abstractmethod
  def set_config(self, config):
    pass

  @abstractmethod
  def get_connector(self):
    pass

  @abstractmethod
  def is_connected(self):
    pass

  def connect(self):
    if (self.connection is None) or (not self.is_connected()):
      self.connection = self.get_connector().connect(**self.get_connection_params())

  def get_connection(self):
    return self.connection
  
  def get_cursor(self):
    return self.get_connection().cursor()

  def commit(self):
    return self.get_connection().commit()
  
  def close(self):
    self.get_cursor().close()
    self.get_connection().close()

  def convert_list_to_string(self, values):
    return ','.join(values)
  
  def insert(self, table, data):
    self.connect()
    column_names = []
    column_values = []

    for key, value in data.items():
      column_names.append(key)
      column_values.append(value)

    column_string = self.convert_list_to_string(column_names)
    placeholders = ','.join([self.placeholder] * len(data))
    values = tuple(column_values)

    sql = (
        f"INSERT INTO {table} (%s)"
        "VALUES (%s)"
    )% (column_string, placeholders)

    self.get_cursor().execute(sql, values)
    self.commit()