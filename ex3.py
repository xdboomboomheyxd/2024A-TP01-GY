# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
speed = float(input('Quelle est la vitesse initiale de la boulle ? '))
angle = float(input('Quelle est l\'angle de lancement de la boule ? '))
distance = ((speed**2)*(math.sin(2*math.radians(angle))))/9.8
print('La distance maximale en x est de '+ str(round(distance, 2)) + 'm')