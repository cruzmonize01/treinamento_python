import httpx
from bs4 import BeautifulSoup

def acessar_pagina(link): 
    pagina = httpx.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser") 
    return bs 

def extrair_infos(html):
    tag_lista_noticias = html.find("section", attrs={"class": "l-list__list"}).find_all("a")
    print(f"quantas noticias encontrei? {len(tag_lista_noticias)}")
    
    for noticia in tag_lista_noticias:
        titulo = noticia.find("h2").text
        tag= noticia.find("a")
        link = tag["href"] if tag else ("sem link")
        data = noticia.find("time").text.strip() 
        
        print(titulo)
        print(link)
        print(data)

        conteudo = acessar_pagina(link)

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
            print ("data não encontrada")

def main():
    link = "https://www.cartacapital.com.br/mais-recentes/page/2"
    html = acessar_pagina(link)
    extrair_infos(html)

if __name__ == "__main__":
    main()