#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.
country = input('Quel est le pays dont vous voulez les médailles classifiées ? ')
code_medals = input('Inserez la chaine de médailles concernées en majuscule: ')
gold_medals=0
silver_medals=0
bronze_medals=0
bad_input=False
for letter in code_medals:
    if letter != 'B' and letter != 'S' and letter != 'G':
        bad_input = True
        break
    else:
        pass

if bad_input == False:
    gold_medals = code_medals.count('G')
    silver_medals = code_medals.count('S')
    bronze_medals = code_medals.count('B')
    print('Médailles:')
    print('- Or: ' + str(gold_medals))
    print('- Argent: ' + str(silver_medals))
    print('- Bronze: ' + str(bronze_medals)) 
else:
    print('Veuillez entrer un code valide')
    

