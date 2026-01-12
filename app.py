import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (CORREÇÃO DE FONTE E ÍCONES)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok", page_icon="🥝", layout="wide")

# PALETA DE CORES
COR_FUNDO = "#f4f8f0"
COR_TEXTO = "#1a3300"
COR_TEXTO_SECUNDARIO = "#33691e"
COR_BOTAO = "#7cb342"
COR_BORDA = "#dcedc8"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700;900&display=swap');
    
    /* --- CORREÇÃO DE FONTE CIRÚRGICA --- */
    /* Aplicamos a fonte bonita APENAS em elementos de texto, protegendo os ícones */
    h1, h2, h3, h4, h5, p, a, li, .stButton button, .stTextInput input, .stSelectbox, label {{
        font-family: 'Quicksand', sans-serif !important;
        color: {COR_TEXTO};
    }}
    
    .stApp {{ background-color: {COR_FUNDO} !important; }}
    #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} header {{visibility: hidden;}}
    
    /* --- CABEÇALHO --- */
    .header-container {{
        display: flex;
        align-items: center;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }}
    .header-icon {{ font-size: 45px; margin-right: 15px; }}
    .header-title {{ font-size: 28px; font-weight: 900; color: {COR_TEXTO_SECUNDARIO}; margin: 0; }}
    
    /* --- BOTÃO DE FILTRO (EXPANDER) CORRIGIDO --- */
    .streamlit-expanderHeader {{
        background-color: {COR_BOTAO} !important;
        border-radius: 12px;
        padding: 15px 20px !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 10px rgba(124, 179, 66, 0.2);
        border: none !important;
        color: white !important;
    }}
    
    /* Força o texto dentro do botão a ser Quicksand e Branco */
    .streamlit-expanderHeader p {{
        font-family: 'Quicksand', sans-serif !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }}
    
    /* --- ÍCONES DO EXPANDER (A CURA DO BUG) --- */
    /* Garante que o ícone da seta use a fonte original do sistema e não a Quicksand */
    .streamlit-expanderHeader svg {{
        fill: white !important; /* Deixa a setinha branca */
    }}
    
    /* --- BOTÕES GERAIS --- */
    .stButton > button {{
        background-color: {COR_BOTAO} !important;
        color: white !important;
        border: none;
        border-radius: 15px;
        font-weight: 900;
        padding: 15px;
        font-size: 16px;
        box-shadow: 0 4px 0px #558b2f;
        transition: transform 0.1s;
    }}
    .stButton > button:active {{ transform: translateY(2px); box-shadow: 0 2px 0px #558b2f; }}
    
    /* --- INPUTS --- */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
        background-color: white !important;
        border: 2px solid {COR_BORDA} !important;
        color: {COR_TEXTO} !important;
        border-radius: 10px;
        height: 50px;
    }}
    
    /* --- LOGIN --- */
    .login-box {{
        background: white;
        padding: 40px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(85, 139, 47, 0.1);
        border: 1px solid {COR_BORDA};
    }}
    
    /* --- CARD DE VÍDEO --- */
    .video-card {{
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.03);
        border: 1px solid white;
    }}
    
    /* --- BADGE DE NICHO (BRANCO) --- */
    .niche-badge {{
        display: inline-block;
        background-color: #FFFFFF;
        color: {COR_BOTAO} !important;
        border: 2px solid {COR_BOTAO};
        padding: 5px 14px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 0.85em;
        font-family: 'Quicksand', sans-serif !important;
        letter-spacing: 0.5px;
        white-space: nowrap;
    }}
    
    iframe {{ width: 100% !important; border-radius: 12px; }}
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
                st.markdown(f"<h2 style='text-align:center; color:{COR_TEXTO}; font-family:Quicksand, sans-serif;'>Acessando Satélite...</h2>", unsafe_allow_html=True)
                components.html("""
                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                    <lottie-player src="https://lottie.host/8d061158-3655-4871-8985-898766792362/s2s1s8s6s7.json" background="transparent" speed="1" style="width: 300px; height: 300px; margin: auto;" autoplay></lottie-player>
                """, height=350)
        time.sleep(3.5)
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
        st.markdown("""
        <div class="login-box">
            <h1 style='font-size: 50px; margin:0;'>🥝</h1>
            <h2 style='margin-top:10px; color:#558b2f;'>Kiwi Tok</h2>
            <p style='font-weight:600; color:#777;'>Inteligência Viral</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        senha = st.text_input("Senha de Acesso:", type="password", placeholder="kiwi2026")
        
        if st.button("✨ ENTRAR NO SISTEMA"):
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
    videos_pool = ["https://www.tiktok.com/@amazonhome/video/7298123456789012345", "https://www.tiktok.com/@hudabeauty/video/7234567890123456789", "https://www.tiktok.com/@apple/video/7306076366050512174", "https://www.tiktok.com/@tiktok/video/7258384074697313562", "https://www.tiktok.com/@khaby.lame/video/7258384074697313562"]
    data = []
    for i in range(qtd):
        n = random.choice(lista)
        item = {"id": i, "user": f"@{n.lower().replace(' ','')}_{random.randint(10,99)}", "niche": n, "url": random.choice(videos_pool), "views": f"{random.randint(10, 900)}K", "analise": f"Alta retenção detectada em {n}."}
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

# BOTÃO DE FILTRO (Com texto corrigido)
with st.expander("⚙️ CLIQUE PARA FILTRAR (PAÍS & NICHO) 🔽", expanded=False):
    st.markdown("### 1. Selecione a Região")
    region = st.radio("", ["🇺🇸 Estados Unidos", "🇧🇷 Brasil"], index=1, horizontal=True)
    country_code = "US" if "Estados Unidos" in region else "BR"
    
    db = generate_data(country_code, 2000)
    
    st.markdown("### 2. Selecione o Nicho")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "✨ Ver Todos")
    filtro_cat = st.selectbox("", cats)

# Subtítulo
flag = "🇺🇸" if country_code == "US" else "🇧🇷"
st.markdown(f"""
    <div style="margin-top: 20px; margin-bottom: 20px; border-bottom: 2px solid {COR_BORDA}; padding-bottom: 10px;">
        <h3 style="color:{COR_TEXTO}; font-weight: 800;">{flag} Feed de Resultados</h3>
    </div>
""", unsafe_allow_html=True)

filtrado = db
if filtro_cat != "✨ Ver Todos":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]

# Loop de Vídeos
for v in filtrado[:10]:
    st.markdown(f"""
    <div class="video-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <span style="font-weight:800; font-size:1.1em; color:{COR_TEXTO_SECUNDARIO};">{v['user']}</span>
            <span class="niche-badge">{v['niche']}</span>
        </div>
    """, unsafe_allow_html=True)
    
    try: vid_id = v['url'].split("/video/")[1].split("?")[0]
    except: vid_id = "7258384074697313562"
    
    components.html(f"""
        <style>body{{margin:0;padding:0;}}</style>
        <blockquote class="tiktok-embed" cite="{v['url']}" data-video-id="{vid_id}" style="max-width: 100%; min-width: 100%;" > 
        <section> <a target="_blank" href="{v['url']}">Ver no App</a> </section> </blockquote> 
        <script async src="https://www.tiktok.com/embed.js"></script>
    """, height=340)
    
    st.markdown(f"""
        <div style="margin-top:15px; color:{COR_TEXTO};">
            <div style="background:#f9fbf7; padding:15px; border-radius:12px; border: 1px solid {COR_BORDA};">
                <p style="margin:0; font-weight:bold; font-size:0.85em; text-transform:uppercase; color:{COR_BOTAO};">Análise Kiwi:</p>
                <p style="margin:5px 0 0 0; font-weight:600;">{v['analise']}</p>
            </div>
            <p style="font-weight:900; font-size:1.1em; margin-top:10px; text-align:right; color:{COR_TEXTO_SECUNDARIO};">👁️ {v['views']} Views</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"<center style='color:{COR_BOTAO}; font-weight:bold; margin-bottom:30px;'>Kiwi Tok v17.0 • Bug Fix</center>", unsafe_allow_html=True)
