import pandas as pd


import pandas as pd


def leer_excel(ruta):
    """
    Lee un archivo Excel y devuelve un DataFrame.
    """
    try:
        datos = pd.read_excel(ruta)
        return datos
    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None


def calcular_valor_total(df):
    """
    Calcula el valor total del inventario.

    Parámetros:
        df (DataFrame): Inventario.

    Retorna:
        float: Valor total del inventario.
    """
    total = (df["Cantidad"] * df["Precio"]).sum()
    return total


def productos_bajo_stock(df):
    """
    Devuelve los productos con menos de 10 unidades.

    Parámetros:
        df (DataFrame): Inventario.

    Retorna:
        DataFrame: Productos con bajo stock.
    """
    return df[df["Cantidad"] < 10]


def estadisticas_inventario(df):
    """
    Calcula estadísticas generales del inventario.

    Retorna:
        dict: Estadísticas del inventario.
    """
    estadisticas = {
        "total_productos": len(df),
        "valor_total": calcular_valor_total(df),
        "cantidad_total": df["Cantidad"].sum(),
        "precio_promedio": df["Precio"].mean()
    }

    return estadisticas


def generar_reporte(df):
    """
    Muestra un reporte completo del inventario.
    """

    estadisticas = estadisticas_inventario(df)

    print("=" * 50)
    print("        REPORTE DE INVENTARIO")
    print("=" * 50)

    print(f"Total de productos registrados : {estadisticas['total_productos']}")
    print(f"Cantidad total en inventario   : {estadisticas['cantidad_total']}")
    print(f"Valor total del inventario     : ${estadisticas['valor_total']:.2f}")
    print(f"Precio promedio                : ${estadisticas['precio_promedio']:.2f}")

    print("\nProductos con bajo stock (<10 unidades)\n")

    print(productos_bajo_stock(df))

    print("\nFin del reporte")