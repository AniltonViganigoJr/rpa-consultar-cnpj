import http.client
import json
from src.utils.logger import setup_logger

session_logger = setup_logger()
        
def get_dados_cnpj(url: str, cnpj: str) -> any:
    conexao = http.client.HTTPSConnection(url)
    print(url)
    print(cnpj)
    session_logger.info('API - Conexão realizada com sucesso')
    conexao.request('GET', f'/v1/cnpj/{cnpj}')
    session_logger.info('API - Requisição realizada com sucesso')
    resposta = conexao.getresponse()
    dados = resposta.read()
    empresa = json.loads(dados.decode('utf-8'))
    conexao.close()
    session_logger.info('API - Conexão encerrada realizada com sucesso')
    
    if empresa.get('status','') == 'Error':
        session_logger.info(f'API - Não foi possível obter os dados do CNPJ: {cnpj}')
        return empresa.get('message', 'Não foi possível obter os dados da empresa')
    
    session_logger.info('API - Dados obtidos com sucesso')
    return empresa
    