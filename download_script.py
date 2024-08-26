import requests
import os
from pathlib import Path

def download_files(dest_dir=None):
    # Se nenhum diretório for especificado, usa o diretório de downloads padrão do usuário
    if dest_dir is None:
        dest_dir = str(Path.home() / "Downloads")
    
    # Verifica se o diretório existe, se não, cria-o
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    urls = [
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Mega-Sena',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotofacil',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Quina',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotomania',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Timemania',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Dupla-Sena',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Dia-de-Sorte',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Super-Sete',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Mais-Milionaria',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Federal'
    ]

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            content_disposition = response.headers.get('content-disposition')
            if content_disposition:
                file_name = content_disposition.split('filename=')[-1].strip('"')
            else:
                file_name = url.split('modalidade=')[-1] + '.zip'
            file_path = os.path.join(dest_dir, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Arquivo '{file_name}' baixado com sucesso para {file_path}.")
        else:
            print(f"Erro ao fazer download de {url}. Código de status: {response.status_code}")

    return "Download concluído com sucesso!"

# Exemplo de uso
download_files()
