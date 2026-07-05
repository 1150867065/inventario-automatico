import pandas as pd

from src.inventario import calcular_valor_total
from src.inventario import productos_bajo_stock
from src.inventario import estadisticas_inventario


def crear_dataframe_prueba():
    """
    Crea un DataFrame de prueba para las pruebas unitarias.
    """
    datos = {
        "Producto": ["Mouse", "Teclado", "Monitor"],
        "Cantidad": [15, 8, 4],
        "Precio": [20, 35, 180]
    }

    return pd.DataFrame(datos)


def test_calcular_valor_total():
    df = crear_dataframe_prueba()

    resultado = calcular_valor_total(df)

    esperado = (15 * 20) + (8 * 35) + (4 * 180)

    assert resultado == esperado


def test_productos_bajo_stock():
    df = crear_dataframe_prueba()

    resultado = productos_bajo_stock(df)

    assert len(resultado) == 2

    assert "Teclado" in resultado["Producto"].values

    assert "Monitor" in resultado["Producto"].values


def test_estadisticas_inventario():
    df = crear_dataframe_prueba()

    estadisticas = estadisticas_inventario(df)

    assert estadisticas["total_productos"] == 3

    assert estadisticas["cantidad_total"] == 27

    assert estadisticas["valor_total"] == 1300

    assert round(estadisticas["precio_promedio"], 2) == 78.33