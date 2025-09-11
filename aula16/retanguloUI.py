import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header('Cálculos com Retângulo') #cabeçalho da página
        base = st.text_input('Informe a base:')
        altura = st.text_input('Informe a altura:')
        if st.button('Calcular'): #cria um botão
            base = float(base)
            altura = float(altura)
            retangulo = Retangulo(base, altura)
            st.write(retangulo) #parágrafo na página
            st.write(retangulo.calc_area())
            st.write(retangulo.calc_diagonal())