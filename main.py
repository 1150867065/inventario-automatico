from src.inventario import leer_excel
from src.inventario import generar_reporte

ruta = "datos/inventario.xlsx"

datos = leer_excel(ruta)

if datos is not None:
    generar_reporte(datos)