import httpx  # Importa a biblioteca httpx para realizar requisições web

from bs4 import BeautifulSoup  # Importa BeautifulSoup para analisar o HTML

def acessar_pagina(link): 
    pagina=httpx.get(link)
    bs=BeautifulSoup(pagina.text,"html.parser") 
    return bs 

def extrair_infos(html):
    tag_lista_noticias=html.find_all("div",attrs={"class": "l-list__item"})
    print(tag_lista_noticias)
    for noticia in tag_lista_noticias:
    
        titulo= noticia.find("h2", attrs={"class": "l-list__item"}).text
        link=noticia.a["href"]
        data=noticia.time.text 
        print(titulo)
        print(link)
        print (data)
        conteudo=acessar_pagina(link)
        autoria=conteudo.find_all("strong")[1]
        print(autoria)
        print ("###")
def main():
    link="https://www.cartacapital.com.br/mais-recentes/page/2"
    acessar=acessar_pagina(link)
    extrair=extrair_infos(acessar)
    #https://www.cartacapital.com.br/sociedade/morre-maria-nice-miranda-primeira-defensora-publica-do-pais/

if __name__ == "__main__":
    main()
