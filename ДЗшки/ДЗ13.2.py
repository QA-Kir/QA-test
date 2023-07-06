#1 case
my_string = 'Programming in Python'
print(my_string[::2])

#2 case
num_sequence = '9876543210'
print(num_sequence[::-3])

#3 case (v1)
first_image = 'summer_vacation.jpg'
second_image = 'winter_snowfall.png'
fact_1 = f'Файл имеет расширение {first_image[15:]}'
fact_2 = f'Файл имеет расширение {second_image[15:]}'
print(fact_1)
print(fact_2)

#3 case (v2)
first_image = 'summer_vacation.jpg'
second_image = 'winter_snowfall.png'
ext_1 = first_image.split('summer_vacation')[-1]
ext_2 = second_image.split('winter_snowfall')[-1]
fact_1 = f'Файл имеет расширение {ext_1}'
fact_2 = f'Файл имеет расширение {ext_2}'
print(fact_1)
print(fact_2)

#4 case
vehicle1 = 'Tesla Model 3'
vehicle2 = 'Ford Mustang'
tesla_cost_rub = 5500000
ford_cost_rub = 7500000
usd_per_rub = 82
tesla_cost_usd = round(tesla_cost_rub / usd_per_rub,2)
ford_cost_usd = round(ford_cost_rub / usd_per_rub,2)
print(f'The price of {vehicle1} in dollars is {tesla_cost_usd}')
print(f'The price of {vehicle2} in dollars is {ford_cost_usd}')

#5 case (v1)
web_address = 'https://www.wikipedia.org/wiki/Python_(programming_language)'
path =  web_address.split('.org')[-1]
print(path)

#5 case (v2)
web_address = 'https://www.wikipedia.org/wiki/Python_(programming_language)'
path =  web_address[25:]
print(path)