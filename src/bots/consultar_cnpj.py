import yaml
from datetime import datetime
from pathlib import Path
from src.utils.logger import setup_logger
from src.tasks.api import get_dados_cnpj
from src.bots.gravar_dados_empresa import gravar_dados_empresa

#Instanciar logger
log = setup_logger()

#Carregar informações do arquivo 'settings.yaml'
if 'config' not in globals():
    config_file = Path(__file__).resolve().parent.parent.parent / 'config' / 'settings.yaml'

    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        log.info('Configurações carregadas com sucesso')

def executar(cnpj:str) -> bool:
    log.info(f'Iniciando execução para o CNPJ: {cnpj} às {datetime.now().strftime("%H:%M:%S")}')
    
    #Endpoint da API
    site_url = config['site_url']
    if not site_url:
        log.error("Chave 'site_url' não encontrada no arquivo 'settings.yaml'")
        return False
        
    try:
        resposta = get_dados_cnpj(site_url, cnpj)
        if resposta and isinstance(resposta, dict) and resposta.get('status','').upper() == 'OK':
            log.info('API - Status code: OK')
            #Gravar os Dados Obtidos no Relatório
            gravar_dados_empresa(resposta)
            log.info(f'Execução concluída para o CNPJ: {cnpj} às {datetime.now().strftime("%H:%M:%S")}')
            return True
        else:
            log.warning(f'Dados inválidos retornados para o CNPJ: {cnpj}')
            return False
    except Exception as e:
        log.exception(f'Erro ao consultar a API: {e}')
        return False
