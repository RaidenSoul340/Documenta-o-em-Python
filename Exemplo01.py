import fitz
from docx import Document 

#Convertendo de PDF para docx
def pdf_to_docx(pdf, docx):
    pdf_document = fitz.open(pdf)
    doc = Document()

    #Percorrendo cada pagina do do Arquivo PDF
    for item in range(pdf_document.page_count):
        pagina = pdf_document.load_page(item)#Carrega a página especifica com o indice
        texto = pagina.get_text("text")#Extrai o texto da página e retorna uma string
        doc.add_paragraph(texto)#Adicionana cada texto extraindo em um paragrafo no doc

    doc.save(docx)#Salva o arquivo no diretório raiz onde está o arquivo
    print(f"Arquivo .docx criado:{docx}")

#("arquivo em pdf", "arquivo docx salvo")
pdf_to_docx("Desafio.pdf", "gtil.docx")