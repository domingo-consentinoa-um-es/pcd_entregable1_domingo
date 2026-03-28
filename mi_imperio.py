# Entregable de Prácticas Domingo Consentino Asensio

from enum import Enum

class MiImperio:
    '''Esta es la clase controladora del sistema. Gestiona el catálogo de almacenes, 
    unidades de combate y coordina los procesos de login y adquisición/gestión de 
    repuestos'''

    def __init__(self):
        pass

class Almacen:
    '''Gestiona una lista de "Repuesto" y permite consultar stock, buscar piezas y 
    actualizar las cantidades de los repuestos'''

    def __init__(self):
        pass

class Repuesto:
    '''Almacena el nombre de la pieza, el proveedor, el precio y la cantidad disponible 
    en el respectivo almacén'''

    def __init__(self):
        pass

class UnidadDeCombate:
    '''Define los atributos de seguridad y autentificación, que son el tipo de unidad,
    ID de combate o la clave para transmisión cifrada'''

    def __init__(self):
        pass

class Nave(UnidadDeCombate):
    '''Subclase de UnidadDeCombate (Herencia), son las unidades de tipo Nave (espaciales). 
    Gestiona la lista de "Piezas" que definen que repuesto se requiere'''

    def __init__(self):
        super().__init__()

class EstacionEspacial(Nave):
    '''Subclase de Nave (Herencia), que guarda el número de tripulantes, el pasaje y 
    una enumeración de distintas localizaciones donde puede estar ubicada'''

    def __init__(self):
        super().__init__()

class Ubicacion(Enum):
    ENDOR = "Endor"
    CUMULO_RAIMOS = "Cúmulo Raimos"
    NEBULOSA_KALIIDA = "Nebulosa Kaliida"

class NaveEstelar(Nave):
    '''Subclase de Nave (Herencia), que guarda el número de tripulantes, el pasaje y una 
    enumeración con las clases de Naves Estelares'''

    def __init__(self):
        super().__init__()

class Clase(Enum):
    EJECUTOR = "Ejecutor"
    ECLIPSE = "Eclipse"
    SOBERANO = "Soberano"

class CazaEstelar(Nave):
    '''Subclase de Nave (Herencia), que guarda la dotación'''

    def __init__(self):
        super().__init__()

class Piezas:
    '''Representa el componente específico de una nave. Define el nombre de la pieza y su 
    cantidad necesaria'''

    def __init__(self):
        pass

## EXCEPCIONES ##
class ErrorMiImperio(Exception):
    '''De aquí salen todas las excepciones del proyecto'''
    pass