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
        # Inicializar los 3 atributos 'privados' con guion bajo (_)
        self._velocidad_max = velocidad_max
        self._nivel_combustible = nivel_combustible
        self._año_fabricacion = año_fabricacion

    # --- @property año_fabricacion ---
    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not (1886 <= valor <= 2026):
            raise ValueError(
                f"El año de fabricación debe estar entre 1886 y 2026. Valor ingresado: {valor}"
            )
        self._año_fabricacion = int(valor)

    # --- @property nivel_combustible ---
    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not (0.0 <= valor <= 100.0):
            raise ValueError(
                f"El nivel de combustible debe estar entre 0.0 y 100.0. Valor ingresado: {valor}"
            )
        self._nivel_combustible = float(valor)

    # --- @property velocidad_max ---
    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError(
                f"La velocidad máxima debe ser mayor a 0. Valor ingresado: {valor}"
            )
        self._velocidad_max = float(valor)

    def tiempo_llegada(self, distancia_km: float) -> float:
        """Calcula el tiempo estimado de llegada en horas."""
        return distancia_km / self._velocidad_max

    def __str__(self) -> str:
        return (
            f"Automóvil: {self.marca} {self.modelo} | Año: {self._año_fabricacion} | "
            f"Vel. Máx: {self._velocidad_max} km/h | Combustible: {self._nivel_combustible}%"
        )


# Instancia de prueba al final del archivo
auto = Automovil("Toyota", "Corolla", 180.0, 75.0, 2020)
print(auto)
print(f"Tiempo de llegada: {auto.tiempo_llegada(360)} horas")