import re
from pathlib import Path
from src.utils.logger import setup_logger
from src.bots.consultar_cnpj import executar

if __name__ == '__main__':
    #Instanciar a variável 'log'
    log = setup_logger()
    
    log.info("Início da execução do processo de consulta de CNPJs")
    
    #Lista de CNPJs
    lista_cnpj = [
        '92.963.560/0001-60'
    ]
    
    for cnpj in lista_cnpj:
        #Remover Caracteres Especiais
        cnpj = re.sub(r'\D', '', cnpj)
        
        if len(cnpj) == 14:
            try:
                executar(cnpj)
                log.info(f'CNPJ {cnpj} consultado com sucesso')
            except Exception as e:
                log.error(f'Erro ao consultar o CNPJ {cnpj}: {e}')
        else:
            log.warning(f'CNPJ inválido: {cnpj}')
    
    log.info("Processo finalizado com sucesso")