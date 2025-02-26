project_name/  # Nome do diretório do pacote
│   setup.py  # Arquivo de configuração do pacote
│   README.md  # Documentação do pacote
│   requirements.txt  # Lista de dependências
│
└───project_name/  # Diretório do módulo principal
    │   __init__.py  # Define este diretório como um pacote Python
    │   main.py  # Módulo principal

# Conteúdo de setup.py
from setuptools import setup, find_packages

setup(
    name="project_name",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gerar_senha=project_name.main:gerar_senha'
        ],
    },
)

# Conteúdo de requirements.txt (por enquanto vazio, pode ser preenchido conforme necessário)

# Conteúdo de README.md
# Gerador de Senhas Aleatórias

Este pacote gera senhas aleatórias seguras utilizando caracteres alfanuméricos e símbolos.

## Instalação

```
pip install .
```

## Uso

Para gerar uma senha com 12 caracteres padrão:

```python
from project_name.main import gerar_senha
print(gerar_senha())
```

# Conteúdo de main.py - Gerador de senhas
import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha aleatória segura com o tamanho especificado."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

if __name__ == "__main__":
    print("Senha gerada:", gerar_senha())
