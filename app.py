import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Una invitación especial...", page_icon="🗝️", layout="centered")

# Estilo visual estilo Coraline (Oscuro, azules, morados, amarillo neón y fuentes temáticas)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Henny+Penny&display=swap');
    
    .stApp {
        background-color: #0d1321;
        background-image: radial-gradient(circle, #1d2d44 0%, #0d1321 80%);
        color: #f0ebd8;
        font-family: 'Henny Penny', cursive;
    }
    h1, h2, h3, p {
        font-family: 'Henny Penny', cursive !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #3e5c76;
        color: #f2cc8f;
        border: 2px dashed #f2cc8f;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(242, 204, 143, 0.3);
        transition: 0.3s;
        width: 100%;
        font-size: 1.2rem;
        font-family: 'Henny Penny', cursive;
    }
    .stButton>button:hover {
        background-color: #f2cc8f;
        color: #0d1321;
        box-shadow: 0 0 20px #f2cc8f;
        border: 2px solid #0d1321;
    }
    .ticket {
        background: linear-gradient(135deg, #1d2d44 0%, #3e5c76 100%);
        padding: 30px;
        border: 3px dashed #f2cc8f;
        border-radius: 20px;
        text-align: center;
        color: #f0ebd8;
        box-shadow: 0 0 30px rgba(242, 204, 143, 0.5);
        margin-top: 20px;
    }
    .ticket h2 { color: #f2cc8f; font-size: 2.5rem; text-shadow: 2px 2px 4px #000; }
    .ticket h3 { color: #fff; margin: 5px 0; }
    .gif-container {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.5);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Variables de estado para guardar las decisiones (como un progreso de videojuego)
if 'nivel' not in st.session_state:
    st.session_state.nivel = 1
if 'dia' not in st.session_state:
    st.session_state.dia = ""
if 'lugar' not in st.session_state:
    st.session_state.lugar = ""
if 'hora' not in st.session_state:
    st.session_state.hora = ""

# Diccionario de cines y horarios
horarios_cine = {
    "Artz Pedregal Market": ["17:25 PM"],
    "Artz Pedregal Platino": ["15:20 PM", "20:20 PM"],
    "Cuicuilco": ["17:15 PM", "19:25 PM"],
    "Galerías Insurgentes Market": ["16:20 PM"],
    "Manacar": ["17:30 PM"]
}

dias_disponibles = [
    "Lunes 5 de Octubre", "Martes 6 de Octubre", "Miércoles 7 de Octubre", 
    "Jueves 8 de Octubre", "Viernes 9 de Octubre", "Sábado 10 de Octubre", 
    "Domingo 11 de Octubre", "Lunes 12 de Octubre"
]

# Funciones para avanzar de nivel
def avanzar(nivel):
    st.session_state.nivel = nivel

# NIVEL 1: El Saludo
if st.session_state.nivel == 1:
    st.markdown("<h1>🗝️ Un mensaje misterioso...</h1>", unsafe_allow_html=True)
    
    # INYECCIÓN DIRECTA DE HTML CON TRUCO PARA EVADIR EL BLOQUEO
    st.markdown("""
        <div class="gif-container">
            <img src="https://media.tenor.com/J3PnbDkK0W8AAAAC/coraline-tunnel.gif" width="100%" alt="Coraline Tunnel" referrerpolicy="no-referrer">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 1.5rem;'>Aloo, como tas?. Quería ver si querías ir a ver Coraline jijiji, te voy a dejar los días fechas y lugares donde la van a pasar 🧵🪡</p>", unsafe_allow_html=True)
    
    st.write("")
    if st.button("Continuar a la otra dimensión... 🚪"):
        avanzar(2)
# NIVEL 2: Escoger el Día
elif st.session_state.nivel == 2:
    st.markdown("<h1>🗓️ Nivel 1: Elige tu destino temporal</h1>", unsafe_allow_html=True)
    st.markdown("<p>¿Qué día quieres cruzar la puerta?</p>", unsafe_allow_html=True)
    
    dia_elegido = st.select_slider("", options=dias_disponibles)
    
    st.write("")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Atrás"): avanzar(1)
    with col2:
        if st.button("Fijar fecha 📌"):
            st.session_state.dia = dia_elegido
            avanzar(3)

# NIVEL 3: Escoger el Lugar
elif st.session_state.nivel == 3:
    st.markdown("<h1>📍 Nivel 2: Elige el terreno de juego</h1>", unsafe_allow_html=True)
    st.markdown("<p>¿En qué portal nos vemos?</p>", unsafe_allow_html=True)
    
    lugar_elegido = st.radio("Selecciona la ubicación:", list(horarios_cine.keys()), index=0)
    
    st.write("")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Atrás"): avanzar(2)
    with col2:
        if st.button("Fijar ubicación 🗺️"):
            st.session_state.lugar = lugar_elegido
            avanzar(4)

# NIVEL 4: Escoger la Hora
elif st.session_state.nivel == 4:
    st.markdown("<h1>⏱️ Nivel 3: El momento exacto</h1>", unsafe_allow_html=True)
    st.markdown(f"<p>Horarios para el portal en <b>{st.session_state.lugar}</b>:</p>", unsafe_allow_html=True)
    
    horarios_disponibles = horarios_cine[st.session_state.lugar]
    hora_elegida = st.radio("Selecciona la hora de función:", horarios_disponibles, index=0)
    
    st.write("")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Atrás"): avanzar(3)
    with col2:
        if st.button("Generar Llave (Boleto) 🗝"):
            st.session_state.hora = hora_elegida
            avanzar(5)

# NIVEL 5: El Comprobante (Boleto)
elif st.session_state.nivel == 5:
    st.balloons()
    st.markdown("<h1>¡Misión Completada! 🪡🐈‍⬛</h1>", unsafe_allow_html=True)
    st.markdown("<p>Tómale screenshot a este pase mágico para no olvidar los detalles.</p>", unsafe_allow_html=True)
    
    ticket_html = f"""
    <div class="ticket">
        <h2>🎟️ PASE A LA OTRA DIMENSIÓN 🎟️</h2>
        <hr style="border: 1px dashed #f2cc8f;">
        <h3>🎬 Película: CORALINE</h3>
        <h3>🗓️ Día: {st.session_state.dia}</h3>
        <h3>📍 Lugar: {st.session_state.lugar}</h3>
        <h3>⏱️ Hora: {st.session_state.hora}</h3>
        <hr style="border: 1px dashed #f2cc8f;">
        <p style="font-size: 1rem; color: #f2cc8f;">No olvides traer botones para los ojos...</p>
    </div>
    """
    st.markdown(ticket_html, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🔄 Volver a empezar por si te equivocaste"):
        avanzar(1)
