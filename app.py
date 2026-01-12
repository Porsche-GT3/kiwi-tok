import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ==============================================================================
# 1. SISTEMA DE LOGIN (SEGURANÇA)
# ==============================================================================
def check_password():
    """Retorna True se o usuário logar corretamente."""
    
    # Se já estiver logado, libera
    if st.session_state.get('password_correct', False):
        return True

    # Tela de Login Bonita
    st.markdown("""
        <style>
        .stApp {background-color: #000000;} /* Fundo Preto para Login */
        </style>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align: center; color: #8BC34A;'>🥝 Kiwi Tok</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: white;'>Acesso Restrito - Área de Membros</p>", unsafe_allow_html=True)
        
        password = st.text_input("Digite a Chave de Acesso:", type="password")
        
        if st.button("Entrar no Sistema"):
            if password == "kiwi2026":  # <--- SUA SENHA AQUI
                st.session_state['password_correct'] = True
                st.rerun()
            else:
                st.error("Senha incorreta. Acesso negado.")
    return False

# ==============================================================================
# CONFIGURAÇÃO GERAL
# ==============================================================================
st.set_page_config(page_title="Kiwi Tok - Login", page_icon="🥝", layout="wide")

# VERIFICA O LOGIN ANTES DE MOSTRAR O RESTO
if not check_password():
    st.stop()  # Para o código aqui se não tiver senha

# ==============================================================================
# AQUI COMEÇA O SEU SAAS (SÓ APARECE DEPOIS DO LOGIN)
# ==============================================================================

# CSS Profissional (Só carrega se logar)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #F8F9FA; }
    
    .video-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #E0E0E0;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    .video-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(139, 195, 74, 0.2);
        border-color: #8BC34A;
    }
    .niche-tag {
        background-color: #8BC34A;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75em;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 2. O GERADOR DE "BIG DATA"
@st.cache_data
def generate_database(qtd=1000):
    nichos_list = ["Dropshipping", "Beleza", "Tech", "Culinária", "Fitness", "Yoga", "Pesca", "Carros", "Skate", "Humor", "Pets/Gatos", "Crypto", "Finanças", "DIY", "Games", "Moda", "Marketing", "Imóveis"]
    video_pool = [
        "https://www.tiktok.com/@tiktok/video/7258384074697313562", 
        "https://www.tiktok.com/@amazonhome/video/7298123456789012345", 
        "https://www.tiktok.com/@apple/video/7306076366050512174", 
        "https://www.tiktok.com/@hudabeauty/video/7234567890123456789"
    ]
    data = []
    for i in range(qtd):
        nicho = random.choice(nichos_list)
        item = {
            "id": i, "user": f"@user_{random.randint(1000,9999)}", "niche": nicho,
            "url": random.choice(video_pool), "views": f"{random.randint(100, 900)}K",
            "engagement": f"{random.randint(5, 25)}%", "analysis": f"Alta retenção detectada em {nicho}."
        }
        data.append(item)
    return data

full_database = generate_database(1000) 

# 3. INTERFACE INTELIGENTE
with st.sidebar:
    st.title("🥝 Kiwi Tok")
    st.markdown(f"Bem-vindo, **Admin**") # Mostra que logou
    if st.button("Sair (Logout)"):
        st.session_state['password_correct'] = False
        st.rerun()
    st.write("---")
    
    # Filtros
    all_niches = sorted(list(set([x['niche'] for x in full_database])))
    all_niches.insert(0, "Todos os Nichos")
    selected_niche = st.selectbox("Navegar por Categoria:", all_niches)
    
    st.success("🟢 Sistema Online")

st.title("🔥 Banco de Dados Viral (Protegido)")

# Filtros Lógica
filtered_data = full_database
if selected_niche != "Todos os Nichos":
    filtered_data = [x for x in filtered_data if x['niche'] == selected_niche]

st.markdown(f"**Encontrados:** {len(filtered_data)} vídeos.")

# Grid
col1, col2 = st.columns(2)
for i, video in enumerate(filtered_data[:20]):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        st.markdown(f"""
        <div class="video-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-weight:bold; color:#333;">{video['user']}</span>
                <span class="niche-tag">{video['niche']}</span>
            </div>
            <div style="font-size:0.85em; color:#666; margin-bottom:10px;">
                👁️ {video['views']} • ❤️ {video['engagement']}
            </div>
        """, unsafe_allow_html=True)
        
        try: vid_id = video['url'].split("/video/")[1].split("?")[0]
        except: vid_id = "7258384074697313562"
            
        embed_code = f"""
            <blockquote class="tiktok-embed" cite="{video['url']}" data-video-id="{vid_id}" style="max-width: 100%;min-width: 200px;" > 
            <section> <a target="_blank" href="{video['url']}">Ver no TikTok</a> </section> </blockquote> 
            <script async src="https://www.tiktok.com/embed.js"></script>
        """
        components.html(embed_code, height=360, scrolling=True)
        st.markdown("</div>", unsafe_allow_html=True)