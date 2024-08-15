import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#creando una instancia
app = FastAPI()

#sintaxis de decorador
@app.get("/")
def get_list():
    return [1,2,3]  

#Creando otra ruta
@app.get("/contact")
def get_list():
    return {'name' : 'Dens'}

#Creando otra ruta
@app.get("/html",response_class=HTMLResponse)
def get_list():
    #Aquí puedo incluir el renderizado de una pagina
    return """
        <h1>Encabezado 1 para pagina</h1>
        <p>Este es un parrafo para la pagina</p>
    """
#Guardamos y automáticamente tiene que recargar

def run():
    store.get_categories()

#Para correrlo como script
if __name__ == "__main__":
    run()  # run() es la función que se ejecuta cuando se corre el script
