import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (PASTEL LEGÍVEL)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok", page_icon="🥝", layout="wide")

# PALETA DE CORES (LINDA E LEGÍVEL)
COR_FUNDO = "#f4f8f0"       # Creme Esverdeado (Muito suave)
COR_TEXTO = "#1a3300"       # Verde Floresta Escuro (Contraste alto, mas elegante)
COR_DESTAQUE = "#558b2f"    # Verde Folha (Para títulos importantes)
COR_BOTAO = "#7cb342"       # Verde Kiwi (Vibrante)
COR_CARD = "#FFFFFF"        # Branco para os vídeos

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700;900&display=swap');
    
    /* RESET GERAL - FONTES E CORES */
    html, body, [class*="css"], p, div, span, label, h1, h2, h3, h4, h5, h6 {{
        font-family: 'Quicksand', sans-serif !important;
        color: {COR_TEXTO};
        line-height: 1.6; /* Aumentei para não encavalar */
    }}
    
    .stApp {{ background-color: {COR_FUNDO} !important; }}
    #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} header {{visibility: hidden;}}
    
    /* BOTÃO DE FILTRO (EXPANDER) - Ajustado para não encavalar */
    .streamlit-expanderHeader {{
        background-color: {COR_BOTAO} !important;
        color: white !important;
        border-radius: 12px;
        font-weight: 700;
        font-size: 18px !important;
        padding: 20px !important; /* Mais espaço */
        box-shadow: 0 4px 10px rgba(124, 179, 66, 0.3);
    }}
    .streamlit-expanderHeader p {{ color: white !important; }}
    
    /* BOTÕES NORMAIS */
    .stButton > button {{
        background-color: {COR_BOTAO} !important;
        color: white !important;
        border: none;
        border-radius: 15px;
        font-weight: 900;
        padding: 15px 20px;
        width: 100%;
        font-size: 16px;
        box-shadow: 0 4px 0px #558b2f; /* Efeito 3D sutil */
        transition: all 0.2s;
    }}
    .stButton > button:hover {{
        transform: translateY(2px);
        box-shadow: 0 2px 0px #558b2f;
    }}
    
    /* INPUTS E SELECTBOX (Claros e Legíveis) */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
        color: {COR_TEXTO} !important;
        background-color: white !important;
        border: 2px solid #dcedc8 !important;
        border-radius: 10px;
        font-weight: 700;
        height: 50px; /* Mais alto para facilitar o toque */
    }}
    
    /* LOGIN BOX */
    .login-box {{
        background: white;
        padding: 40px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(85, 139, 47, 0.1);
        border: 1px solid #dcedc8;
    }}
    
    /* CARD DE VÍDEO (Estilo Pinterest Clean) */
    .video-card {{
        background: {COR_CARD};
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        border: 1px solid #f1f8e9;
    }}
    
    /* BADGE DE NICHO (Corrigido para não ficar em cima do texto) */
    .niche-badge {{
        display: inline-block;
        background-color: {COR_BOTAO};
        color: white !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 0.85em;
        letter-spacing: 0.5px;
        white-space: nowrap; /* Impede quebra de linha */
    }}
    
    /* AJUSTES MOBILE */
    iframe {{ width: 100% !important; border-radius: 12px; }}
    
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. LOGIN COM ANIMAÇÃO
# ==============================================================================
def show_kiwi_animation():
    if st.session_state.get('animating', False):
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"<h2 style='text-align:center; color:{COR_DESTAQUE};'>Acessando Satélite...</h2>", unsafe_allow_html=True)
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

# Cabeçalho Limpo
c1, c2 = st.columns([1, 6])
with c1: st.markdown("<h1 style='margin:0;'>🥝</h1>", unsafe_allow_html=True)
with c2: st.markdown(f"<h1 style='margin:0; font-size:28px; padding-top:10px; color:{COR_DESTAQUE};'>Radar de Tendências</h1>", unsafe_allow_html=True)
st.write("") 

# BOTÃO DE FILTRO (Estilo Botão Verde Bonito)
with st.expander("⚙️ CLIQUE PARA FILTRAR (PAÍS & NICHO) 🔽", expanded=False):
    st.markdown("### 1. Selecione a Região")
    region = st.radio("", ["🇺🇸 Estados Unidos", "🇧🇷 Brasil"], index=1, horizontal=True)
    country_code = "US" if "Estados Unidos" in region else "BR"
    
    db = generate_data(country_code, 2000)
    
    st.markdown("### 2. Selecione o Nicho")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "✨ Ver Todos")
    filtro_cat = st.selectbox("", cats)

# FEED
flag = "🇺🇸" if country_code == "US" else "🇧🇷"
st.markdown(f"<h3 style='margin-top:20px; color:{COR_TEXTO}; border-bottom:2px solid #dcedc8; padding-bottom:10px;'>{flag} Resultados Encontrados</h3>", unsafe_allow_html=True)

filtrado = db
if filtro_cat != "✨ Ver Todos":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]

for v in filtrado[:10]:
    # Card Container
    st.markdown(f"""
    <div class="video-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <span style="font-weight:800; font-size:1.2em; color:{COR_DESTAQUE};">{v['user']}</span>
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
            <div style="background:#f1f8e9; padding:15px; border-radius:12px; border-left: 5px solid {COR_BOTAO};">
                <p style="margin:0; font-weight:bold; font-size:0.9em; text-transform:uppercase; color:{COR_BOTAO};">Análise Kiwi:</p>
                <p style="margin:5px 0 0 0; font-weight:600;">{v['analise']}</p>
            </div>
            <p style="font-weight:900; font-size:1.1em; margin-top:10px; text-align:right; color:{COR_DESTAQUE};">👁️ {v['views']} Views</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"<center style='color:{COR_BOTAO}; font-weight:bold;'>Kiwi Tok v14.0 • Design Pastel</center><br>", unsafe_allow_html=True)
