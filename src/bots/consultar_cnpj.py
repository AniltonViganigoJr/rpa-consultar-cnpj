import yaml
from pathlib import Path
from src.utils.logger import setup_logger
from src.tasks.api import get_dados_cnpj

def executar(cnpj):
    log = setup_logger()
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
            return resposta
        log.warning(f'API - Status code: {resposta.get('status')}')
        return None
    except Exception as e:
        log.exception(f'Exception Error: {e}')
        print(e)
