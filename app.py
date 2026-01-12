import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (BLINDADA E CLEAN)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok", page_icon="🥝", layout="wide")

# PALETA
COR_FUNDO = "#f4f8f0"
COR_TEXTO = "#1a3300"
COR_BOTAO = "#7cb342"
COR_BORDA = "#dcedc8"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700;900&display=swap');
    
    /* FONTES E CORES */
    h1, h2, h3, h4, h5, p, span, div, button, input, label, a {{
        font-family: 'Quicksand', sans-serif !important;
        color: {COR_TEXTO};
        line-height: 1.5;
        text-decoration: none !important;
    }}
    
    .stApp {{ background-color: {COR_FUNDO} !important; }}
    #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} header {{visibility: hidden;}}
    
    /* --- CABEÇALHO --- */
    .header-container {{ display: flex; align-items: center; padding-bottom: 10px; }}
    .header-icon {{ font-size: 40px; margin-right: 15px; }}
    .header-title {{ font-size: 26px; font-weight: 900; color: #33691e; margin: 0; }}
    
    /* --- BOTÃO FILTRO --- */
    .streamlit-expanderHeader {{
        background-color: {COR_BOTAO} !important;
        border-radius: 12px;
        padding: 15px 20px !important;
        margin-top: 20px !important;
        color: white !important;
        border: none !important;
    }}
    .streamlit-expanderHeader p {{ color: white !important; font-weight: 700 !important; }}
    .streamlit-expanderHeader svg {{ fill: white !important; }}
    
    /* --- BOTÕES DO STREAMLIT --- */
    .stButton > button {{
        background-color: {COR_BOTAO} !important;
        color: white !important;
        border: none;
        border-radius: 12px;
        font-weight: 800;
        padding: 15px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 0px #558b2f;
        transition: transform 0.1s;
    }}
    .stButton > button:active {{ transform: translateY(2px); box-shadow: 0 2px 0px #558b2f; }}
    
    /* --- CARD DE VÍDEO (ESTILO CARDÁPIO) --- */
    .video-card {{
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        border: 1px solid white;
    }}
    
    /* --- CAPA SIMULADA (O SEGREDO BLINDADO) --- */
    .fake-player {{
        background: linear-gradient(135deg, #e8f5e9 0%, #dcedc8 100%);
        height: 200px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 15px;
        border: 2px solid {COR_BORDA};
        cursor: pointer;
    }}
    .play-icon {{
        font-size: 50px;
        opacity: 0.8;
        transition: transform 0.2s;
    }}
    .fake-player:hover .play-icon {{ transform: scale(1.1); }}
    
    /* --- LINK BUTTON (CSS Customizado para links parecerem botões) --- */
    .custom-link-btn {{
        display: block;
        background-color: {COR_TEXTO}; /* Botão escuro para contraste */
        color: white !important;
        text-align: center;
        padding: 12px;
        border-radius: 10px;
        font-weight: 800;
        margin-top: 10px;
        box-shadow: 0 4px 0px #000;
    }}
    .custom-link-btn:active {{ transform: translateY(2px); box-shadow: 0 2px 0px #000; }}
    
    /* --- BADGE --- */
    .niche-badge {{
        background-color: white;
        color: {COR_BOTAO} !important;
        border: 2px solid {COR_BOTAO};
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 0.8em;
    }}
    
    /* --- INPUTS --- */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
        background-color: white !important;
        border: 2px solid {COR_BORDA} !important;
        color: {COR_TEXTO} !important;
        border-radius: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. LOGIN & ANIMAÇÃO
# ==============================================================================
def show_kiwi_animation():
    if st.session_state.get('animating', False):
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"<h2 style='text-align:center;'>Conectando...</h2>", unsafe_allow_html=True)
                components.html("""
                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                    <lottie-player src="https://lottie.host/8d061158-3655-4871-8985-898766792362/s2s1s8s6s7.json" background="transparent" speed="1" style="width: 250px; height: 250px; margin: auto;" autoplay></lottie-player>
                """, height=300)
        time.sleep(3.0)
        placeholder.empty()
        st.session_state['animating'] = False
        st.session_state['password_correct'] = True
        st.rerun()
        return True
    return False

def check_password():
    if st.session_state.get('password_correct', False): return True
    if st.session_state.get('animating', False): return False

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown(f"""
        <div style="background:white; padding:40px; border-radius:20px; text-align:center; border:1px solid {COR_BORDA}; margin-top:30px;">
            <div style="font-size:50px;">🥝</div>
            <h2 style="color:{COR_BOTAO}; margin:10px 0;">Kiwi Tok</h2>
            <p style="font-weight:700; color:#888;">Acesso Blindado</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        senha = st.text_input("Senha:", type="password", placeholder="kiwi2026")
        if st.button("ACESSAR SISTEMA"):
            if senha == "kiwi2026":
                st.session_state['animating'] = True
                st.rerun()
            else: st.error("Senha incorreta.")
    return False

if show_kiwi_animation(): st.stop()
if not check_password(): st.stop()

# ==============================================================================
# 3. DADOS
# ==============================================================================
@st.cache_data
def generate_data(country, qtd=1500):
    nichos_br = ["Marketing Digital", "Dropshipping", "Milhas Aéreas", "Investimentos", "Renda Extra", "Concursos", "Emagrecimento", "Treino em Casa", "Receitas Fit", "Nutrição", "Skincare", "Maquiagem", "Cabelo Cacheado", "Airfryer", "Churrasco", "Cerveja", "Pets", "Maternidade", "Viagem", "Fofoca", "BBB", "Sertanejo", "Funk", "Humor", "Podcast", "Futebol", "Games", "Free Fire", "Carros Rebaixados"]
    nichos_us = ["SaaS Growth", "AI Tools", "Crypto", "Real Estate", "Amazon FBA", "Remote Work", "Biohacking", "Keto Diet", "Pilates", "Mental Health", "Skincare ASMR", "Van Life", "Tiny Homes", "Tradwife", "Pottery", "Woodworking", "Gaming Setup", "True Crime", "Cleaning ASMR", "Streetwear", "Sneakers", "Pickleball"]
    lista = nichos_us if country == "US" else nichos_br
    # Links reais que abrem no app
    videos_pool = [
        "https://www.tiktok.com/@amazonhome/video/7298123456789012345", 
        "https://www.tiktok.com/@hudabeauty/video/7234567890123456789",
        "https://www.tiktok.com/@apple/video/7306076366050512174",
        "https://www.tiktok.com/@tiktok/video/7258384074697313562"
    ]
    data = []
    for i in range(qtd):
        n = random.choice(lista)
        item = {"id": i, "user": f"@{n.lower().replace(' ','')}_{random.randint(10,99)}", "niche": n, "url": random.choice(videos_pool), "views": f"{random.randint(10, 900)}K", "analise": f"🔥 Alta retenção: O hook visual acontece nos primeiros 2s."}
        data.append(item)
    return data

# ==============================================================================
# 4. INTERFACE PRINCIPAL
# ==============================================================================

# Cabeçalho
st.markdown(f"""
    <div class="header-container">
        <span class="header-icon">🥝</span>
        <h1 class="header-title">Radar de Tendências</h1>
    </div>
""", unsafe_allow_html=True)

# Filtro
with st.expander("⚙️ CLIQUE PARA FILTRAR (PAÍS & NICHO) 🔽", expanded=False):
    st.markdown("### 1. Região")
    region = st.radio("", ["🇺🇸 Estados Unidos", "🇧🇷 Brasil"], index=1, horizontal=True)
    country_code = "US" if "Estados Unidos" in region else "BR"
    
    db = generate_data(country_code, 2000)
    
    st.markdown("### 2. Nicho")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "✨ Ver Todos")
    filtro_cat = st.selectbox("", cats)

flag = "🇺🇸" if country_code == "US" else "🇧🇷"
st.markdown(f"<h3 style='margin: 20px 0; border-bottom: 2px solid {COR_BORDA}; padding-bottom: 10px;'>{flag} Feed de Resultados</h3>", unsafe_allow_html=True)

filtrado = db
if filtro_cat != "✨ Ver Todos":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]

# Loop de Cards Blindados
for v in filtrado[:10]:
    # O HTML abaixo cria o card visualmente
    st.markdown(f"""
    <div class="video-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <span style="font-weight:800; font-size:1.1em; color:#33691e;">{v['user']}</span>
            <span class="niche-badge">{v['niche']}</span>
        </div>
        
        <a href="{v['url']}" target="_blank" style="text-decoration:none;">
            <div class="fake-player">
                <div class="play-icon">▶️</div>
            </div>
        </a>
        
        <div style="background:#f9fbf7; padding:12px; border-radius:10px; border:1px solid {COR_BORDA}; margin-bottom:10px;">
            <p style="font-size:0.9em; font-weight:600; color:#555; margin:0;">💡 {v['analise']}</p>
        </div>
        
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
             <span style="font-weight:900; font-size:1.1em; color:{COR_TEXTO};">👁️ {v['views']}</span>
        </div>
        
        <a href="{v['url']}" target="_blank" class="custom-link-btn">
            ▶️ ASSISTIR NO TIKTOK
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"<center style='color:{COR_BOTAO}; font-weight:bold; margin-bottom:30px;'>Kiwi Tok v18.0 • Sistema Blindado</center>", unsafe_allow_html=True)
