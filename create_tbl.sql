--DROP TABLE IF EXISTS streamlit.fluxo_caixa;

CREATE TABLE streamlit.fluxo_caixa (

    id SERIAL PRIMARY KEY,
    descricao VARCHAR(50),
    parcela INTEGER,
    dt_compra DATE,
    valor NUMERIC,
    nome VARCHAR(50),
    conta VARCHAR(50),
    observacao VARCHAR(255)

);