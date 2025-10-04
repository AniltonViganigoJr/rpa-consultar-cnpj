"""
Módulo: logger.py
Descrição: Este módulo configura e demonstra o uso do logger
em Python, gravando mensagens no console e em arquivo.
"""

import logging
from pathlib import Path

def setup_logger():
    """
        Configura o logger do projeto.

        Cria o diretório 'logs' se não existir, configura
        o arquivo de log 'execution.log' e adiciona handlers
        para gravação em arquivo e console.

        Retorna:
            None
    """
    log_dir = Path(__file__).resolve().parent.parent.parent / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'execution.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('RPA')
