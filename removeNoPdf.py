import os

# Caminho da pasta onde estão os arquivos
pasta = r"C:\Users\Usuário\Downloads\curriculosAutomação"


# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    # Verifica se é um arquivo e se não termina com .pdf
    if os.path.isfile(caminho_arquivo) and not arquivo.lower().endswith(".pdf"):
        os.remove(caminho_arquivo)  # Exclui o arquivo
        print(f"Removido: {arquivo}")

print("Processo concluído!")
