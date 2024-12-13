from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from docx import Document


#Função para carregar o conteúdo de um arquivo .docx
def extraindo_texto(docx_path):
    doc = Document(docx_path)
    texto = ""
    for item in doc.paragraphs: #Percorrendo o texto de cada parágrafo
        texto += item.text + "\n" #Adicionando cada texto encontrado
    return texto

#Caminho para o arquivo .docx
docx_path = 'gtil.docx'

#Extraindo o texto do arquivo .docx
text = extraindo_texto(docx_path)

#Definindo a lista de stopwords
stopwords = set(STOPWORDS)

#Adicionando a lista vazia
novas_palavras = []

#Abrindo o arquivo stopword que possui o encoding utf8
with open("stopwords", 'r', encoding="utf8") as item:
    #for linha in item: Este laço percorre o arquivo linha por linha.
    #for word in linha.split(): para cada linha dividir em palavras.
    #new_words.append(word): para cada palavra encontrada adiciona na lista.
    [novas_palavras.append(word) for linha in item for word in linha.split()]

new_stopwords = stopwords.union(novas_palavras)

#Criando a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

#Exibindo a WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")#Não mostrar na Tela
plt.show()#mostra na tela