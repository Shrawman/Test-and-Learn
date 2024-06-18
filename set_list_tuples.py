cities = ["Mubmbai","Dhaka","New York"]
countries = ["India","Bangladesh","USA"]

cico = zip(cities,countries)
for i in cico:
    print(i)

d= {city: country for city,country in zip(cities,countries)}
print(d)
num = [2,4,5,7,8,9]
num_increment = set(i+1 for i in num)
num_square = [i*i for i in num]
print(num_square)
print(num_increment)