#INICIO DE DOWNLOADS NA MÁQUINA LOCAL


import requests
import os

def download_files(dest_dir=r'C:\Users\Marcio Fernando Maia\Downloads'):
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
        else:
            print(f"Erro ao fazer download de {url}. Código de status: {response.status_code}")

    return "Download concluído com sucesso!"
 
#FIM DE DOWNLOADS NA MÁQUINA LOCAL



#INICIO DE DOWNLOADS NA MÁQUINA DE QUALQUER USUÁRIO
"""
import requests
import os

def get_user_download_dir():
    #Obtém o diretório padrão de downloads do usuário atual.
    if os.name == 'nt':  # Windows
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif os.name == 'posix':  # Unix/Linux/Mac
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        raise EnvironmentError("Sistema operacional não suportado")

def download_files(dest_dir=None):
    #Baixa arquivos para o diretório especificado ou o diretório de downloads do usuário.
    if dest_dir is None:
        dest_dir = get_user_download_dir()

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
        try:
            response = requests.get(url, timeout=10)  # Adiciona um timeout para evitar bloqueios
            response.raise_for_status()  # Levanta um erro para códigos de status HTTP não exitosos

            # Obtém o nome do arquivo a partir do cabeçalho Content-Disposition, se disponível
            content_disposition = response.headers.get('content-disposition')
            if content_disposition:
                file_name = content_disposition.split('filename=')[-1].strip('"')
            else:
                file_name = url.split('modalidade=')[-1] + '.zip'
            
            # Caminho completo do arquivo
            file_path = os.path.join(dest_dir, file_name)
            
            # Salva o arquivo no diretório de destino
            with open(file_path, 'wb') as file:
                file.write(response.content)
            
            print(f"Arquivo salvo em {file_path}")

        except requests.RequestException as e:
            print(f"Erro ao fazer download de {url}. Detalhes: {e}")

    return "Download concluído com sucesso!"

# Exemplo de uso
if __name__ == "__main__":
    print(download_files())


"""
#FIM DE DOWNLOADS NA MÁQUINA DE QUALQUER USUÁRIO
