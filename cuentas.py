class CuentaBancaria:

  def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
    self.numero_cuenta = numero_cuenta
    self.titular = titular
    if saldo_inicial < 0:
      raise ValueError("El saldo inicial no puede ser negativo.")
    self._saldo = float(saldo_inicial)



class CuentaAhorros(CuentaBancaria):

  def __init__(
      self,
      numero_cuenta: str,
      titular: str,
      tasa_interes: float,
      saldo_inicial: float = 0.0,
  ):
    super().__init__(numero_cuenta, titular, saldo_inicial)
    self.tasa_interes = tasa_interes

  def calcular_interes(self) -> float:
    return self.consultar_saldo() * (self.tasa_interes / 100)

  def __str__(self) -> str:
    base = super().__str__()
    return (
        f"{base} | Tasa Interés: {self.tasa_interes}% | Interés Anual: S/"
        f" {self.calcular_interes():.2f}"
    )