import os

# Caminho do diretório onde estão os arquivos
diretorio = r"C:\Users\Usuário\Downloads\curriculosAutomação"

# Itera sobre os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    # Verifica se os caracteres '(' e ')' estão no nome do arquivo
    if '(' in nome_arquivo and ')' in nome_arquivo:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        try:
            os.remove(caminho_arquivo)
            print(f"Arquivo removido: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao remover {nome_arquivo}: {e}")
