class MyClass:
  #metodo publico
  def registry(self) -> None:
    print("Start process")
    self.__verify()
    self.__verify_registry()
    self.__insert_data()

  #metodo privado
  def __verify(self) -> None:
    print("Verify data")

  def __verify_registry(self) -> None:
    print("Verify registry")

  def __insert_data(self) -> None:
    print("insert in DB")

obj = MyClass()
obj.registry()