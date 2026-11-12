"""
==============================================================================
Módulo de Análisis de Elementos (Muros 3D, Vigas, Columnas y Losas)
==============================================================================
"""

import plotly.graph_objects as go


def calcular_muro_mamposteria(
    longitud: float,
    altura: float,
    espesor: float,
    niveles: int,
    peso_volumetrico: float
) -> dict:
    """Calcula área, volumen y peso propio de muros de mampostería por niveles."""
    area = longitud * altura
    vol = area * espesor
    peso_1 = vol * peso_volumetrico
    peso_tot = peso_1 * niveles
    return {
        "area": area,
        "vol": vol,
        "peso_1": peso_1,
        "peso_tot": peso_tot
    }


def generar_modelo_3d_muro(longitud: float, altura: float, espesor: float, niveles: int) -> go.Figure:
    """Construye una figura 3D interactiva en Plotly representando los niveles del muro."""
    fig = go.Figure()
    for n in range(niveles):
        z0 = n * altura
        z1 = (n + 1) * altura
        x = [0, longitud, longitud, 0, 0, longitud, longitud, 0]
        y = [0, 0, espesor, espesor, 0, 0, espesor, espesor]
        z = [z0, z0, z0, z0, z1, z1, z1, z1]

        fig.add_trace(go.Mesh3d(
            x=x,
            y=y,
            z=z,
            i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            opacity=0.85,
            color='#0284c7',
            name=f'Nivel {n + 1}'
        ))

    fig.update_layout(
        scene=dict(
            xaxis_title='Longitud (m)',
            yaxis_title='Espesor (m)',
            zaxis_title='Altura (m)',
            aspectmode='data'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=280
    )
    return fig


def calcular_viga(base: float, peralte: float, claro: float, cv_lineal: float) -> dict:
    """Calcula peso propio, carga total distribuida y momento máximo en viga."""
    cm = base * peralte * 2400.0
    w_total = cm + cv_lineal
    m_max = (w_total * (claro ** 2)) / 8.0
    return {"cm": cm, "w_total": w_total, "m_max": m_max}


def calcular_columna(lado_a: float, lado_b: float, altura: float, carga_trib: float) -> dict:
    """Calcula peso propio y carga axial total en columna de concreto."""
    peso_col = lado_a * lado_b * altura * 2400.0
    p_total = peso_col + carga_trib
    return {"peso_col": peso_col, "p_total": p_total}


def calcular_losa(espesor: float, lx: float, ly: float, cv_m2: float) -> dict:
    """Calcula carga muerta, carga total por m² y peso completo del tablero de losa."""
    cm = espesor * 2400.0 + 90.0
    w_m2 = cm + cv_m2
    peso_tablero = w_m2 * lx * ly
    return {"cm": cm, "w_m2": w_m2, "peso_tablero": peso_tablero}