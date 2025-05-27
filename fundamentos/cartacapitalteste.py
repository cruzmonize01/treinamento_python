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
        infos_gerais = conteudo.find("div", attrs={"class": "s-content__infos"}).span.text.strip() #deu certo antes mas n quer dar agora
        print(infos_gerais)
        tag_lista_paragrafos= conteudo.find_all("div", attrs={"class": "content-closed contentOpen"})
        paragrafos=[]
        for tag in tag_lista_paragrafos:
                try:
                    paragrafo = tag.p.text.strip()
                    paragrafos.append(paragrafo)
                
                except AttributeError:
                    continue
        print(paragrafos)
        subtitulo=conteudo.find("div", attrs={"class":"content-closed contentOpen"} ).p.text.strip
        #print(subtitulo)
        print("#"*10)
        tag_lista_subtitulos=conteudo.find_all("div", attrs={"class": "content-closed contentOpen"})
        for tag in tag_lista_subtitulos:
                try:
                    subtitulo= tag.p.text.strip()
                    print(subtitulo)
                except AttributeError:
                    continue

    texto = infos_gerais[0].replace("Por\n", "Por ").strip()
    partes = [p.strip() for p in texto.split("\n") if p.strip()]
    print(f"\nPartes encontradas: {partes}")

    if len(partes) >= 2:
        autor = partes[0].replace("Por ", "")
        data = partes[1]
    else:
        print("❌ Não foi possível encontrar autor e data.")
        autor = None
        data = None
    
    
    
       
    print("#"*10)

def main():
    link = "https://www.cartacapital.com.br/mais-recentes/page/3"
    html = acessar_pagina(link)
    #print(html)
    extrair_infos(html)

if __name__ == "__main__":
 main()