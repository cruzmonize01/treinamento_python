import httpx
from bs4 import BeautifulSoup

def acessar_pagina(link): 
    pagina = httpx.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser") 
    return bs 

def extrair_infos(html):
    tag_lista_noticias = html.find("section", attrs={"class": "l-list__list"}).find_all("a",attrs= {"class":"l-list__item"})
    print(f"quantas noticias encontrei? {len(tag_lista_noticias)}")
      
    for noticia in tag_lista_noticias:
        try:
            link = noticia["href"] 
        except:
            continue
        titulo = noticia.find("h2").text

        
        print(titulo)
        print(link)

    
        conteudo = acessar_pagina(link)
        autoria=conteudo.find("div", attrs={"class": "s-content__infos"}).a.text.strip()
        print(autoria)
        infos_gerais = infos_gerais.find("div", attrs={"class": "s-content__infos"}).span.text.strip()
        
        
        print("#"*10)

def main():
    link = "https://www.cartacapital.com.br/mais-recentes/page/3"
    html = acessar_pagina(link)
    #print(html)
    extrair_infos(html)

if __name__ == "__main__":
    main()