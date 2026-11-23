import streamlit as st

# Configuração da página
st.set_page_config(page_title="Demonstração do Streamlit", page_icon="🧪")

# Título principal
st.title("Minha primeira aplicação com Streamlit")

# Texto simples
st.write("Esta aplicação demonstra algumas funções básicas do Streamlit.")

st.divider()

# Seção sobre a ferramenta
st.header("O que é Streamlit?")
st.write(
    "Streamlit é uma biblioteca Python que permite criar aplicações web "
    "interativas de forma simples, sem precisar desenvolver HTML, CSS ou JavaScript."
)

# Subtítulo
st.subheader("Exemplo de interação")

nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}! Seja bem-vindo(a) à aplicação.")

st.divider()

# Demonstração de Markdown
st.header("Formatando textos com Markdown")
st.markdown("É possível escrever **textos em negrito**, *itálico* e também criar listas:")
st.markdown("""
- Primeiro item
- Segundo item
- Terceiro item
""")

# Legenda
st.caption("Exemplo de legenda: este texto aparece menor e pode ser usado como observação.")

st.divider()

# Exibição de código
st.header("Exemplo de código Python")
st.write("O Streamlit também consegue exibir trechos de código:")
st.code(
    'import streamlit as st\n\nst.title("Olá, mundo!")\nst.write("Minha primeira aplicação")',
    language="python"
)

st.divider()

st.subheader("Conclusão")
st.write("Com poucas linhas de Python, conseguimos criar uma página web simples e interativa.")
