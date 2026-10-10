class CuentaBancaria:

  def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
    self.numero_cuenta = numero_cuenta
    self.titular = titular
    if saldo_inicial < 0:
      raise ValueError("El saldo inicial no puede ser negativo.")
    self._saldo = float(saldo_inicial)