from wordcloud import WordCloud
import matplotlib.pyplot as plt

#texto para gerar o WordCloud
texto = "Python é uma linguagem de programação popular para análise de dados, ciência de dados e inteligência artificial. Python é fácil de aprender e usar"

#Criando a nuvem de palavras
nuvem = WordCloud(width=800, height=400, background_color="white").generate(texto)#Criando a nuvem

#Criando e exibindo a nuvem de palavras (matplotlib)
plt.figure(figsize=(10, 5))
#Interpolation='bilinear':suaviza a imagem
plt.imshow(nuvem, interpolation='bilinear')
#Axis off: remove os eixos(caso tivesse X e Y)
plt.axis("off")#Não mostrar na Tela
plt.show()#mostra na tela







