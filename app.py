import streamlit as st
import streamlit.components.v1 as components
import random

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (ULTRA LEGÍVEL - PRETO NO BRANCO)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok", page_icon="🥝", layout="wide")

# CSS BRUTO PARA FORÇAR PRETO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');
    
    /* FORÇAR TUDO A SER PRETO E LEGÍVEL */
    html, body, [class*="css"], p, div, span, label, h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif !important;
        color: #000000 !important; /* Preto Puro */
        line-height: 1.5;
    }
    
    /* Fundo Branco Puro */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Esconde menu padrão */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* BOTÃO DE FILTRO (EXPANDER) */
    .streamlit-expanderHeader {
        background-color: #000000 !important; /* Fundo Preto */
        color: #FFFFFF !important; /* Texto Branco */
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px !important;
    }
    .streamlit-expanderHeader p {
        color: #FFFFFF !important; /* Garante que o texto dentro seja branco */
    }
    
    /* BOTÕES NORMAIS */
    .stButton > button {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: 2px solid #000000;
        border-radius: 10px;
        font-weight: bold;
        padding: 15px 20px;
        width: 100%;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #333333 !important;
        color: #FFF !important;
    }
    
    /* Inputs e Selectbox (Garante texto preto dentro) */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        color: #000000 !important;
        background-color: #F0F0F0 !important;
        border: 1px solid #000000 !important;
        font-weight: 600;
    }
    
    /* LOGIN CONTAINER */
    .login-box {
        border: 2px solid #000000;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        background: #FAFAFA;
        margin-top: 20px;
    }
    
    /* CARD DE VÍDEO (Borda Preta Definida) */
    .video-card {
        background: #FFFFFF;
        border: 2px solid #000000; /* Borda preta forte */
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 25px;
        box-shadow: 4px 4px 0px #000000; /* Sombra sólida estilo Retrô/Pop */
    }
    
    /* BADGE DE NICHO */
    .niche-badge {
        background-color: #000000;
        color: #FFFFFF !important;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.8em;
    }
    
    /* Ajuste de Iframe */
    iframe { width: 100% !important; }
    
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. LOGIN ALTO CONTRASTE
# ==============================================================================
def check_password():
    if st.session_state.get('password_correct', False): return True
    
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("""
        <div class="login-box">
            <h1 style='font-size: 40px; margin:0;'>🥝</h1>
            <h2 style='margin-top:0;'>KIWI TOK</h2>
            <p style='font-weight:bold;'>Área Restrita</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Digite a Senha:**")
        senha = st.text_input("", type="password", placeholder="kiwi2026", label_visibility="collapsed")
        
        if st.button("ENTRAR AGORA"):
            if senha == "kiwi2026":
                st.session_state['password_correct'] = True
                st.rerun()
            else: st.error("SENHA INCORRETA.")
    return False

if not check_password(): st.stop()

# ==============================================================================
# 3. DADOS
# ==============================================================================
@st.cache_data
def generate_data(country, qtd=1500):
    nichos_br = ["Marketing Digital", "Dropshipping", "Milhas Aéreas", "Investimentos", "Renda Extra", "Concursos", "Emagrecimento", "Treino em Casa", "Receitas Fit", "Nutrição", "Skincare", "Maquiagem", "Cabelo Cacheado", "Airfryer", "Churrasco", "Cerveja", "Pets", "Maternidade", "Viagem", "Fofoca", "BBB", "Sertanejo", "Funk", "Humor", "Podcast", "Futebol", "Games", "Free Fire", "Carros Rebaixados"]
    nichos_us = ["SaaS Growth", "AI Tools", "Crypto", "Real Estate", "Amazon FBA", "Remote Work", "Biohacking", "Keto Diet", "Pilates", "Mental Health", "Skincare ASMR", "Van Life", "Tiny Homes", "Tradwife", "Pottery", "Woodworking", "Gaming Setup", "True Crime", "Cleaning ASMR", "Streetwear", "Sneakers", "Pickleball"]

    lista = nichos_us if country == "US" else nichos_br
    # Pool de vídeos funcionais
    videos_pool = [
        "https://www.tiktok.com/@amazonhome/video/7298123456789012345", 
        "https://www.tiktok.com/@hudabeauty/video/7234567890123456789",
        "https://www.tiktok.com/@apple/video/7306076366050512174",
        "https://www.tiktok.com/@tiktok/video/7258384074697313562",
        "https://www.tiktok.com/@khaby.lame/video/7258384074697313562"
    ]

    data = []
    for i in range(qtd):
        n = random.choice(lista)
        item = {
            "id": i, "user": f"@{n.lower().replace(' ','')}_{random.randint(10,99)}", "niche": n,
            "url": random.choice(videos_pool), "views": f"{random.randint(10, 900)}K",
            "analise": f"Alta retenção detectada em {n}."
        }
        data.append(item)
    return data

# ==============================================================================
# 4. INTERFACE PRINCIPAL
# ==============================================================================

# Cabeçalho
c1, c2 = st.columns([1, 5])
with c1:
    st.markdown("<h1 style='margin:0;'>🥝</h1>", unsafe_allow_html=True)
with c2:
    st.markdown("<h1 style='margin:0; font-size:24px; padding-top:10px;'>RADAR VIRAL</h1>", unsafe_allow_html=True)

st.write("") 

# BOTÃO DE FILTRO (PRETO E BRANCO)
with st.expander("⚙️ CLIQUE PARA FILTRAR (PAÍS & NICHO) 🔽", expanded=False):
    st.markdown("### 1. REGIÃO")
    region = st.radio("", ["🇺🇸 Estados Unidos", "🇧🇷 Brasil"], index=1)
    country_code = "US" if "Estados Unidos" in region else "BR"
    
    db = generate_data(country_code, 2000)
    
    st.markdown("### 2. NICHO")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "TODOS")
    filtro_cat = st.selectbox("", cats)

# FEED
flag = "🇺🇸" if country_code == "US" else "🇧🇷"
st.markdown(f"### {flag} RESULTADOS:", unsafe_allow_html=True)

filtrado = db
if filtro_cat != "TODOS":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]

for v in filtrado[:10]:
    # Card Container
    st.markdown(f"""
    <div class="video-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; border-bottom: 1px solid #000; padding-bottom:5px;">
            <span style="font-weight:900; font-size:1.1em;">{v['user']}</span>
            <span class="niche-badge">{v['niche']}</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Player
    try: vid_id = v['url'].split("/video/")[1].split("?")[0]
    except: vid_id = "7258384074697313562"
    
    components.html(f"""
        <style>body{{margin:0;padding:0;}}</style>
        <blockquote class="tiktok-embed" cite="{v['url']}" data-video-id="{vid_id}" style="max-width: 100%; min-width: 100%;" > 
        <section> <a target="_blank" href="{v['url']}">Ver no App</a> </section> </blockquote> 
        <script async src="https://www.tiktok.com/embed.js"></script>
    """, height=340)
    
    # Texto Descritivo em Preto
    st.markdown(f"""
        <div style="margin-top:10px; color:#000;">
            <p style="margin-bottom:0px; font-weight:bold;">ANÁLISE:</p>
            <p style="margin-top:0px;">{v['analise']}</p>
            <p style="font-weight:900; font-size:1.1em; margin-top:5px;">👁️ {v['views']} Visualizações</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<center>Kiwi Tok v12.0 • Ultra Contrast</center><br>", unsafe_allow_html=True)
