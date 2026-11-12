"""
==============================================================================
Módulo de Cálculos Estructurales Básicos, por m² y Combinaciones LRFD
==============================================================================
"""


def calcular_cargas_basicas(cm: float, cv: float, longitud: float) -> dict:
    """Calcula carga total por m², carga lineal distribuida y carga puntual equivalente."""
    ct = cm + cv
    w = ct * longitud
    p_total = w * longitud
    p_kn = (p_total * 9.81) / 1000.0
    return {
        "ct": ct,
        "w": w,
        "p_total": p_total,
        "p_kn": p_kn
    }


def calcular_cargas_m2(
    espesor_cm: float,
    firme: float,
    acabado: float,
    instalaciones: float,
    cv: float
) -> dict:
    """Calcula el desglose de carga unitaria por metro cuadrado de losa."""
    peso_losa = (espesor_cm / 100.0) * 2400.0
    cm_total = peso_losa + firme + acabado + instalaciones
    total = cm_total + cv
    return {
        "peso_losa": peso_losa,
        "cm_total": cm_total,
        "total": total
    }


def calcular_combinacion_lrfd(f_cm: float, f_cv: float, cm: float, cv: float) -> dict:
    """Calcula la carga última factorizada mediante combinación gravitacional LRFD."""
    qu = (f_cm * cm) + (f_cv * cv)
    qu_kn = qu * 0.00981
    return {
        "qu": qu,
        "qu_kn": qu_kn
    }