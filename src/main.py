import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.bots.consultar_cnpj import executar

if __name__ == '__main__':
    executar(...)