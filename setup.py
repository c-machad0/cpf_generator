"""
responsável por definir os metadados e configurações de empacotamento, facilitando:

- O reconhecimento correto dos módulos pelo Python
- A instalação do pacote (inclusive em modo editável com `pip install -e .`)
- A importação absoluta em testes e aplicações externas

Isso torna seu projeto “instalável” e garante que todas as dependências e caminhos sejam configurados automaticamente.
"""

from setuptools import find_packages, setup

setup(
    name='cpf_generator',
    version='0.1',
    package_dir={'': 'src'}, # diretorio do pacote
    packages=find_packages(where='src'), # permite encontrar pacotes dentro do código fonte do projeto
)