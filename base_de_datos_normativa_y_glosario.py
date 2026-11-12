"""
==============================================================================
Módulo de Datos Normativos, Geolocalización y Conceptos Básicos
==============================================================================
"""

BASE_NORMATIVA = {
    "Campeche": {
        "norma": "Reglamento de Construcciones del Estado de Campeche / NTC",
        "municipios": {
            "Campeche (Capital)": {
                "zona": "B1",
                "c": 0.12,
                "viento": 160,
                "desc": "Zona costera con sismicidad baja-moderada e impacto de vientos huracanados."
            },
            "Carmen (Ciudad del Carmen)": {
                "zona": "B2",
                "c": 0.14,
                "viento": 180,
                "desc": "Alta exposición a vientos francos del Golfo de México e influencia marina."
            },
            "Champotón": {
                "zona": "B1",
                "c": 0.12,
                "viento": 160,
                "desc": "Zona costera con vientos de diseño regionales según MDOC-CFE."
            },
            "Escárcega": {
                "zona": "A",
                "c": 0.08,
                "viento": 140,
                "desc": "Zona continental interior de Campeche, sismicidad baja."
            },
            "Calakmul": {
                "zona": "A",
                "c": 0.08,
                "viento": 130,
                "desc": "Zona continental de baja sismicidad y vientos moderados."
            }
        }
    },
    "Ciudad de México (CDMX)": {
        "norma": "Normas Técnicas Complementarias NTC-CDMX 2023",
        "municipios": {
            "Alcaldía Cuauhtémoc (Zona III Lago)": {
                "zona": "III (Lago)",
                "c": 0.45,
                "viento": 75,
                "desc": "Arcillas blandas de alta compresibilidad. Alta amplificación sísmica."
            },
            "Alcaldía Coyoacán (Zona II Transición)": {
                "zona": "II (Transición)",
                "c": 0.32,
                "viento": 75,
                "desc": "Intercalación de estratos arcillosos y depósitos firmes."
            },
            "Alcaldía Tlalpan (Zona I Lomas)": {
                "zona": "I (Lomas)",
                "c": 0.16,
                "viento": 75,
                "desc": "Terreno firme de roca o tepetate con baja amplificación sísmica."
            }
        }
    },
    "Jalisco": {
        "norma": "Reglamento Estatal de Jalisco / ACI 318",
        "municipios": {
            "Guadalajara": {
                "zona": "C",
                "c": 0.30,
                "viento": 120,
                "desc": "Zona de sismicidad alta por subducción del Pacífico."
            },
            "Puerto Vallarta": {
                "zona": "D",
                "c": 0.40,
                "viento": 190,
                "desc": "Zona costera de muy alta sismicidad y exposición a huracanes."
            }
        }
    },
    "Nuevo León": {
        "norma": "Reglamento de Construcción de Monterrey / MDOC-CFE",
        "municipios": {
            "Monterrey": {
                "zona": "A",
                "c": 0.06,
                "viento": 130,
                "desc": "Sismicidad muy baja, diseño dominado por ráfagas de viento."
            },
            "San Pedro Garza García": {
                "zona": "A",
                "c": 0.06,
                "viento": 130,
                "desc": "Zona sísmica baja con requerimientos de viento en laderas."
            }
        }
    },
    "Yucatán": {
        "norma": "Reglamento de Construcciones de Mérida / MDOC-CFE",
        "municipios": {
            "Mérida": {
                "zona": "A",
                "c": 0.05,
                "viento": 160,
                "desc": "Baja sismicidad, dominada por efectos de viento huracanado."
            },
            "Progreso": {
                "zona": "A",
                "c": 0.05,
                "viento": 190,
                "desc": "Exposición costera directa a ráfagas de viento huracanado."
            }
        }
    },
    "Oaxaca": {
        "norma": "Reglamento de Construcciones para Oaxaca / NTC",
        "municipios": {
            "Oaxaca de Juárez": {
                "zona": "D",
                "c": 0.48,
                "viento": 110,
                "desc": "Zona de altísima sismicidad debido a la brecha de subducción."
            },
            "Salina Cruz": {
                "zona": "D",
                "c": 0.50,
                "viento": 180,
                "desc": "Combinación de altísima sismicidad y vientos dominantes del Istmo."
            }
        }
    },
    "Veracruz": {
        "norma": "Reglamento del Estado de Veracruz / CFE",
        "municipios": {
            "Veracruz (Puerto)": {
                "zona": "B",
                "c": 0.18,
                "viento": 180,
                "desc": "Zona expuesta a vientos del Norte e impacto de tormentas."
            },
            "Xalapa": {
                "zona": "B",
                "c": 0.16,
                "viento": 140,
                "desc": "Zona montañosa de sismicidad moderada."
            }
        }
    }
}

PESOS_VOLUMETRICOS = {
    "Material": [
        "Concreto Armado",
        "Concreto Simple",
        "Tabique Rojo Macizo",
        "Bloque Hueco de Concreto",
        "Mortero Cemento-Arena",
        "Acero Estructural"
    ],
    "Peso Volumétrico (kg/m³)": [2400, 2200, 1500, 1200, 2100, 7850],
    "Peso Volumétrico (kN/m³)": [23.54, 21.58, 14.71, 11.77, 20.60, 77.00]
}

CONCEPTOS_GLOSARIO = [
    ("Estructura", "Ensamblaje de elementos interconectados diseñado para soportar y transmitir cargas."),
    ("Carga Estructural", "Fuerzas o acciones externas e internas actuantes sobre la edificación."),
    ("Elementos Estructurales", "Componentes como vigas, columnas, muros, losas y zapatas."),
    ("Transmisión de Cargas", "Trayectoria que recorre el peso desde la losa hasta la cimentación."),
    ("Deformación", "Cambio de forma o tamaño que experimenta un cuerpo por cargas aplicadas."),
    ("Esfuerzo", "Intensidad de la fuerza interna por unidad de área (σ = P/A, τ = V/A)."),
    ("Tipos de Cargas Estructurales", "Clasificación en Cargas Muertas, Cargas Vivas y Accidentales."),
    ("Carga Concentrada", "Fuerza aplicada en un área puntual reducida (fuerza puntual P)."),
    ("Carga Distribuida", "Carga repartida continua sobre una longitud (kg/m) o área (kg/m²)."),
    ("Flexión", "Efecto generado por momentos flectores que produce compresión y tensión."),
    ("Compresión", "Esfuerzo interno axial que tiende a acortar o aplastar un elemento."),
    ("Tensión / Tracción", "Esfuerzo interno axial que tiende a estirar o alargar un elemento."),
    ("Cortante", "Fuerza transversal que intenta deslizar una sección respecto a otra."),
    ("Torsión", "Momento que tiende a retorcer un elemento alrededor de su eje longitudinal."),
    ("Capacidad de Carga", "Magnitud máxima de carga que un elemento soporta antes de fallar."),
    ("Factor de Seguridad", "Relación entre la resistencia real del elemento y la carga esperada.")
]