import requests
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    #estado
    print(r.status_code)
    #saber la respuesta
    print(r.text)
    print(type(r.text))
    #lo convierte a JSON
    categories = r.json()
    for category in categories:
        print(category['name'])

    
