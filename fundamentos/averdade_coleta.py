import httpx
from bs4 import BeautifulSoup
import os
import sys
from datetime import datetime
from dateutil import parser
import requests

DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
if NOME_PROJETO == "templates":
    from diretorios.diretorio import diretorios, diretorios_template 
else:
    from templates.diretorios.diretorio import diretorios, diretorios_template 
print(f'DIR PROJETO: {DIR_PROJETO}')
from templates.acesso_bd.inserir_bd import inserir_bd, inserir_bd_pdf
from templates.acesso_bd.metadados import obter_infos, dict_a_partir_chave
from templates.template_html.html_template import html_consultar_json
from templates.coleta.paginas import acessar_pagina, montar_links_paginacao_01
from templates.obter_locale import data_extenso
from templates.log_txt import log_txt

def extrair_infos(link_pagina, dados):

    #####
    # Extração das informações disponíveis na página web.
    #####
    link= "https://averdade.org.br/category/brasil/"
    pagina = acessar_pagina(link_pagina)
    bs = pagina[0]
    http_code = pagina[1]
    print(http_code)
    conteudo_noticia = acessar_pagina(link)[0]
    conteudo = acessar_pagina(link)  [0]
   
    tag_lista_noticias=bs.find_all("div",attrs={"class":"td-module-meta-info"})
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
        tag_lista_paragrafos = conteudo.find_all("div", attrs={"class": "tdb-block-inner td-fix-index"})
        paragrafos = []

        for bloco in tag_lista_paragrafos:
            paragrafos_bloco = bloco.find_all("p")
        for p in paragrafos_bloco:
            texto = p.get_text(strip=True)
        if texto:
            paragrafos.append(texto)

        subtitulo= conteudo.find("div",attrs={"tdb-block-inner td-fix-index"})
        print(subtitulo)
        paragrafos=[ ]
        tag_lista_subtitulos=conteudo.find_all("div", attrs={"class": "tdb-block-inner td-fix-index"})
        for tag in tag_lista_subtitulos:
            try:
                subtitulo = tag.get_text(strip=True)
                print(subtitulo)

            except AttributeError:
                continue

       



        
        print("#"*10)

        
        try:
            autoria = conteudo.find_all("strong")[1].text
            print(autoria)
        except IndexError:
            print("Autoria não encontrada.")
      
    

        #####
        # Inserção dos dados no banco:
        #####

    
        dados["env_dir_bd"] = dados["sigla"]
        data_arq = f"{data[-4:]}-{data[-7:-5]}" if data else "NA"
        nome_arq_bd = f"{dados['sigla']}-{data_arq}"

        dados["titulo"] = titulo
        dados["link"] = link
        dados["data"] = data
        dados["horario"] = horario
        dados["imagens"] = imagens
        dados["paragrafos"] = paragrafos
        dados["autoria"] = autoria
        dados["nome_arq_bd"] = nome_arq_bd

        inserir_bd(dados)


    print("#"*10)


def main():
    env_dir_bd =  "BD_JORNAL_BR_AVERDADE"  
    caminho_arquivo_json = "/home/nepps_monizegoncalves/codigo/newscloud/geral/metadados/INFOS_BD_MONIZE.json"  
    chaves_desejadas = [
        "page_final",
        "page_inicial",
        "intervalo",
        "url",
        "codigo_bd",
        "sigla",
        "origem",
        "tipo_dado",
        "pais",
        "classificado",
        "dir_bd",
        "dir_base",
    ]
    dados = obter_infos(caminho_arquivo_json, env_dir_bd, chaves_desejadas)
    url = dados["url"]
    page_final = dados["page_final"]
    page_inicio = dados["page_inicial"]
    intervalo = dados["intervalo"]
    dados = dict_a_partir_chave(dados)
    lista_url_paginacao = montar_links_paginacao_01(url, page_final, page_inicio, intervalo)

    for link_pagina in lista_url_paginacao:
        extrair_infos(link_pagina, dados)


if __name__=="__main__":
    main()