class Automovil:

  def __init__(
      self,
      marca: str,
      modelo: str,
      velocidad_max: float,
      nivel_combustible: float,
      año_fabricacion: int,
  ):
    self.marca = marca
    self.modelo = modelo
    self.velocidad_max = velocidad_max
    self.nivel_combustible = nivel_combustible
    self.año_fabricacion = año_fabricacion
