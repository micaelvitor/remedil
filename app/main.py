from typing import Optional

from fastapi import FastAPI

from bs4 import BeautifulSoup

import requests
app = FastAPI()





@app.get("/drogariasaopaulo")
async def root():
    listaprincipal= ["link","preco","titulo","categoria"]
    pagina=2
    contador=1
    while pagina<178: #178 gerais. conclusão dada por 8557 produtos e 48 por pagina

        testeurl= ("https://www.drogariasaopaulo.com.br/buscapagina?fq=C%3a%2f800%2f&PS=48&sl=727d3c85-e93a-42fd-bd7e-42dfd3978c22&cc=48&sm=0&PageNumber="+str(pagina))
        page = requests.get(testeurl)
        soup= BeautifulSoup(page.content,"html.parser")
        results = soup
        remedios = results.find_all("div",class_="descricao-prateleira")
        
        for remedio in remedios:
            try:
                link=(remedio.find("a", class_="collection-link"))['href']
                preco=remedio.find(class_="valor-por").getText().strip()
                titulo=(remedio.find(class_="collection-link")).getText()
                categoria="geral"
                listaremedio=[{'link':link,'preco':preco,'titulo':titulo,'categoria':categoria}]
                listaprincipal.extend(listaremedio)
            
            except:
                pass

                      
            contador=contador+1
            

        pagina=pagina+1
    return(listaprincipal)


@app.get("/drogariaspacheco")
async def root():
    
    listaprincipal= ["link","preco","titulo","categoria"]
    pagina=2
    contador=1
    while pagina<10: #178 gerais. conclusão dada por 8557 produtos e 48 por pagina

        testeurl= ("https://www.drogariaspacheco.com.br/buscapagina?fq=C%3a%2f800%2f&PS=48&sl=d3e0ddd8-cb3d-47a5-b619-6747a06b74ce&cc=48&sm=0&PageNumber="+str(pagina))
        page = requests.get(testeurl)
        soup= BeautifulSoup(page.content,"html.parser")
        results = soup
        remedios = results.find_all("div",class_="descricao-prateleira")
        
        for remedio in remedios:
            try:
                link=(remedio.find("a", class_="collection-link"))['href']
                preco=remedio.find(class_="valor-por").getText().strip()
                titulo=(remedio.find(class_="collection-link")).getText()
                categoria="geral"
                listaremedio=[{'link':link,'preco':preco,'titulo':titulo,'categoria':categoria}]
                listaprincipal.extend(listaremedio)
            
            except:
                pass # não faço ideia de oque faz cair nessa except mas da no mesmo

                      
            contador=contador+1
            

        pagina=pagina+1
    return(listaprincipal)


@app.get("/drogaraia")
def scraperaia(urlbase="https://www.drogaraia.com.br/medicamentos",maximodepaginas=10):
    

#definir url base e numero de paginas

        
    listaprincipal= []
    pagina=2
    contador=1

    while pagina<maximodepaginas: #778 geral, 64 com receita
        testeurl= ((urlbase)+".html?p="+str(pagina))
        page = requests.get(testeurl)
        results= BeautifulSoup(page.content,"html.parser")
        remedios = results.find_all("div",class_="container")
        

        for remedio in remedios:
            try:
                link=(remedio.find("a", class_="show-hover"))['href'] 
                preco=remedio.find(class_="price").getText().strip() 
                titulo=(remedio.find("a", class_="show-hover")).getText()
                categoria=urlbase.rsplit('/',1)[-1]
                listaremedio=[{'link':link,'preco':preco,'titulo':titulo,'categoria':categoria}]
                listaprincipal.extend(listaremedio)
            
            except:
                pass
                     
            contador=contador+1
            

        pagina=pagina+1
    return(listaprincipal)


@app.get("/drogaraia/medicamentos/monitores-e-testes/teste-de-controle-glicemicos")
def scraperaia2(urlbase="https://www.drogaraia.com.br/medicamentos/monitores-e-testes/teste-de-controle-glicemicos",maximodepaginas=10):
    

#definir url base e numero de paginas

        
    listaprincipal= []
    pagina=2
    contador=1

    while pagina<maximodepaginas: #778 geral, 64 com receita
        testeurl= ((urlbase)+".html?p="+str(pagina))
        page = requests.get(testeurl)
        results= BeautifulSoup(page.content,"html.parser")
        remedios = results.find_all("div",class_="container")
        

        for remedio in remedios:
            try:
                link=(remedio.find("a", class_="show-hover"))['href'] 
                preco=remedio.find(class_="price").getText().strip() 
                titulo=(remedio.find("a", class_="show-hover")).getText()
                categoria=urlbase.rsplit('/',1)[-1]
                listaremedio=[{'link':link,'preco':preco,'titulo':titulo,'categoria':categoria}]
                listaprincipal.extend(listaremedio)
            
            except:
                pass
                     
            contador=contador+1
            

        pagina=pagina+1
    return(listaprincipal)


@app.get("/")
def read_item():
    return {"hello world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
