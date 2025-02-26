# Criando-um-pacote-de-Processamento-de-Imagens🔐 Gerador de Senhas Aleatórias
Este repositório contém um pacote Python simples para gerar senhas aleatórias seguras utilizando caracteres alfanuméricos e símbolos.

📌 Funcionalidades
✅ Geração de senhas aleatórias com tamanho personalizável
✅ Uso de letras, números e caracteres especiais
✅ Fácil instalação e uso

🚀 Instalação
Clone o repositório e instale o pacote localmente:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/project_name.git  
cd project_name  
pip install .  
⚡ Uso
Importe a função no seu código Python:

python
Copiar
Editar
from project_name.main import gerar_senha  
print(gerar_senha())  # Gera uma senha padrão com 12 caracteres  
print(gerar_senha(16))  # Gera uma senha com 16 caracteres  
📦 Publicação
Para publicar o pacote no PyPI:

bash
Copiar
Editar
python setup.py sdist bdist_wheel  
python -m twine upload --repository pypi dist/*  
🛠 Contribuindo
Contribuições são bem-vindas! Siga estes passos para contribuir:

Faça um fork do repositório
Crie uma branch para sua feature (git checkout -b minha-feature)
Commit suas mudanças (git commit -m 'Adicionei uma nova feature')
Faça um push (git push origin minha-feature)
Abra um Pull Request
📄 Licença
