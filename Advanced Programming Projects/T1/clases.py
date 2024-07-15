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
        if self.tipo == "normal":
            dificultad = round(p.POND_ARENA_NORMAL*(round((self.rareza +
                                                           self.humedad +
                                                           self.dureza
                                                           + self.estatica) /
                                                          40, 2)), 2)
            return dificultad
        elif (self.tipo == "rocosa") or (self.tipo == "magnetica"):
            dificultad = round((self.rareza + self.humedad + self.dureza*2
                                                           + self.estatica) /
                               50, 2)
            return dificultad
        else:
            dificultad = round((self.rareza + self.humedad + self.dureza
                                                           + self.estatica) /
                               40, 2)
            return dificultad


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
        dias_descanso = int(self.edad/20)
        self.dias_descansando += 1
        if self.dias_descansando == dias_descanso:
            self.energia = 100
            self.dias_descansando = 0

    def encontrar_item(self, arena: Arena):
        probabilidad_item = (p.PROB_ENCONTRAR_ITEM)*(self.suerte/10)
        encontro_item = random.choices([True, False],
                                       weights=[probabilidad_item,
                                                1 - probabilidad_item], k=1)[0]
        if (arena.tipo == "mojada") or (arena.tipo == "magnetica"):
            tipo_item = random.choices(["tesoro", "consumibles"],
                                       weights=[0.5, 0.5], k=1)[0]
            if tipo_item == "tesoro":
                limite_s = len(f.info_tesoros) - 1
                tesoro = f.info_tesoros[random.randint(0, limite_s)]
                objeto_tesoro = f.instanciar_tesoro(tesoro)
                return objeto_tesoro
            else:
                limite_s = len(f.info_consumibles) - 1
                consumible = f.info_consumibles[random.randint(0, limite_s)]
                objeto_consumible = f.instanciar_consumible(consumible)
                return objeto_consumible
        else:
            if encontro_item is True:
                prob_consumible = p.PROB_ENCONTRAR_CONSUMIBLE
                tipo_item = random.choices(["tesoro", "consumible"],
                                           weights=[p.PROB_ENCONTRAR_TESORO,
                                                    prob_consumible],
                                           k=1)[0]
                if tipo_item == "tesoro":
                    limite_s = len(f.info_tesoros) - 1
                    tesoro = f.info_tesoros[random.randint(0, limite_s)]
                    objeto_tesoro = f.instanciar_tesoro(tesoro)
                    return objeto_tesoro
                else:
                    limite = len(f.info_consumibles) - 1
                    consumible = f.info_consumibles[random.randint(0, limite)]
                    objeto_consumible = f.instanciar_consumible(consumible)
                    return objeto_consumible
            else:
                return False

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
        metros_cavados = round(((30/self.edad)+(
            (self.felicidad+(2*self.fuerza))/10))*(
            1/(10*arena.dificultad_arena())), 2)
        self.gastar_energia()
        return metros_cavados

    def gastar_energia(self):
        energia_gastada = int((10/self.fuerza)+(self.edad/6))
        self.energia = self.energia - energia_gastada

    def consumir(self, item: Consumible):
        self.energia = self.energia + item.energia + p.ENERGIA_ADICIONAL_TAREO
        self.fuerza = self.fuerza + item.fuerza
        self.suerte = self.suerte + item.suerte + p.SUERTE_ADICIONAL_TAREO
        self.felicidad = (self.felicidad + item.felicidad
                          - p.FELICIDAD_PERDIDA_TAREO)
        self.edad = self.edad + p.EDAD_ADICIONAL_TAREO


class ExcavadorDocencio(Excavador):
    def __init__(self, tuple: namedtuple):
        super().__init__(tuple)
        self.tipo = "docencio"

    def cavar(self, arena: Arena):
        metros_cavados = round(((30/self.edad)+(
            (self.felicidad+(2*self.fuerza))/10))*(
            1/(10*arena.dificultad_arena())), 2)
        self.felicidad = self.felicidad + p.FELICIDAD_ADICIONAL_DOCENCIA
        self.fuerza = self.fuerza + p.FUERZA_ADICIONAL_DOCENCIA
        self.gastar_energia()
        return metros_cavados

    def gastar_energia(self):
        energia_gastada = int((10/self.fuerza)+(self.edad/6) +
                              p.ENERGIA_PERDIDA_DOCENCIA)
        self.energia = self.energia - energia_gastada

    def consumir(self, item: Consumible):
        self.energia = self.energia + item.energia
        self.fuerza = self.fuerza + item.fuerza
        self.suerte = self.suerte + item.suerte
        self.felicidad = self.felicidad + item.felicidad


class ExcavadorHibrido(ExcavadorDocencio, ExcavadorTareo):

    def __init__(self, tuple: namedtuple):
        super().__init__(tuple)
        self.tipo = "hibrido"

    def cavar(self, arena: Arena):
        metros_cavados = ExcavadorDocencio.cavar(self, arena)
        return metros_cavados

    def gastar_energia(self):
        energia_gastada = int(((10/self.fuerza)+(self.edad/6) +
                              p.ENERGIA_PERDIDA_DOCENCIA)/2)
        self.energia = self.energia - energia_gastada
        if self.energia < 20:
            self.energia = 20

    def consumir(self, item: Consumible):
        self.energia = self.energia + item.energia + p.ENERGIA_ADICIONAL_TAREO
        if self.energia < 20:
            self.energia = 20
        self.fuerza = self.fuerza + item.fuerza
        self.suerte = self.suerte + item.suerte + p.SUERTE_ADICIONAL_TAREO
        self.felicidad = (self.felicidad + item.felicidad
                          - p.FELICIDAD_PERDIDA_TAREO)
        self.edad = self.edad + p.EDAD_ADICIONAL_TAREO
