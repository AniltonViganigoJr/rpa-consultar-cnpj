import pandas as pd
from pathlib import Path
from datetime import datetime
from src.utils.logger import setup_logger

#Instanciar a variável 'log'
log = setup_logger()

def gravar_dados_empresa(dados_empresa):
    
    #Validar se o Diretório Existe. Caso não exista, será criado
    output_dir = Path(__file__).resolve().parent.parent.parent / 'output'
    output_dir.mkdir(exist_ok=True)
    log.info('[Output] Diretório validado com sucesso')
    
    #Gerar Nome do Arquivo Excel
    nome_empresa = dados_empresa['nome']
    excel_file_name = output_dir / f'DadosEmpresa_{nome_empresa}_{datetime.now().strftime("%d_%m_%Y")}.xlsx'
    log.info('[Output] Nome do relatório definido com sucesso')
    log.info(f'[Excel] {excel_file_name}')
    
    #Gerar Dicionário com os Dados Específicos
    dados = {
    'Nome':[dados_empresa['nome']],
    'Atividade Principal': [dados_empresa['atividade_principal'][0]['text']],
    'Porte': [dados_empresa['porte']],
    'Atividades Secundárias': [dados_empresa['atividades_secundarias'][0]['text']],
    'Situação': [dados_empresa['situacao']]
    }
    
    #Criar o DataFrame
    df = pd.DataFrame(dados)
    
    #Inserir Dados no Relatório Excel
    with pd.ExcelWriter(excel_file_name, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=dados_empresa['nome'][:30],index=False)
        log.info('[Output] Dados inseridos no relatório com sucesso')
