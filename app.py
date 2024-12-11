import streamlit as st
from pydantic import ValidationError
from contrato import Compras
from database import salvar_dados_postgres

def main():

    st.title('Fluxo de Caixa')    

    descricao = st.selectbox('Descrição:', sorted(['Gasolina', 'Mercado', 'Restaurante', 'Conta Fixa', 'Padaria']))    
    parcela = st.number_input("Compra Parcelada:", min_value=0, value=1, step=1, format="%d")
    dt_compra = st.date_input("Data Compra:")
    valor = st.number_input("Valor:")
    nome = st.selectbox('Quem pagou:', sorted(['Quenia', 'Rafa'])) 
    conta = st.selectbox('Despesa individual ou conjunta:', sorted(['Individual Quenia', 'Individual Rafa', 'Conjunta']))
    observacao = st.text_input("Observação Compra:")

    if st.button("Salvar"):

        try:
            # chamando o contrato dos dados
            dados_compra = Compras( descricao = descricao, 
                                    parcela = parcela,
                                    dt_compra = dt_compra, 
                                    valor = valor, 
                                    nome = nome,
                                    conta = conta,
                                    observacao = observacao)
            
            st.title("**Detalhes da Compra:**")
            st.write(dados_compra) 
         
            try:
                salvar_dados_postgres(dados_compra)
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")
     
        except ValidationError as e:
            st.error(f"Deu erro: {e}")     
       
if __name__=="__main__":
    main()
