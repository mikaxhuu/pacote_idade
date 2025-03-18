from datetime import datetime
from math import floor

def calculo_idade(data_nascimento):

    anos = (datetime.now() - data_nascimento).days // 365
    meses = floor(((datetime.now() - data_nascimento).days / 365) * 12)
    dias = (datetime.now() - data_nascimento).days
    
    if anos == 1:
        return f'Você tem: {anos} anos de idade, {meses} meses e {dias} dias de vida.'

    elif anos != 1:
        return f'Você tem: {anos} anos de idade, {meses} meses e {dias} dias de vida.'
    
    data_nascimento = datetime.strptime(input('Informe a data de nascimento (formato dd/mm/AAAA): '), "%d/%m/%Y")

    return data_nascimento