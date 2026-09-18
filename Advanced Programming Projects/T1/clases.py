from abc import ABC, abstractmethod
from collections import namedtuple
import parametros as p
import random
import funciones as f


class Arena:

    def __init__(self, tuple: namedtuple):
        self.nombre = tuple.nombre
        self.tipo = tuple.tipo
        self.__rareza = int(tuple.rareza)
        self.__humedad = int(tuple.humedad)
        self.__dureza = int(tuple.dureza)
        self.__estatica = int(tuple.estatica)

    @property
    def rareza(self):
        return self.__rareza

    @rareza.setter
    def rareza(self, value):
        if value < 1:
            self.__rareza = 1
        elif value > 10:
            self.__rareza = 10
        else:
            self.__rareza = value

    @property
    def humedad(self):
        return self.__humedad

    @humedad.setter
    def humedad(self, value):
        if value < 1:
            self.__humedad = 1
        elif value > 10:
            self.__humedad = 10
        else:
            self.__humedad = value

    @property
    def dureza(self):
        return self.__dureza

    @dureza.setter
    def dureza(self, value):
        if value < 1:
            self.__dureza = 1
        elif value > 10:
            self.__dureza = 10
        else:
            self.__dureza = value

    @property
    def estatica(self):
        return self.__estatica

    @estatica.setter
    def estatica(self, value):
        if value < 1:
            self.__estatica = 1
        elif value > 10:
            self.__estatica = 10
        else:
            self.__estatica = value

    def dificultad_arena(self) -> float:
        # Computes a difficulty score from rareza/humedad/dureza/estatica,
        # weighted differently per arena tipo. Solution logic redacted for
        # showcase repo.
        pass


class Item (ABC):
    def __init__(self, nombre, tipo, descripcion):
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion


class Tesoro(Item):
    def __init__(self, calidad, cambio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calidad = int(calidad)
        self.cambio = cambio


class Consumible(Item):
    def __init__(self, energia, fuerza, suerte, felicidad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.energia = int(energia)
        self.fuerza = int(fuerza)
        self.suerte = int(suerte)
        self.felicidad = int(felicidad)


class Excavador(ABC):

    def __init__(self, tuple: namedtuple):
        self.nombre = tuple.nombre
        self.__edad = int(tuple.edad)
        self.__energia = int(tuple.energia)
        self.__fuerza = int(tuple.fuerza)
        self.__suerte = int(tuple.suerte)
        self.__felicidad = int(tuple.felicidad)
        self.dias_descansando = 0

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        if value < 18:
            self.__edad = 18
        elif value > 60:
            self.__edad = 60
        else:
            self.__edad = value

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, value):
        if value < 0:
            self.__energia = 0
        elif value > 100:
            self.__energia = 100
        else:
            self.__energia = value

    @property
    def fuerza(self):
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, value):
        if value < 1:
            self.__fuerza = 1
        elif value > 10:
            self.__fuerza = 10
        else:
            self.__fuerza = value

    @property
    def suerte(self):
        return self.__suerte

    @suerte.setter
    def suerte(self, value):
        if value < 1:
            self.__suerte = 1
        elif value > 10:
            self.__suerte = 10
        else:
            self.__suerte = value

    @property
    def felicidad(self):
        return self.__felicidad

    @felicidad.setter
    def felicidad(self, value):
        if value < 1:
            self.__felicidad = 1
        elif value > 10:
            self.__felicidad = 10
        else:
            self.__felicidad = value

    @abstractmethod
    def cavar(self):
        pass

    def descansar(self):
        # Rest duration scales with age; once the required rest days have
        # elapsed, energy is restored to full. Solution logic redacted for
        # showcase repo.
        pass

    def encontrar_item(self, arena: Arena):
        # Rolls for whether an item is found (probability scaled by luck),
        # then picks treasure vs. consumable (odds vary by arena type) and
        # instantiates a random item of that kind. Solution logic redacted
        # for showcase repo.
        pass

    @abstractmethod
    def gastar_energia(self):
        pass

    @abstractmethod
    def consumir(self):
        pass


class ExcavadorTareo(Excavador):

    def __init__(self, tuple: namedtuple):
        super().__init__(tuple)
        self.tipo = "tareo"

    def cavar(self, arena: Arena):
        # Digging-yield formula for this digger type (age/happiness/strength
        # vs. arena difficulty), then spends energy. Solution logic redacted
        # for showcase repo.
        pass

    def gastar_energia(self):
        # Per-dig energy cost formula for this digger type. Solution logic
        # redacted for showcase repo.
        pass

    def consumir(self, item: Consumible):
        # Applies a consumable's stat effects, type-specific tuning.
        # Solution logic redacted for showcase repo.
        pass


class ExcavadorDocencio(Excavador):
    def __init__(self, tuple: namedtuple):
        super().__init__(tuple)
        self.tipo = "docencio"

    def cavar(self, arena: Arena):
        # Digging-yield formula for this digger type, plus its own
        # happiness/strength side-effects. Solution logic redacted for
        # showcase repo.
        pass

    def gastar_energia(self):
        # Per-dig energy cost formula for this digger type. Solution logic
        # redacted for showcase repo.
        pass

    def consumir(self, item: Consumible):
        # Applies a consumable's stat effects, type-specific tuning.
        # Solution logic redacted for showcase repo.
        pass


class ExcavadorHibrido(ExcavadorDocencio, ExcavadorTareo):

    def __init__(self, tuple: namedtuple):
        super().__init__(tuple)
        self.tipo = "hibrido"

    def cavar(self, arena: Arena):
        metros_cavados = ExcavadorDocencio.cavar(self, arena)
        return metros_cavados

    def gastar_energia(self):
        # Blended energy-cost formula (averaging the two parent types),
        # with a minimum floor. Solution logic redacted for showcase repo.
        pass

    def consumir(self, item: Consumible):
        # Applies a consumable's stat effects, blending both parent types'
        # tuning with a minimum energy floor. Solution logic redacted for
        # showcase repo.
        pass
