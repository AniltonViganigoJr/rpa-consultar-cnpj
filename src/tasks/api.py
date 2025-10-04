import http.client
import json
from src.utils.logger import setup_logger

log = setup_logger()
        
def get_dados_cnpj(url: str, cnpj: str) -> any:
    conexao = http.client.HTTPSConnection(url)
    log.info('API - Conexão realizada com sucesso')
    conexao.request('GET', f'/v1/cnpj/{cnpj}')
    log.info('API - Requisição realizada com sucesso')
    resposta = conexao.getresponse()
    dados = resposta.read()
    empresa = json.loads(dados.decode('utf-8'))
    conexao.close()
    log.info('API - Conexão encerrada realizada com sucesso')
    
    if empresa.get('status','') == 'Error':
        log.info(f'API - Não foi possível obter os dados do CNPJ: {cnpj}')
        return empresa.get('message', 'Não foi possível obter os dados da empresa')
    
    log.info('API - Dados obtidos com sucesso')
    return empresa
    