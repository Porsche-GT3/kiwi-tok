import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. CONFIGURAÇÃO VISUAL (TEMA ZEN)
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok", page_icon="🥝", layout="wide")

# PALETA DE CORES PASTEL
COR_FUNDO = "#F1F8E9"       # Verde muito claro (quase branco)
COR_ACCENT = "#AED581"      # Verde Kiwi Suave
COR_TEXTO = "#33691E"       # Verde Floresta (para leitura)
COR_CARD = "#FFFFFF"        # Branco Puro
COR_BOTAO = "#8BC34A"       # Verde Principal

# CSS AVANÇADO (INJETANDO BELEZA)
st.markdown(f"""
    <style>
    /* Importando fonte arredondada e calma */
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Nunito', sans-serif;
        color: {COR_TEXTO};
    }}
    
    /* Fundo Geral */
    .stApp {{
        background-color: {COR_FUNDO};
    }}
    
    /* Esconder menus padrões chatos */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Estilizando a Sidebar */
    [data-testid="stSidebar"] {{
        background-color: #FFFFFF;
        border-right: 1px solid #DCEDC8;
    }}
    
    /* BOTÕES PERSONALIZADOS (Suaves) */
    .stButton > button {{
        background-color: {COR_BOTAO};
        color: white;
        border-radius: 25px;
        border: none;
        padding: 12px 30px;
        font-weight: 700;
        box-shadow: 0 4px 6px rgba(139, 195, 74, 0.2);
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: {COR_ACCENT};
        transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(139, 195, 74, 0.3);
    }}
    
    /* CAIXAS DE TEXTO (Inputs) */
    .stTextInput > div > div > input {{
        border-radius: 15px;
        border: 1px solid #DCEDC8;
        padding: 10px;
    }}
    
    /* CARD DE LOGIN (Centralizado e Bonito) */
    .login-container {{
        background-color: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #F0F4C3;
    }}
    
    /* CARD DE VÍDEO (Design Apple/Clean) */
    .video-card {{
        background: white;
        padding: 20px;
        border-radius: 25px;
        border: 1px solid #F1F8E9;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03); /* Sombra muito suave */
        transition: transform 0.3s ease;
    }}
    .video-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(139, 195, 74, 0.15);
    }}
    
    /* Badge de Nicho */
    .niche-badge {{
        background-color: #F1F8E9;
        color: {COR_TEXTO};
        padding: 5px 12px;
        border-radius: 12px;
        font-size: 0.8em;
        font-weight: 800;
        letter-spacing: 0.5px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. SISTEMA DE LOGIN (AGORA BONITO)
# ==============================================================================
def check_password():
    """Tela de Login estilo 'SaaS Premium'"""
    if st.session_state.get('password_correct', False):
        return True

    # Layout de colunas para centralizar
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True) # Espaço vazio
        st.markdown("""
        <div class="login-container">
            <h1 style='color:#8BC34A; font-size: 3em;'>🥝</h1>
            <h2 style='color:#33691E;'>Bem-vindo ao Kiwi Tok</h2>
            <p style='color:#7CB342;'>Inteligência Viral Suave</p>
        </div>
        """, unsafe_allow_html=True)
        
        senha = st.text_input("Senha de Acesso:", type="password", placeholder="Digite sua chave...")
        
        if st.button("✨ Entrar no Sistema", use_container_width=True):
            if senha == "kiwi2026":
                st.session_state['password_correct'] = True
                st.rerun()
            else:
                st.error("🔒 Senha incorreta.")
    return False

if not check_password():
    st.stop()

# ==============================================================================
# 3. LÓGICA DO APP (DADOS)
# ==============================================================================
@st.cache_data
def generate_database(qtd=500):
    nichos = ["🌿 Yoga & Pilates", "💄 Beleza Clean", "💻 Tech Minimalista", "🧘‍♀️ Meditação", "🏠 Home Decor", "🥗 Comida Saudável", "👗 Moda Slow", "🐱 Pets Fofos", "✈️ Viagem Zen", "📚 Estudos"]
    videos_reais = [
        "https://www.tiktok.com/@amazonhome/video/7298123456789012345", 
        "https://www.tiktok.com/@hudabeauty/video/7234567890123456789",
        "https://www.tiktok.com/@apple/video/7306076366050512174",
        "https://www.tiktok.com/@tiktok/video/7258384074697313562"
    ]
    data = []
    for i in range(qtd):
        n = random.choice(nichos)
        item = {
            "id": i, "user": f"@creator_{random.randint(10,99)}", "niche": n,
            "url": random.choice(videos_reais), 
            "views": f"{random.randint(100, 900)}K",
            "analise": f"Estética visual calma. Retenção alta detectada em {n}."
        }
        data.append(item)
    return data

db = generate_database()

# ==============================================================================
# 4. A INTERFACE PRINCIPAL (ZEN)
# ==============================================================================

# Sidebar Limpa
with st.sidebar:
    st.title("🥝 Menu")
    st.write("") # Espaço
    
    # Filtro com design melhorado
    st.markdown("**🔍 O que você procura?**")
    busca = st.text_input("", placeholder="Ex: Yoga...")
    
    st.markdown("**📂 Categorias**")
    cats = sorted(list(set([x['niche'] for x in db])))
    cats.insert(0, "✨ Ver Tudo")
    filtro_cat = st.radio("", cats)
    
    st.write("---")
    st.caption("Modo Zen v7.0 • Online")
    if st.button("Sair"):
        st.session_state['password_correct'] = False
        st.rerun()

# Conteúdo Principal
st.markdown("<h1 style='font-weight: 800; color: #33691E;'>Oasis de Tendências</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #7CB342; margin-top: -15px;'>Descubra o que viraliza com tranquilidade.</p><br>", unsafe_allow_html=True)

# Lógica de Filtro
filtrado = db
if filtro_cat != "✨ Ver Tudo":
    filtrado = [x for x in filtrado if x['niche'] == filtro_cat]
if busca:
    filtrado = [x for x in filtrado if busca.lower() in x['niche'].lower()]

# Grid de Vídeos
col1, col2 = st.columns(2)

for i, v in enumerate(filtrado[:10]): # Mostra 10 por página para ficar leve
    local = col1 if i % 2 == 0 else col2
    with local:
        st.markdown(f"""
        <div class="video-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <span style="font-weight:700; font-size:1.1em;">{v['user']}</span>
                <span class="niche-badge">{v['niche']}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Player
        try: vid_id = v['url'].split("/video/")[1].split("?")[0]
        except: vid_id = "7258384074697313562"
        
        # Player embutido
        components.html(f"""
            <blockquote class="tiktok-embed" cite="{v['url']}" data-video-id="{vid_id}" style="max-width: 100%;min-width: 200px;" > 
            <section> <a target="_blank" href="{v['url']}">Ver</a> </section> </blockquote> 
            <script async src="https://www.tiktok.com/embed.js"></script>
        """, height=380)
        
        st.markdown(f"""
            <div style="margin-top:10px; color:#558B2F; font-size:0.9em;">
                👁️ {v['views']} Visualizações
            </div>
            <div style="margin-top:5px; padding:10px; background-color:#F9FBF7; border-radius:10px; font-size:0.85em; color:#666;">
                ✨ {v['analise']}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><center style='color:#AED581'>🥝 Design by Kiwi Zen</center>", unsafe_allow_html=True)
