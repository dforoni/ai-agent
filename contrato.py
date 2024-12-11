from pydantic import BaseModel,validator, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum
from typing import Optional


class DescricaoEnum(str, Enum):
    descricao01 = 'Gasolina'
    descricao02 = 'Mercado'
    descricao03 = 'Restaurante'
    descricao04 = 'Conta Fixa'
    descricao05 = 'Padaria'

class NomeEnum(str, Enum):
    nome01 = 'Quenia'
    nome02 = 'Rafa'

class ContaEnum(str, Enum):
    conta01 = 'Individual Quenia'
    conta02 = 'Individual Rafa'
    conta03 = 'Conjunta'

class Compras(BaseModel):
    """
    Classe de despesas geradas de custos diários.

    Args: AJUSTAR
    descricao: DescricaoEnum
    parcela: PositiveInt | None  # Número inteiro positivo ou None  
    dt_compra: datetime
    valor: PositiveFloat
    nome: NomeEnum
    conta: ContaEnum
    observacao: str

    """
    descricao: DescricaoEnum
    parcela: PositiveInt | None  # Número inteiro positivo ou None  
    dt_compra: datetime
    valor: PositiveFloat
    nome: NomeEnum
    conta: ContaEnum
    observacao: str | None

    @validator('descricao')
    def validate_descricao(cls, v):
        if v not in DescricaoEnum:
            raise ValueError(f"{v} não existe essa descrição.")
        return v
    
    @validator('nome')
    def validate_nome(cls, v):
        if v not in NomeEnum:
            raise ValueError(f"{v} não existe esse nome.")
        return v
    
    @validator('conta')
    def validate_conta(cls, v):
        if v not in ContaEnum:
            raise ValueError(f"{v} não existe essa conta.")
        return v
