# Exercise #1
# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]



new_places = list(filter(lambda x:x.strip() != "", places))

print(new_places)


# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]


author.sort(key = lambda name : name.lower().split()[-1])

print(author)
    
    



# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

new_places = list(map(lambda i : (i[0],i[1] * 9/5 + 32) ,places))
print(new_places)


# Exercise #4
# Create a generator function that individually returns each movie genre back from the list
def movies():
 genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]
 for movie in genres:
        yield movie
my_movies = movies()
for i in my_movies:
    print(i)




