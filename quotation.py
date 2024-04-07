# creating the class and its attributes
class Quotation:

  def __init__(self, p_name, p_price, s_price, gain, p_iva, s_iva):
    self.__p_name = p_name
    self.__p_price = p_price
    self.__s_price = s_price
    self.__gain = gain
    self.__p_iva = p_iva
    self.__s_iva = s_iva

  # Getters
  def get_p_name(self):
    return self.__p_name

  def get_p_price(self):
    return self.__p_price

  def get_s_price(self):
    return self.__s_price

  def get_gain(self):
    return self.__gain

  def get_p_iva(self):
    return self.__p_iva

  def get_s_iva(self):
    return self.__s_iva

  # Setters
  def set_p_name(self, new_p_name):
    self.__p_name = new_p_name

  def set_p_price(self, new_p_price):
    self.__p_price = new_p_price

  def set_s_price(self, new_s_price):
    self.__s_price = new_s_price

  def set_gain(self, new_gain):
    self.__gain = new_gain

  def set_p_iva(self, new_p_iva):
    self.__p_iva = new_p_iva

  def set_s_iva(self, new_s_iva):
    self.__s_iva = new_s_iva
