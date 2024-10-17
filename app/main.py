
'''data = [
    {
        'Country': 'Ecuador',
        'Population': 140
    },
    {
        'Country': 'Inglaterra',
        'Population': 650
    }
]

def run():
    keys, values = mod.get_population()
    print(keys, values)

    country = input('Type Country => ')
    result = mod.population_by_country(data, country)
    print(result)
'''
import mod
import read_csv
import charts
import pandas as pd

def run():
    '''
    data = read_csv.read_csv('data.csv')
    # Filtro por continente
    # data = list(filter(lambda item: item['Continent'] == 'South America', data))
    # % de Poblacion mundial
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_piechart(countries, percentages)
'''

    # Poblacion por años de un pais
    
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Europe']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_piechart(countries, percentages)

    data = read_csv.read_csv('data.csv')
    country = input('Type Country => ')
    print(country)
    result = mod.population_by_country(data, country)
    print(result)
    if len(result) > 0:
         country = result[0]
         labels, values = mod.get_populationcsv(country)
         charts.generate_barchart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()
