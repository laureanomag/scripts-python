import re
from datetime import datetime

# VALIDACIONES BÁSICAS
def es_dni(texto):
    # Verifica si tiene solo números y 7 u 8 dígitos
    return texto.isdigit() and len(texto) in [7, 8]


def es_email(texto):
    # Verifica formato básico de email
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, texto) is not None


def esta_en_rango(numero, minimo, maximo):
    # Verifica si está dentro del rango
    return minimo <= numero <= maximo


def es_entero(valor):
    # Intenta convertir a entero
    try:
        int(valor)
        return True
    except:
        return False


def es_float(valor):
    # Intenta convertir a decimal
    try:
        float(valor)
        return True
    except:
        return False


def es_numero(valor):
    # Es número si es entero o float
    return es_entero(valor) or es_float(valor)


def convertir_a_entero(valor):
    # Convierte a entero si se puede
    try:
        return int(valor)
    except:
        return None


def convertir_a_float(valor):
    # Convierte a float si se puede
    try:
        return float(valor)
    except:
        return None


def es_positivo(numero):
    # Verifica si es mayor que 0
    return numero > 0

# FECHAS Y HORAS

def es_hora_valida(texto):
    # Formato HH:MM
    try:
        datetime.strptime(texto, "%H:%M")
        return True
    except:
        return False


def es_fecha_hora_valida(texto, formato="%Y-%m-%d %H:%M"):
    # Verifica fecha + hora
    try:
        datetime.strptime(texto, formato)
        return True
    except:
        return False


def tiene_formato_fecha(texto, formato="%Y-%m-%d"):
    # Verifica solo fecha
    try:
        datetime.strptime(texto, formato)
        return True
    except:
        return False

# FUNCIONES EXTRA

def diferencia_dias(fecha1, fecha2):
    # Calcula diferencia entre fechas
    f1 = datetime.strptime(fecha1, "%Y-%m-%d")
    f2 = datetime.strptime(fecha2, "%Y-%m-%d")
    return abs((f2 - f1).days)


def obtener_timestamp():
    # Devuelve tiempo actual en segundos
    return datetime.now().timestamp()


def formatear_fecha(fecha, formato_salida="%d/%m/%Y"):
    # Cambia formato de fecha
    f = datetime.strptime(fecha, "%Y-%m-%d")
    return f.strftime(formato_salida)