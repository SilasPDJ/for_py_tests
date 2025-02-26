import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import numpy as np

# Carrega os nomes dos arquivos da planilha Excel
df = pd.read_excel(
    "O:\\OneDrive\\Pai\\GRATEFUL-JAZZ-SINFONICA-MIA\\Osiel planilha.xlsx")

df['VALOR'] = df['VALOR'].replace('', np.nan)

df_filtered = df.dropna(subset=['VALOR'])
nomes = df_filtered['NOME'].tolist()


# Solicita o caminho do arquivo PDF
pdf_path = r"O:\OneDrive\Pai\GRATEFUL-JAZZ-SINFONICA-MIA\recibos\recibos.pdf"

# Verifica se o arquivo fornecido existe
if not os.path.isfile(pdf_path):
    print("O arquivo fornecido não existe.")
    exit()

# Cria o diretório de saída se não existir
output_dir = os.path.join(os.path.dirname(pdf_path), "Paginas")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Lê o arquivo PDF
with open(pdf_path, "rb") as infile:
    pdf = PdfFileReader(infile)
    num_pages = pdf.getNumPages()

    # Divide o PDF em páginas individuais e nomeia conforme os dados da planilha
    for page_num in range(num_pages):
        pdf = PdfFileReader(infile)
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page_num))

        # Define o nome do arquivo para cada página
        # Usa o nome correspondente da planilha se disponível
        nome_arquivo = nomes[page_num] if page_num < len(
            nomes) else f"pagina_{page_num + 1}"
        output_pdf_path = os.path.join(output_dir, f"{nome_arquivo}.pdf")

        # Salva a página individual como um novo PDF
        with open(output_pdf_path, "wb") as outfile:
            pdf_writer.write(outfile)

    print(f"PDF dividido em {num_pages} páginas e salvo em '{output_dir}'.")
