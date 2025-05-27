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
        tag_lista_paragrafos= conteudo.find_all("div", attrs={"class":"td_block_wrap tdb_single_content tdi_66 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})
        paragrafos=[]
        subtitulo= conteudo.find("div",attrs={"tdb-block-inner td-fix-index"})
        print(subtitulo)
        tag_lista_subtitulos=conteudo.find_all("div", attrs={"class": "tdb-block-inner td-fix-index"})
        for tag in tag_lista_subtitulos:
            try:
                subtitulo = tag.b.text.strip()
                print(subtitulo)
            except AttributeError:
                continue

        for tag in tag_lista_paragrafos:
                try:
                    paragrafo = tag.p.text.strip()
                    print(paragrafo)
                except AttributeError:
                    continue


        conteudo = acessar_pagina(link)
    
        
        print("#"*10)

        
        try:
            autoria = conteudo.find_all("strong")[1].text
            print(autoria)
        except IndexError:
            print("Autoria não encontrada.")



def main():
    link="https://averdade.org.br/category/internacional/"
    acessar=acessar_pagina(link)
    extrair=extrair_infos(acessar)
    #https://averdade.org.br/category/brasil/page/2/



     


if __name__ == "__main__":
    main()

