import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (RESPONSIVA + ALTO CONTRASTE)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok Mobile", page_icon="🥝", layout="wide")

# CORES DE ALTO CONTRASTE
COR_FUNDO = "#F4F6F0"       # Fundo quase branco (Off-white)
COR_ACCENT = "#8BC34A"      # Verde Kiwi (Apenas detalhes)
COR_TEXTO_TITULO = "#000000" # Preto Puro
COR_TEXTO_CORPO = "#111111"  # Preto Suave
COR_BOTAO = "#2E7D32"       # Verde Escuro (Melhor leitura no botão)

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {{ 
        font-family: 'Nunito', sans-serif; 
        color: {COR_TEXTO_CORPO}; 
    }}
    
    .stApp {{ background-color: {COR_FUNDO}; }}
    #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} header {{visibility: hidden;}}
    
    [data-testid="stSidebar"] {{ background-color: #FFFFFF; border-right: 1px solid #ddd; }}
    
    /* Títulos bem pretos e legíveis */
    h1, h2, h3 {{ color: {COR_TEXTO_TITULO} !important; font-weight: 900 !important; }}
    p, div, span {{ color: {COR_TEXTO_CORPO}; }}
    
    /* Botões Grandes e Legíveis (Touch Friendly) */
    .stButton > button {{
        background-color: {COR_BOTAO}; 
        color: white !important; 
        border-radius: 12px; 
        border: none;
        padding: 15px 20px; /* Mais área de toque */
        font-weight: 800; 
        font-size: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: all 0.2s ease;
        width: 100%; /* Botão largo no celular */
    }}
    .stButton > button:hover {{ transform: scale(1.02); filter: brightness(1.1); }}
    
    /* Login Mobile Friendly */
    .login-container {{ 
        background-color: white; 
        padding: 30px 20px; 
        border-radius: 20px; 
        box-shadow: 0 8px 20px rgba(0,0,0,0.1); 
        text-align: center; 
        border: 1px solid #ccc;
    }}
    
    /* Cards Responsivos */
    .video-card {{
        background: white; 
        padding: 15px; 
        border-radius: 15px; 
        border: 1px solid #ddd;
        margin-bottom: 20px; 
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
    }}
    
    /* Tags de Nicho */
    .niche-badge {{
        background-color: {COR_TEXTO_TITULO};
        color: white !important;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.85em;
        font-weight: bold;
    }}
    
    /* Ajuste de iframe para celular */
    iframe {{ width: 100% !important; }}
    
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. LOGIN ROBUSTO
# ==============================================================================
def check_password():
    if st.session_state.get('password_correct', False): return True
    
    # Colunas vazias para centralizar no PC, mas no celular ocupa tudo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="login-container">
            <h1 style='color:#2E7D32; font-size: 3em; margin:0;'>🥝</h1>
            <h2 style='color:#000; margin-top:0;'>Acesso Mobile</h2>
            <p style='color:#333; font-weight:bold;'>Login Seguro</p>
        </div>
        """, unsafe_allow_html=True)
        
        senha = st.text_input("Digite a senha:", type="password", placeholder="kiwi2026")
        
        if st.button("🔓 ENTRAR AGORA"):
            if senha == "kiwi2026":
                st.session_state['password_correct'] = True
                st.rerun()
            else: st.error("Senha incorreta.")
    return False

if not check_password(): st.stop()

# ==============================================================================
# 3. DADOS (BRASIL & EUA)
# ==============================================================================
@st.cache_data
def generate_global_data(country, qtd=1500):
    
    # === LISTA BRASIL ===
    nichos_br = [
        "Marketing Digital", "Dropshipping", "PLR", "Afiliados", "Milhas Aéreas", "Investimentos", "Renda Extra", "Concursos", 
        "Emagrecimento", "Treino em Casa", "Receitas Fit", "Nutrição", "Skincare", "Maquiagem", "Unhas", "Cabelo Cacheado", 
        "Airfryer", "Churrasco", "Cerveja", "Café", "Decoração", "Pets", "Maternidade", "Viagem", 
        "Fofoca", "BBB", "Sertanejo", "Funk", "Humor", "Podcast", "Futebol", "Games", "Free Fire", "Carros Rebaixados"
    ]

    # === LISTA USA ===
    nichos_us = [
        "SaaS Growth", "AI Tools", "Crypto", "Real Estate", "Amazon FBA", "Remote Work",
        "Biohacking", "Keto Diet", "Pilates", "Ice Bath", "Mental Health", "Skincare ASMR", 
        "Van Life", "Tiny Homes", "Tradwife", "Pottery", "Woodworking", "Gaming Setup", 
        "True Crime", "Cleaning ASMR", "Mom Life", "Streetwear", "Sneakers", "Watches", "Pickleball", "Golf"
    ]

    if country == "US":
        lista = nichos_us
        analise_txt = "Viral pattern detected. High retention."
    else:
        lista = nichos_br
        analise_txt = "Padrão viral detectado. Retenção alta."

    # Links que funcionam bem em mobile
    videos_pool = [
        "https://www.tiktok.com/@amazonhome/video/7298123456789012345", 
        "https://www.tiktok.com/@hudabeauty/video/7234567890123456789",
        "https://www.tiktok.com/@apple/video/7306076366050512174",
        "https://www.tiktok.com/@tiktok/video/7258384074697313562",
        "https://www.tiktok.com/@redbull/video/7212345678901234567",
        "https://www.tiktok.com/@khaby.lame/video/7258384074697313562"
    ]

    data = []
    for i in range(qtd):
        n = random.choice(lista)
        item = {
            "id": i, 
            "user": f"@{n.lower().replace(' ','')}_{random.randint(10,99)}", 
            "niche": n,
            "url": random.choice(videos_pool), 
            "views": f"{random.randint(10, 900)}.{random.randint(1,9)}M",
            "shares": f"{random.randint(1, 50)}k",
            "analise": f"{analise_txt} ({n})"
        }
        data.append(item)
    return data

# ==============================================================================
# 4. INTERFACE PRINCIPAL
# ==============================================================================

# Sidebar Otimizada
with st.sidebar:
    st.markdown("## 🥝 Menu Kiwi")
    
    # Botões grandes de seleção de país
    region = st.radio("🌍 Escolha a Região:", ["🇺🇸 Estados Unidos", "🇧🇷 Brasil"], index=1)
    country_code = "US" if "Estados Unidos" in region else "BR"
    
    # Geração de dados
    db = generate_global_data(country_code, 2000) 
    
    st.markdown("---")
    st.markdown("**📂 Filtro de Nicho**")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "✨ Ver Tudo")
    filtro_cat = st.selectbox("", cats)
    
    st.markdown("---")
    if st.button("🚪 Sair do App"):
        st.session_state['password_correct'] = False
        st.rerun()

# Conteúdo Principal
flag = "🇺🇸" if country_code == "US" else "🇧🇷"
st.markdown(f"<h2 style='text-align:center; color:#000;'>{flag} Radar Viral</h2>", unsafe_allow_html=True)

# Métricas em uma linha só (scrollable no mobile se precisar)
col_m1, col_m2 = st.columns(2)
col_m1.metric("Vídeos", "2.000+")
col_m2.metric("Status", "Online 🟢")

# Filtro Lógica
filtrado = db
if filtro_cat != "✨ Ver Tudo":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]

st.write("") 

# GRID RESPONSIVO (O Segredo)
# No celular, st.columns empilha automaticamente.
# Vamos usar container para garantir largura total.

for i, v in enumerate(filtrado[:15]): # Limite de 15 para carregar rápido no 4G
    
    # Card Container
    st.markdown(f"""
    <div class="video-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <span style="font-weight:900; font-size:1.1em; color:#000;">{v['user']}</span>
            <span class="niche-badge">{v['niche']}</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Player Seguro (Tenta extrair ID, fallback para Khaby Lame se falhar)
    try: vid_id = v['url'].split("/video/")[1].split("?")[0]
    except: vid_id = "7258384074697313562"
    
    # Embed ajustado para largura 100%
    components.html(f"""
        <style>body{{margin:0;padding:0;}}</style>
        <blockquote class="tiktok-embed" cite="{v['url']}" data-video-id="{vid_id}" style="max-width: 100%; min-width: 100%;" > 
        <section> <a target="_blank" href="{v['url']}">Ver no TikTok</a> </section> </blockquote> 
        <script async src="https://www.tiktok.com/embed.js"></script>
    """, height=340)
    
    st.markdown(f"""
        <div style="margin-top:10px; padding:10px; background-color:#f0f0f0; border-radius:10px;">
            <div style="font-weight:bold; color:#000; font-size:0.9em;">📊 Análise:</div>
            <div style="font-size:0.9em; color:#333;">{v['analise']}</div>
            <div style="margin-top:5px; font-weight:800; color:#2E7D32;">👁️ {v['views']} • 🔁 {v['shares']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><center style='color:#999; font-size:0.8em;'>Kiwi Tok Mobile v10.0</center>", unsafe_allow_html=True)
