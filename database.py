import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from contrato import Compras
import streamlit as st

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def salvar_dados_postgres(dados: Compras):
    """
    Função para salvar no postgres
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS     
        )
        # Mensagem de sucesso para a conexão
        st.success("Conexão com o banco de dados realizada com sucesso!")

        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de compras
        insert_query = sql.SQL(
            "INSERT INTO streamlit.fluxo_caixa (descricao, parcela, dt_compra, valor, nome, conta, observacao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.descricao,
            dados.parcela,
            dados.dt_compra,
            dados.valor,
            dados.nome,
            dados.conta,
            dados.observacao
        
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")