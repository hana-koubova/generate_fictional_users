from faker import Faker
from faker.config import AVAILABLE_LOCALES
import pycountry
import pycountry_convert as pc
from pycountry_convert import country_alpha2_to_continent_code

fake = Faker()

country_codes = []
country_names = []
countries_dict = {
   'NA': {},
   'SA': {},
   'AS': {},
   'OC': {},
   'AF': {},
   'EU': {}
}

locales_codes = [local for local in AVAILABLE_LOCALES]
#print(locales_codes)

continents = {
    'NA': 'North America',
    'SA': 'South America', 
    'AS': 'Asia',
    'OC': 'Australia',
    'AF': 'Africa',
    'EU': 'Europe'
}

for locale in locales_codes:
  #print(locale)
  if '_' in locale:
    try:
        country_code = locale.split('_')[1]
        country_codes.append(country_code)

        #Get Country Name
        country = pycountry.countries.get(alpha_2=country_code)
        country_name = country.name
        country_names.append(country_name)

        #Get Country Continent
        continent_code = country_alpha2_to_continent_code(country_code)

        countries_dict[continent_code][country_code] = {'faker_code': locale,
                                    'name': country_name}
    except:
       continue



country_names_sorted = sorted(country_names)
#print(country_names_sorted)
#print(countries_dict)

