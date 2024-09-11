# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input('Quel est le nom de l\'athlète ? ')
date = input('Quelle est la date du record de l\'athlète ? ')
discipline = input('Quelle est la discipline de l\'athlète ? ')
categorie = input('Quelle est la catégorie de l\'athlète ? Veuillez inscrire nulle si l\'athlète en n\'a pas. ')
record = input('Quel est le record de l\'athlète ? ')
print('''
Nouveau Record:
--------------------''') 
print(date)
if categorie == 'nulle':
    print(discipline)
else:
    print(discipline + ' - ' + categorie)
print(athlete + ' ' + country + ' - ' + record)