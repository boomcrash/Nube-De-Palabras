from wordcloud import WordCloud, STOPWORDS
import os
comentarios=''
stopwords=set(STOPWORDS)
direccion=os.getcwd()
file=open(direccion+'\\desktop\\proyectos\\nube de palabras\\file.txt',"r+")
textdata=file.read().replace('\n','')
wordcloud=WordCloud(width=500,height=500,background_color='white',stopwords=stopwords,min_font_size=10).generate(textdata)
wordcloud.to_file(direccion+'\\desktop\\proyectos\\nube de palabras\\Image.png')
print("se guardo la imagen")
