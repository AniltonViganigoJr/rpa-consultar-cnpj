import yaml
import pandas as pd
from datetime import datetime
from pathlib import Path
from src.utils.logger import setup_logger
from src.tasks.api import get_dados_cnpj

#Instanciar a Variável 'log'
log = setup_logger()

def executar(cnpj):
    config_file = Path(__file__).resolve().parent.parent.parent / 'config' / 'settings.yaml'
    
    #Carregar configurações
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        log.info('Configurações carregadas com sucesso')
    
    #Endpoint da API
    site_url = config['site_url']
        
    try:
        resposta = get_dados_cnpj(site_url, cnpj)
        if resposta.get('status','').upper() == 'OK':
            log.info('API - Status code: OK')
    except Exception as e:
        log.exception(f'Exception Error: {e}')
        print(e)

    #Gravar os Dados Obtidos no Relatório
    gravar_dados_empresa(resposta)

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
        df.to_excel(writer, sheet_name=dados_empresa['nome'], index=False)
        log.info('[Output] Dados inseridos no relatório com sucesso')
