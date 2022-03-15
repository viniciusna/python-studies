"""O enumerate() é um método que age sobre um dado interável, ele faz uma lista com tuplas
que contenham o índice e o valor daquele índice.
EX"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))         #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start=1)))        #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]