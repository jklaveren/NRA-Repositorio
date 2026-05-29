import streamlit as st

st.set_page_config(page_title='NRA | Evolução Comercial', layout='wide')

# Estilo padronizado
st.markdown("""
<style>
    :root { --nra-azul: #102A52; --nra-accent: #E63946; }
    .stApp { background-color: #f0f2f6; }
    .header-box { background: var(--nra-azul); color: white; padding: 30px; border-radius: 12px; text-align: center; margin-bottom: 30px; }
    .block-text { 
        background: #ffffff; 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid var(--nra-azul); 
        margin-bottom: 25px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
    }
    h2 { color: var(--nra-azul); text-align: center; margin-bottom: 20px; }
    .sub-text { color: #555; text-align: center; font-style: italic; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="header-box"><h1>NRA Advocacia Empresarial: Evolução Comercial</h1></div>', unsafe_allow_html=True)

# 1. Desenvolvimento de Prospecção
st.markdown('<div class="block-text"><h2>Desenvolvimento de Aplicativo Próprio</h2><p class="sub-text">Automação de ponta a ponta para otimizar o tempo e reduzir a dependência de métodos manuais. Unificação de dados de fontes diversas.</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
arquivos = ["img/img1.jpeg", "img/img2.jpeg", "img/img3.jpeg"]
legendas = ["Interface de Busca", "Motor de Extração", "Informações sobre os Leads"]

for col, img_path, cap in zip([c1, c2, c3], arquivos, legendas):
    with col:
      st.image(img_path, caption=cap, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 2. Estrutura de Prospecção (Teste A/B)
st.markdown('<div class="block-text"><h2>Estrutura de Prospecção</h2>', unsafe_allow_html=True)

# Selo de Teste A/B
st.markdown("""
    <div style="text-align:center; margin-bottom: 20px;">
        <span style="background-color: #102A52; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.8rem;">
            TESTE A/B EM OPERAÇÃO
        </span>
        <p style="color: #555; font-style: italic; margin-top: 10px;">
            Análise comparativa de canais para identificar onde o custo de aquisição é menor e a conversão em reuniões é maior.
        </p>
    </div>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown('<div style="padding:20px; background:#f9f9f9; border-radius:10px; text-align:center; border-top:4px solid var(--nra-accent);"><h3 style="color:var(--nra-accent);">Cold Calling</h3><p style="font-size:2rem; font-weight:800; margin:0;">1</p><p>Reunião</p></div>', unsafe_allow_html=True)
with col_b:
    st.markdown('<div style="padding:20px; background:#eef2f7; border-radius:10px; text-align:center; border-top:4px solid var(--nra-azul);"><h3 style="color:var(--nra-azul);">Mala Direta(E-mail)</h3><p style="font-size:2rem; font-weight:800; margin:0;">8</p><p>Reuniões</p></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 3. Mapeamento de Demanda de Mercado (Dados Estratégicos)
st.markdown('<div class="block-text"><h2>Oportunidades de Mercado</h2><p class="sub-text">Segmentos com maior volume de busca pelos clientes, identificados através do nosso motor de inteligência.</p>', unsafe_allow_html=True)

cols = st.columns(2)
# Aqui alteramos a lógica para focar em "Volume de Busca" identificado pelo seu App
demandas = [
    ("🚀 Alta Demanda: Tributário", "Recuperação de créditos fiscais lidera as buscas dos clientes."),
    ("🤝 Alta Demanda: Societário", "Crescimento expressivo em estruturação corporativa."),
    ("⚖️ Demanda Estável: Trabalhista", "Volume constante em gestão preventiva de passivo."),
    ("📈 Oportunidade: Recuperação", "Busca crescente por reestruturação de empresas.")
]

for i, (tit, sub) in enumerate(demandas):
    with cols[i % 2]:
        st.markdown(f"""
            <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #E63946;">
                <h4 style="color:#102A52; margin: 0 0 10px 0;">{tit}</h4>
                <p style="font-size:1rem; margin: 0;">{sub}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 4. Resultados e Fechamento
st.markdown('<div class="block-text"><h2>Resultados Obtidos: Nova Estratégia</h2><p class="sub-text">Indicadores de performance que validam a viabilidade da nova estrutura comercial de prospecção através de mala direta.</p>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.markdown('<div style="padding:15px; text-align:center; border-top:4px solid var(--nra-azul);"><div style="font-size:1.5rem; font-weight:800; color:var(--nra-azul);">1</div><div style="font-size:0.8rem;">Parceria Consolidada</div></div>', unsafe_allow_html=True)
c2.markdown('<div style="padding:15px; text-align:center; border-top:4px solid var(--nra-azul);"><div style="font-size:1.5rem; font-weight:800; color:var(--nra-azul);">10-20</div><div style="font-size:0.8rem;">Projeção de Contratos</div></div>', unsafe_allow_html=True)
c3.markdown('<div style="padding:15px; text-align:center; border-top:4px solid var(--nra-accent);"><div style="font-size:1.5rem; font-weight:800; color:var(--nra-accent);">5.000+</div><div style="font-size:0.8rem;">Leads trabalhados</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Fechamento
st.markdown("""
<div class="block-text" style="background:#f9f9f9; text-align:center;">
    <h2>Próximos Passos: Integração Estratégica</h2>
    <p>Nosso modelo está validado. <b>Aguardo o alinhamento com o Marketing e Ads</b> para começar a escalar nossa presença e transformar tráfego em contratos qualificados.</p>
</div>
""", unsafe_allow_html=True)