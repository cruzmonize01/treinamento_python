import httpx
from bs4 import BeautifulSoup

def acessar_pagina(link): 
    pagina = httpx.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser") 
    return bs 
def extrair_conteudo(conteudo):
    #subtitulo
    subtitulo_tag = conteudo.find("h2")
    subtitulo = subtitulo_tag.text.strip() if subtitulo_tag else "subtitulo não encontrado"


    #corpo da materia
    corpo_tag=conteudo.find("div", class_="s-content__heading")
    if corpo_tag:
        paragrafos = corpo_tag.find_all ("p")
        corpo_texto = "/n".join( [ p.text.strip() for p in paragrafos ])
    else:
        corpo_texto = "Conteúdo não encontrado"

    #autoria
    try:
        autoria = conteudo.find_all("strong") [1].text.strip()
    except IndexError:
        autoria = "Autoria não encontrada"

    #data
    try:
        data = conteudo.find("time").text.strip()
    except IndexError:
        data =  "Data não encontrada"

def extrair_infos(html):
    tag_lista_noticias = html.find("section", attrs={"class": "l-list__list"}).find_all("a",attrs= {"class":"l-list__item"})
    print(f"quantas noticias encontrei? {len(tag_lista_noticias)}")
      
    for noticia in tag_lista_noticias:
        try:
            link = noticia["href"] 
        except:
            continue
        titulo = noticia.find("h2").text

        data = noticia.find ("span").text.strip() 
        
     
        
        print(titulo)
        print(link)
        print(data)





        conteudo = acessar_pagina(link)
    
        """
        print(conteudo)
        
        try:
            autoria = conteudo.find_all("strong")[1].text
            print(autoria)
        except IndexError:
            print("Autoria não encontrada.")
        
        print("###")
#agora adcionamos mais infos

        try:
            subtitulo = conteudo.find("h2").text.strip()
        except IndexError:
            print("subtitulo não encontrado")

        
        try:
            data =conteudo.find("time").text.strip()
        except IndexError:
            print ("data não encontrada")"""

def main():
    link = "https://www.cartacapital.com.br/mais-recentes/page/3"
    html = acessar_pagina(link)
    #print(html)
    extrair_infos(html)

if __name__ == "__main__":
    main()