# ==============================================================================
# ESTRUCTURAS | Análisis de Cargas - Ingeniería Civil (Archivo Principal)
# Ejecución en terminal: streamlit run app.py
# ==============================================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from datos_normativos import BASE_NORMATIVA, CONCEPTOS_GLOSARIO, PESOS_VOLUMETRICOS
from calculos_basicos import (
    calcular_cargas_basicas,
    calcular_cargas_m2,
    calcular_combinacion_lrfd
)
from elementos_3d import (
    calcular_muro_mamposteria,
    generar_modelo_3d_muro,
    calcular_viga,
    calcular_columna,
    calcular_losa
)
from pruebas import EJERCICIOS_RESUELTOS, ejecutar_pruebas_unitarias

st.set_page_config(
    page_title="ESTRUCTURAS | Análisis de Cargas",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0284c7 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .hero-title { font-size: 2.3rem; font-weight: 800; margin: 0; color: #ffffff; }
    .hero-subtitle { font-size: 1.25rem; color: #7dd3fc; font-weight: 600; margin: 0.2rem 0 0.8rem 0; }
    .calc-step {
        background-color: #ffffff;
        border-left: 4px solid #0284c7;
        padding: 1rem;
        margin-bottom: 0.75rem;
        border-radius: 0 0.5rem 0.5rem 0;
        border: 1px solid #e2e8f0;
        border-left-width: 4px;
    }
    .calc-formula {
        font-family: 'Courier New', Courier, monospace;
        color: #0369a1;
        font-weight: 700;
        background-color: #e0f2fe;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        display: inline-block;
        margin: 0.35rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Navegación Principal")
menu_opcion = st.sidebar.radio(
    "Ir al módulo:",
    [
        "📌 Inicio & Presentación",
        "📚 Conceptos Básicos",
        "🌐 Geolocalización y Normativa",
        "🧮 Cargas Estructurales Básicas",
        "🧱 Muros de Mampostería (3D)",
        "📦 Vigas, Columnas y Losas",
        "📐 Cargas por Metro Cuadrado (m²)",
        "🔀 Combinación de Cargas",
        "✍️ Ejercicios y Pruebas"
    ]
)

st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">ESTRUCTURAS | Análisis de Cargas</h1>
        <div class="hero-subtitle">Ingeniería Civil</div>
        <p style="margin: 0; color: #e0f2fe; font-size: 0.95rem;">
            Plataforma Profesional de Cálculo, Simulación e Interpretación Estructural
        </p>
    </div>
""", unsafe_allow_html=True)

if menu_opcion == "📌 Inicio & Presentación":
    st.header("Importancia del Análisis de Cargas Estructurales")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.write("""
        Toda construcción está sometida a diferentes tipos de cargas, como el peso de sus propios materiales,
        las personas, los muebles, los equipos y las acciones ambientales, entre ellas el viento y los sismos.
        Estas fuerzas pueden afectar el comportamiento de una estructura y, si no se consideran adecuadamente
        durante su diseño, pueden provocar deformaciones excesivas, daños o fallas estructurales.

        Por esta razón, es necesario realizar un análisis que permita identificar las cargas, calcular sus
        magnitudes, establecer sus combinaciones y evaluar sus efectos sobre los elementos que conforman una
        edificación.
        """)
        st.info("Seleccione cualquiera de los módulos en el menú lateral para realizar cálculos dinámicos.")
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?q=80&w=800&auto=format&fit=crop",
            caption="Estructura de Edificación - Análisis y Diseño",
            use_container_width=True
        )

elif menu_opcion == "📚 Conceptos Básicos":
    st.header("Conceptos Básicos de Análisis Estructural")
    st.caption("Glosario completo con las 16 definiciones fundamentales del análisis de cargas.")
    cols = st.columns(2)
    for idx, (titulo, desc) in enumerate(CONCEPTOS_GLOSARIO):
        with cols[idx % 2]:
            st.markdown(f"""
                <div style="background-color: white; padding: 1rem; border-radius: 0.5rem;
                            border: 1px solid #e2e8f0; margin-bottom: 0.75rem;">
                    <h4 style="margin: 0; color: #0284c7; font-size: 0.95rem;">{idx + 1}. {titulo}</h4>
                    <p style="margin-top: 0.4rem; margin-bottom: 0; color: #475569; font-size: 0.85rem;">
                        {desc}
                    </p>
                </div>
            """, unsafe_allow_html=True)

elif menu_opcion == "🌐 Geolocalización y Normativa":
    st.header("Geolocalización, Zonificación y Normativa Regional")
    c1, c2, c3 = st.columns(3)
    with c1:
        estado_sel = st.selectbox("Estado / Entidad Federativa", list(BASE_NORMATIVA.keys()))
    with c2:
        municipios_list = list(BASE_NORMATIVA[estado_sel]["municipios"].keys())
        mun_sel = st.selectbox("Municipio / Alcaldía", municipios_list)
    with c3:
        uso_edif = st.selectbox(
            "Uso de Edificación",
            ["Grupo B: Habitacional / Comercial", "Grupo A: Estructura Esencial (Hospitales, Escuelas)"]
        )

    data_mun = BASE_NORMATIVA[estado_sel]["municipios"][mun_sel]
    norma_nom = BASE_NORMATIVA[estado_sel]["norma"]
    factor_imp = 1.5 if "Grupo A" in uso_edif else 1.0
    c_diseno = round(data_mun["c"] * factor_imp, 3)

    mc1, mc2, mc3, mc4 = st.columns(4)
    mc1.metric("Norma Aplicable", norma_nom.split('/')[0])
    mc2.metric("Coeficiente Sísmico (c)", f"{c_diseno}")
    mc3.metric("Velocidad de Viento (V_r)", f"{data_mun['viento']} km/h")
    mc4.metric("Factor Grupo (Uso)", f"F_imp = {factor_imp}")
    st.success(f"**Criterio Técnico:** {data_mun['desc']}")

    st.markdown("---")
    st.subheader("Pesos Volumétricos Normativos (γ)")
    st.dataframe(pd.DataFrame(PESOS_VOLUMETRICOS), use_container_width=True)

elif menu_opcion == "🧮 Cargas Estructurales Básicas":
    st.header("Cargas Estructurales Básicas")
    col_in, col_out = st.columns([1, 1.2])
    with col_in:
        cm = st.number_input("Carga Muerta (CM) [kg/m²]", min_value=0.1, value=250.0, step=10.0)
        cv = st.number_input("Carga Viva (CV) [kg/m²]", min_value=0.1, value=170.0, step=10.0)
        L = st.number_input("Longitud Tributaria / Claro (L) [m]", min_value=0.1, value=6.0, step=0.5)

    res = calcular_cargas_basicas(cm, cv, L)
    with col_out:
        r1, r2, r3 = st.columns(3)
        r1.metric("Carga Total (CT)", f"{res['ct']:.1f} kg/m²")
        r2.metric("Carga Lineal (w)", f"{res['w']:.1f} kg/m")
        r3.metric("Puntual Eq. (P)", f"{res['p_kn']:.2f} kN")

        st.markdown(f"""
        <div class="calc-step">
            <strong>1. Carga Total (CT):</strong> <span class="calc-formula">CT = CM + CV</span> =
            <strong>{res['ct']:.1f} kg/m²</strong>
        </div>
        <div class="calc-step">
            <strong>2. Carga Lineal (w):</strong> <span class="calc-formula">w = CT × L</span> =
            <strong>{res['w']:.1f} kg/m</strong>
        </div>
        <div class="calc-step">
            <strong>3. Carga Puntual (P):</strong> <span class="calc-formula">P = w × L</span> =
            {res['p_total']:.1f} kg ≈ <strong>{res['p_kn']:.2f} kN</strong>
        </div>
        """, unsafe_allow_html=True)

elif menu_opcion == "🧱 Muros de Mampostería (3D)":
    st.header("Análisis de Muros de Mampostería")
    col_in, col_out = st.columns([1, 1.2])
    with col_in:
        L = st.number_input("Longitud del muro (L) [m]", min_value=0.1, value=5.0, step=0.5)
        H = st.number_input("Altura libre por nivel (H) [m]", min_value=0.1, value=2.7, step=0.1)
        e = st.number_input("Espesor del muro (e) [m]", min_value=0.05, value=0.15, step=0.01)
        niveles = st.number_input("Número de niveles del edificio", min_value=1, value=2, step=1)
        tipo_mamp = st.selectbox(
            "Tipo de Mampostería",
            [
                "Tabique Rojo Macizo (1,500 kg/m³)",
                "Bloque Hueco de Concreto (1,200 kg/m³)",
                "Tabicon Pesado de Concreto (1,800 kg/m³)"
            ]
        )
        pv_val = 1500 if "Rojo" in tipo_mamp else (1200 if "Hueco" in tipo_mamp else 1800)
        fm = st.number_input("Resistencia a compresión f'm [kg/cm²]", min_value=10, value=50, step=5)

    res_m = calcular_muro_mamposteria(L, H, e, niveles, pv_val)
    with col_out:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Área", f"{res_m['area']:.2f} m²")
        m2.metric("Volumen", f"{res_m['vol']:.3f} m³")
        m3.metric("Peso Nivel 1", f"{res_m['peso_1']:,.1f} kg")
        m4.metric("Carga Total", f"{res_m['peso_tot']:,.1f} kg")
        fig = generar_modelo_3d_muro(L, H, e, int(niveles))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    <div class="calc-step">
        1. <strong>Área:</strong> {res_m['area']:.2f} m² |
        2. <strong>Volumen:</strong> {res_m['vol']:.3f} m³ |
        3. <strong>Peso/Nivel:</strong> {res_m['peso_1']:,.1f} kg |
        4. <strong>Total ({niveles} niveles):</strong> {res_m['peso_tot']:,.1f} kg (f'm = {fm} kg/cm²)
    </div>
    """, unsafe_allow_html=True)

elif menu_opcion == "📦 Vigas, Columnas y Losas":
    st.header("Análisis de Elementos Estructurales Individuales")
    elem_tipo = st.radio(
        "Seleccione tipo de elemento:",
        ["Viga de Concreto Armado", "Columna de Concreto", "Losa Maciza"],
        horizontal=True
    )

    if elem_tipo == "Viga de Concreto Armado":
        c1, c2 = st.columns(2)
        with c1:
            b = st.number_input("Base b [m]", value=0.25, step=0.05)
            h = st.number_input("Peralte h [m]", value=0.50, step=0.05)
            L = st.number_input("Claro de Viga L [m]", value=6.0, step=0.5)
            cv_lineal = st.number_input("Carga Viva Lineal [kg/m]", value=300.0, step=50.0)
        rv = calcular_viga(b, h, L, cv_lineal)
        with c2:
            st.metric("Peso Propio (CM)", f"{rv['cm']:.1f} kg/m")
            st.metric("Carga Total (w)", f"{rv['w_total']:.1f} kg/m")
            st.metric("Momento Máximo (M_max)", f"{rv['m_max']:,.1f} kg·m")
            fig, ax = plt.subplots(figsize=(5, 2.2))
            ax.bar(["Carga Muerta", "Carga Viva"], [rv['cm'], cv_lineal], color=["#0284c7", "#7dd3fc"])
            st.pyplot(fig)

    elif elem_tipo == "Columna de Concreto":
        c1, c2 = st.columns(2)
        with c1:
            a = st.number_input("Lado A [m]", value=0.40, step=0.05)
            b = st.number_input("Lado B [m]", value=0.40, step=0.05)
            H = st.number_input("Altura Columna H [m]", value=3.5, step=0.5)
            p_trib = st.number_input("Carga Tributaria Superior [kg]", value=12000.0, step=1000.0)
        rc = calcular_columna(a, b, H, p_trib)
        with c2:
            st.metric("Peso Columna (CM)", f"{rc['peso_col']:.1f} kg")
            st.metric("Carga Axial Total (P_u)", f"{rc['p_total']:,.1f} kg")

    else:
        c1, c2 = st.columns(2)
        with c1:
            e_losa = st.number_input("Espesor de losa [m]", value=0.12, step=0.01)
            lx = st.number_input("Largo Lx [m]", value=4.0, step=0.5)
            ly = st.number_input("Ancho Ly [m]", value=5.0, step=0.5)
            cv_m2 = st.number_input("Carga Viva [kg/m²]", value=170.0, step=10.0)
        rl = calcular_losa(e_losa, lx, ly, cv_m2)
        with c2:
            st.metric("Carga Muerta (CM)", f"{rl['cm']:.1f} kg/m²")
            st.metric("Carga Total (w)", f"{rl['w_m2']:.1f} kg/m²")
            st.metric("Peso Tablero Completo", f"{rl['peso_tablero']:,.1f} kg")

elif menu_opcion == "📐 Cargas por Metro Cuadrado (m²)":
    st.header("Análisis de Cargas Unitario por Metro Cuadrado (w/m²)")
    col_in, col_chart = st.columns([1, 1.2])
    with col_in:
        h_cm = st.number_input("Espesor de losa de concreto [cm]", value=12.0, step=1.0)
        firme = st.number_input("Firme y mortero [kg/m²]", value=40.0, step=5.0)
        acabado = st.number_input("Acabados [kg/m²]", value=35.0, step=5.0)
        inst = st.number_input("Instalaciones [kg/m²]", value=15.0, step=5.0)
        cv_reg = st.number_input("Carga Viva Reglamentaria [kg/m²]", value=170.0, step=10.0)

    rm2 = calcular_cargas_m2(h_cm, firme, acabado, inst, cv_reg)
    with col_chart:
        st.metric("CARGA TOTAL RESULTANTE", f"{rm2['total']:.1f} kg/m²")
        labels = ['Losa Concreto', 'Firme Mortero', 'Acabados', 'Instalaciones', 'Carga Viva']
        sizes = [rm2['peso_losa'], firme, acabado, inst, cv_reg]
        fig, ax = plt.subplots(figsize=(5, 3.8))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4))
        st.pyplot(fig)

elif menu_opcion == "🔀 Combinación de Cargas":
    st.header("Combinación de Cargas Factorizadas (LRFD / NTC)")
    col1, col2 = st.columns(2)
    with col1:
        f_cm = st.number_input("Factor Carga Muerta (γ_D)", value=1.3, step=0.1)
        f_cv = st.number_input("Factor Carga Viva (γ_L)", value=1.5, step=0.1)
        cm_val = st.number_input("Carga Muerta Nominal (CM) [kg/m²]", value=378.0)
        cv_val = st.number_input("Carga Viva Nominal (CV) [kg/m²]", value=170.0)

    r_comb = calcular_combinacion_lrfd(f_cm, f_cv, cm_val, cv_val)
    with col2:
        st.metric("Carga Factorizada Última (Qu)", f"{r_comb['qu']:.1f} kg/m²", f"{r_comb['qu_kn']:.2f} kN/m²")
        st.markdown(f"""
        <div class="calc-step">
            <span class="calc-formula">Qu = γ_D · CM + γ_L · CV</span><br>
            Qu = ({f_cm} × {cm_val}) + ({f_cv} × {cv_val}) = <strong>{r_comb['qu']:.1f} kg/m²</strong>
        </div>
        """, unsafe_allow_html=True)

elif menu_opcion == "✍️ Ejercicios y Pruebas":
    st.header("Ejercicios Resueltos y Validación del Modelo")
    ex_sel = st.selectbox("Seleccione Ejercicio a Revisar:", list(EJERCICIOS_RESUELTOS.keys()))
    ex_data = EJERCICIOS_RESUELTOS[ex_sel]
    st.write(f"**Planteamiento:** {ex_data['planteamiento']}")
    st.code(ex_data["solucion"], language="markdown")

    if st.button("Ejecutar Pruebas Automáticas de Validación"):
        resultados_test = ejecutar_pruebas_unitarias()
        for nombre_prueba, ok in resultados_test:
            if ok:
                st.success(f"✔ {nombre_prueba}: VALIDADO CORRECTAMENTE")