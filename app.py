import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (MOBILE UX + ALTO CONTRASTE)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok Mobile", page_icon="🥝", layout="wide")

# CORES DE ALTO CONTRASTE
COR_FUNDO = "#F4F6F0"       # Off-white (confortável)
COR_TITULO = "#000000"      # Preto Absoluto
COR_TEXTO = "#111111"       # Preto Leitura
COR_BOTAO = "#2E7D32"       # Verde Escuro
COR_EXPANDER = "#FFFFFF"    # Fundo do menu

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {{ 
        font-family: 'Nunito', sans-serif; 
        color: {COR_TEXTO}; 
    }}
    
    .stApp {{ background-color: {COR_FUNDO}; }}
    
    /* Esconde menu padrão do Streamlit para parecer App Nativo */
    #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} header {{visibility: hidden;}}
    
    /* ESTILO DO BOTÃO DE FILTRO (EXPANDER) */
    .streamlit-expanderHeader {{
        font-weight: 900;
        color: white;
        background-color: {COR_BOTAO};
        border-radius: 10px;
        font-size: 1.1em;
        padding: 15px;
    }}
    
    /* Container do Login */
    .login-container {{ 
        background-color: white; 
        padding: 30px 20px; 
        border-radius: 20px; 
        box-shadow: 0 8px 20px rgba(0,0,0,0.1); 
        text-align: center; 
        border: 1px solid #ccc;
    }}
    
    /* Cards de Vídeo Mobile */
    .video-card {{
        background: white; 
        padding: 15px; 
        border-radius: 15px; 
        border: 1px solid #ddd;
        margin-bottom: 25px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); 
    }}
    
    /* Badges e Textos */
    .niche-badge {{
        background-color: #000;
        color: white !important;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.85em;
        font-weight: bold;
        text-transform: uppercase;
    }}
    
    /* Ajuste de iframe para celular */
    iframe {{ width: 100% !important; }}
    
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. LOGIN SEGURO
# ==============================================================================
def check_password():
    if st.session_state.get('password_correct', False): return True
    
    col1, col2, col3 = st.columns([1, 4, 1]) # Coluna do meio maior para mobile
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="login-container">
            <h1 style='color:#2E7D32; margin:0;'>🥝 KIWI</h1>
            <p style='color:#000; font-weight:bold;'>Acesso Restrito</p>
        </div>
        """, unsafe_allow_html=True)
        
        senha = st.text_input("Senha:", type="password", placeholder="kiwi2026")
        
        if st.button("🔓 ACESSAR SISTEMA", use_container_width=True):
            if senha == "kiwi2026":
                st.session_state['password_correct'] = True
                st.rerun()
            else: st.error("Senha incorreta.")
    return False

if not check_password(): st.stop()

# ==============================================================================
# 3. GERADOR DE DADOS
# ==============================================================================
@st.cache_data
def generate_global_data(country, qtd=1500):
    # === LISTAS REAIS ===
    nichos_br = ["Marketing Digital", "Dropshipping", "PLR", "Afiliados", "Milhas Aéreas", "Investimentos", "Renda Extra", "Concursos", "Emagrecimento", "Treino em Casa", "Receitas Fit", "Nutrição", "Skincare", "Maquiagem", "Unhas", "Cabelo Cacheado", "Airfryer", "Churrasco", "Cerveja", "Café", "Decoração", "Pets", "Maternidade", "Viagem", "Fofoca", "BBB", "Sertanejo", "Funk", "Humor", "Podcast", "Futebol", "Games", "Free Fire", "Carros Rebaixados"]
    nichos_us = ["SaaS Growth", "AI Tools", "Crypto", "Real Estate", "Amazon FBA", "Remote Work", "Biohacking", "Keto Diet", "Pilates", "Ice Bath", "Mental Health", "Skincare ASMR", "Van Life", "Tiny Homes", "Tradwife", "Pottery", "Woodworking", "Gaming Setup", "True Crime", "Cleaning ASMR", "Mom Life", "Streetwear", "Sneakers", "Watches", "Pickleball", "Golf"]

    lista = nichos_us if country == "US" else nichos_br
    analise_txt = "Viral pattern detected." if country == "US" else "Padrão viral detectado."
    
    # Pool de Links
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
# 4. INTERFACE PRINCIPAL (Mobile First)
# ==============================================================================

# Cabeçalho Fixo
c1, c2 = st.columns([1, 4])
with c1:
    st.markdown("<h1 style='margin:0; font-size:2.5em;'>🥝</h1>", unsafe_allow_html=True)
with c2:
    st.markdown("<h2 style='margin:0; padding-top:10px; color:#000;'>Kiwi Tok</h2>", unsafe_allow_html=True)

st.write("") # Espaço

# ==============================================================================
# 🔥 O BOTÃO/SETA NO TOPO (A SOLUÇÃO)
# ==============================================================================
# Colocamos os filtros aqui, e não na Sidebar.
# O "expander" cria o efeito de botão que abre o menu.

with st.expander("⚙️ CLIQUE AQUI PARA FILTRAR (PAÍS & NICHO) 🔽", expanded=False):
    st.markdown("**1. Escolha a Região:**")
    region = st.radio("", ["🇺🇸 Estados Unidos", "🇧🇷 Brasil"], index=1, horizontal=True)
    country_code = "US" if "Estados Unidos" in region else "BR"
    
    # Gera dados baseado na escolha
    db = generate_global_data(country_code, 2000)
    
    st.markdown("---")
    st.markdown("**2. Selecione o Nicho:**")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "✨ Ver Tudo")
    filtro_cat = st.selectbox("", cats)
    
    st.info(f"Mostrando banco de dados: {country_code}")

# ==============================================================================
# FEED DE VÍDEOS
# ==============================================================================
flag = "🇺🇸" if country_code == "US" else "🇧🇷"
st.markdown(f"<h3 style='color:#000; margin-top:20px;'>{flag} Resultados Encontrados:</h3>", unsafe_allow_html=True)

# Filtro Lógica
filtrado = db
if filtro_cat != "✨ Ver Tudo":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]

# Loop de Renderização (Estilo Feed Instagram)
for i, v in enumerate(filtrado[:10]): # Mostra 10 por vez
    
    # Card
    st.markdown(f"""
    <div class="video-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <span style="font-weight:900; font-size:1.1em; color:#000;">{v['user']}</span>
            <span class="niche-badge">{v['niche']}</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Player Seguro
    try: vid_id = v['url'].split("/video/")[1].split("?")[0]
    except: vid_id = "7258384074697313562"
    
    # Embed 100% largura
    components.html(f"""
        <style>body{{margin:0;padding:0;}}</style>
        <blockquote class="tiktok-embed" cite="{v['url']}" data-video-id="{vid_id}" style="max-width: 100%; min-width: 100%;" > 
        <section> <a target="_blank" href="{v['url']}">Ver no App</a> </section> </blockquote> 
        <script async src="https://www.tiktok.com/embed.js"></script>
    """, height=340)
    
    # Dados Abaixo
    st.markdown(f"""
        <div style="margin-top:12px; padding:12px; background-color:#f4f4f4; border-radius:10px;">
            <div style="font-weight:bold; color:#000; font-size:0.9em;">📊 KIWI ANALYTICS:</div>
            <div style="font-size:0.9em; color:#333; margin-bottom:5px;">{v['analise']}</div>
            <div style="font-weight:800; color:#2E7D32;">👁️ {v['views']} • 🔁 {v['shares']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Rodapé simples
st.markdown("<br><center style='color:#000; font-weight:bold;'>Fim dos resultados.</center><br><br>", unsafe_allow_html=True)
