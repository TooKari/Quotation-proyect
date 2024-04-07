# creating the class and its attributes
class Client:
  def __init__(self, name, rut, phone, mail):
      self.__name = name
      self.__rut = rut
      self.__phone = phone
      self.__mail = mail

  # Getters
  def get_name(self):
      return self.__name

  def get_rut(self):
      return self.__rut

  def get_phone(self):
      return self.__phone

  def get_mail(self):
      return self.__mail

  # Setters
  def set_name(self, new_name):
      self.__name = new_name

  def set_rut(self, new_rut):
      self.__rut = new_rut

  def set_phone(self, new_phone):
      self.__phone = new_phone

  def set_mail(self, new_mail):
      self.__mail = new_mail
