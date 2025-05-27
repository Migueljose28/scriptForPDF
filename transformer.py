import os
from PIL import Image
from docx import Document
from fpdf import FPDF
from docx2pdf import convert

class Transformer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        if not os.path.isdir(folder_path):
            raise ValueError(f"Caminho inválido: {folder_path}")

    def image_to_pdf(self, image_path, output_path):
        with Image.open(image_path) as img:
            img.convert('RGB').save(output_path, "PDF")
        print(f"Imagem convertida: {image_path} -> {output_path}")

    def word_to_pdf(self, docx_path, output_path):
        convert(docx_path, output_path)
        print(f"Word convertido: {docx_path} -> {output_path}")

    def is_pdf(self, file_path):
        try:
            with open(file_path, "rb") as file:
                header = file.read(5)
                return header == b"%PDF-"
        except Exception:
            return False

    def convert_files_in_folder(self):
        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            output_path = os.path.splitext(file_path)[0] + ".pdf"

            if os.path.isfile(file_path):
                if self.is_pdf(file_path):
                    print(f"{file_name} já é um PDF válido.")
                elif file_name.lower().endswith((".jpg", ".jpeg", ".png")):
                    print(f"Convertendo imagem: {file_name} -> PDF")
                    self.image_to_pdf(file_path, output_path)
                elif file_name.lower().endswith(".docx"):
                    print(f"Convertendo Word: {file_name} -> PDF")
                    self.word_to_pdf(file_path, output_path)
                else:
                    print(f"Formato não suportado: {file_name}")

    def run(self):
        self.convert_files_in_folder()
        print("Processamento finalizado.")


if __name__ == "__main__":
    path = r"C:\Users\Usuário\Downloads\curriculosAutomação"
    transformer = Transformer(path)
    transformer.run()
