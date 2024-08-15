#trabajando con Módulos 
#mod.py es el modulo que se crea para definir un modulo (tiene una función)
import utils
import read_csv
import charts
import pandas as pd

def run():
  # data = read_csv.read_csv('data.csv')
  # data = list(filter(lambda item : item['Continent'] == 'South America',data))
  # countries = list(map(lambda x: x['Country'], data))
  # percentages = list(map(lambda x: x['World Population Percentage'], data))
  
  #con esto ahorramos el algoritmo de leer CSV del archivo
  df = pd.read_csv('data.csv')
  #Igual a la linea 10 pero cambiando de continente
  df = df[df['Continent'] == 'Africa']
  #Igual a linea 11
  countries = df['Country'].values
  #Igual a linea 12
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()