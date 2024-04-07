# creating the class and its attributes
class User:
  def __init__(self, name, role):
      self.__name = name
      self.__role = role

  # name getter
  def get_name(self):
      return self.__name

  # name setter
  def set_name(self, new_name):
      self.__name = new_name

  # role getter
  def get_role(self):
      return self.__role

  # role setter
  def set_role(self, new_role):
      self.__role = new_role