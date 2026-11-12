"""
==============================================================================
Módulo de Ejercicios Resueltos y Pruebas de Validación
==============================================================================
"""

from calculos_basicos import calcular_cargas_basicas, calcular_combinacion_lrfd
from elementos_3d import calcular_muro_mamposteria

EJERCICIOS_RESUELTOS = {
    "Ejercicio 1: Muro de Mampostería Completo": {
        "planteamiento": (
            "Calcular el peso propio total de un muro de tabique rojo macizo "
            "(γ = 1500 kg/m³) de 5.0 m de longitud, 2.7 m de altura libre por nivel "
            "y 0.15 m de espesor en 2 niveles."
        ),
        "solucion": """
1. Área Frontal:
   A = 5.0 m × 2.7 m = 13.50 m²

2. Volumen de Mampostería:
   V = 13.50 m² × 0.15 m = 2.025 m³

3. Peso Propio por Nivel:
   W_1 = 2.025 m³ × 1500 kg/m³ = 3,037.5 kg

4. Carga Muerta Total (2 Niveles):
   W_tot = 3,037.5 kg × 2 = 6,075.0 kg (59.60 kN)
        """
    },
    "Ejercicio 2: Carga en Losa Maciza": {
        "planteamiento": (
            "Determinar la carga total de servicio por m² para una losa de 12 cm "
            "de espesor con acabados de 35 kg/m², firme de 40 kg/m² e instalaciones "
            "de 15 kg/m² para uso habitacional (CV = 170 kg/m²)."
        ),
        "solucion": """
1. Peso Propio Losa de Concreto:
   CM_losa = 0.12 m × 2400 kg/m³ = 288.0 kg/m²

2. Carga Muerta Total (CM):
   CM = 288.0 + 40 + 35 + 15 = 378.0 kg/m²

3. Carga Total de Servicio (CT):
   CT = CM + CV = 378.0 kg/m² + 170.0 kg/m² = 548.0 kg/m² (5.38 kN/m²)
        """
    },
    "Ejercicio 3: Carga Total en Viga Principal": {
        "planteamiento": (
            "Una viga de 25×50 cm soporta una carga viva de 300 kg/m sobre un claro "
            "de 6.0 metros. Calcular la carga uniformemente distribuida total (w)."
        ),
        "solucion": """
1. Peso Propio Viga de Concreto:
   CM_viga = 0.25 m × 0.50 m × 2400 kg/m³ = 300.0 kg/m

2. Carga Total Distribuida (w):
   w = CM + CV = 300.0 kg/m + 300.0 kg/m = 600.0 kg/m

3. Carga Puntual Equivalente (P):
   P = w × L = 600.0 kg/m × 6.0 m = 3,600.0 kg (35.32 kN)
        """
    }
}


def ejecutar_pruebas_unitarias() -> list:
    """Ejecuta casos de prueba con valores controlados para validar las funciones."""
    res_basico = calcular_cargas_basicas(250, 170, 6.0)
    prueba_1 = (res_basico["ct"] == 420.0 and res_basico["w"] == 2520.0)

    res_muro = calcular_muro_mamposteria(5.0, 2.7, 0.15, 2, 1500)
    prueba_2 = (round(res_muro["peso_tot"], 1) == 6075.0)

    res_comb = calcular_combinacion_lrfd(1.3, 1.5, 378.0, 170.0)
    prueba_3 = (round(res_comb["qu"], 1) == 746.4)

    return [
        ("Prueba 1: Cargas Estructurales Básicas", prueba_1),
        ("Prueba 2: Modelado de Muros de Mampostería", prueba_2),
        ("Prueba 3: Combinación de Cargas LRFD", prueba_3)
    ]