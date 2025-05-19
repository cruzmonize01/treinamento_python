import httpx  # Importa a biblioteca httpx para realizar requisições web

from bs4 import BeautifulSoup  # Importa BeautifulSoup para analisar o HTML

def acessar_pagina(link): 
    pagina=httpx.get(link)
    bs=BeautifulSoup(pagina.text,"html.parser") 
    return bs 

def extrair_infos(html):
    tag_lista_noticias=html.find_all("div",attrs={"class":"td-module-meta-info"})
    print(tag_lista_noticias)
    for noticia in tag_lista_noticias:
    
        titulo= noticia.find("h3", attrs={"class": "entry-title td-module-title"}).text
        link=noticia.a["href"]
        data=noticia.time.text 
        print(titulo)
        print(link)
        print (data)
        conteudo=acessar_pagina(link)
        autoria=conteudo.find_all("strong")
        print(autoria)
        print ("###")


        conteudo = acessar_pagina(link)
    
        
        print(conteudo)
        
        try:
            autoria = conteudo.find_all("strong")[1].text
            print(autoria)
        except IndexError:
            print("Autoria não encontrada.")

def main():
    link="https://averdade.org.br/category/mulheres/"
    acessar=acessar_pagina(link)
    extrair=extrair_infos(acessar)
    #https://averdade.org.br/category/brasil/page/2/

if __name__ == "__main__":
    main()
