import streamlit as st

def main():

    st.title('Fluxo de Caixa - AI Agent')    

    descricao = st.selectbox('Descrição:', ['Gasolina', 'Mercado', 'Restaurante', 'Produtos Limpeza', 'Conta Fixa'])    
    parcela = st.text_input("Compra Parcelada:")
    dt_compra = st.date_input("Data Compra:")
    valor = st.number_input("Valor:")
    observacao = st.text_input("Observação Compra:")

    if st.button("Salvar"):
        st.title("**Detalhes da Compra:**")
        st.write(f"**Descrição da compra:** {descricao}")
        st.write(f"**Compra Parcelada:** {parcela}")
        st.write(f"**Data Compra:** {dt_compra}")
        st.write(f"**Valor:** {valor}")
        st.write(f"**Observação Compra:** {observacao}")
    
if __name__=="__main__":
    main()