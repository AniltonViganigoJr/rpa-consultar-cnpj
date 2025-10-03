from pathlib import Path
import unittest
import logging
import shutil
import sys
from src.utils import logger
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

class TestLogger(unittest.TestCase):
    def setup(self):
        #Define o path do diretório de logs
        self.log_dir = Path(__file__).resolve().parent.parent.parent / 'logs'
        #Remove o diretório se já existir
        if self.log_dir.exists():
            shutil.rmtree(self.log_dir)
            
    def test_logger_creation(self):
        test_logger = logger.setup_logger()
        #Testa se retornou um Logger
        self.assertIsInstance(test_logger, logging.Logger)
        #Testa se o diretório logs foi criado
        self.assertTrue(self.log_dir.exists())
        #Testa se o arquivo execution.log foi criado (inicialmente vazio)
        log_file = self.log_dir / 'execution.log'
        #Dispara uma mensagem de teste
        logging.info('Mensagem teste!')
        #O arquivo deve existir agora
        self.assertTrue(log_file.exists())

if __name__ == '__main__':
    unittest.main()
        