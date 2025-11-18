import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizsite.settings')
django.setup()

from quiz.models import Question

# Questions variées avec explications
questions_data = [
    # Géographie
    {'text': 'Quelle est la capitale de la France?', 'choice_a': 'Paris', 'choice_b': 'Lyon', 'choice_c': 'Marseille', 'choice_d': 'Nice', 'correct': 'a', 'theme': 'Géographie', 'difficulty': 'easy', 'explanation': 'Paris est la capitale et la plus grande ville de France.'},
    {'text': 'Quel est le plus grand océan du monde?', 'choice_a': 'Océan Atlantique', 'choice_b': 'Océan Pacifique', 'choice_c': 'Océan Indien', 'choice_d': 'Océan Arctique', 'correct': 'b', 'theme': 'Géographie', 'difficulty': 'easy', 'explanation': 'L\'océan Pacifique couvre environ 165 millions de km².'},
    {'text': 'Quel est le plus haut sommet du monde?', 'choice_a': 'K2', 'choice_b': 'Mont Blanc', 'choice_c': 'Mont Everest', 'choice_d': 'Denali', 'correct': 'c', 'theme': 'Géographie', 'difficulty': 'easy', 'explanation': 'Le Mont Everest atteint 8 848 mètres d\'altitude.'},
    {'text': 'Combien de continents y a-t-il?', 'choice_a': '5', 'choice_b': '6', 'choice_c': '7', 'choice_d': '8', 'correct': 'c', 'theme': 'Géographie', 'difficulty': 'medium', 'explanation': 'Il existe 7 continents: Afrique, Amérique du Nord, Amérique du Sud, Antarctique, Asie, Europe et Océanie.'},
    {'text': 'Quel est le plus grand désert du monde?', 'choice_a': 'Désert de Mojave', 'choice_b': 'Désert du Sahara', 'choice_c': 'Désert de Gobi', 'choice_d': 'Désert de l\'Atacama', 'correct': 'b', 'theme': 'Géographie', 'difficulty': 'medium', 'explanation': 'Le Sahara est le plus grand désert chaud avec 9 millions de km².'},
    {'text': 'Quel fleuve est le plus long du monde?', 'choice_a': 'Fleuve Amazone', 'choice_b': 'Fleuve Nil', 'choice_c': 'Fleuve Yangtze', 'choice_d': 'Fleuve Mississippi', 'correct': 'b', 'theme': 'Géographie', 'difficulty': 'medium', 'explanation': 'Le Nil est le plus long fleuve du monde avec environ 6 650 km.'},
    {'text': 'Quelle est la capitale du Japon?', 'choice_a': 'Osaka', 'choice_b': 'Kyoto', 'choice_c': 'Tokyo', 'choice_d': 'Yokohama', 'correct': 'c', 'theme': 'Géographie', 'difficulty': 'easy', 'explanation': 'Tokyo est la capitale du Japon et une des plus grandes métropoles du monde.'},
    
    # Histoire
    {'text': 'En quelle année l\'homme a-t-il marché sur la Lune?', 'choice_a': '1965', 'choice_b': '1969', 'choice_c': '1971', 'choice_d': '1973', 'correct': 'b', 'theme': 'Histoire', 'difficulty': 'medium', 'explanation': 'Neil Armstrong a marché sur la Lune le 20 juillet 1969.'},
    {'text': 'En quelle année la Bastille a-t-elle été prise?', 'choice_a': '1787', 'choice_b': '1789', 'choice_c': '1791', 'choice_d': '1793', 'correct': 'b', 'theme': 'Histoire', 'difficulty': 'easy', 'explanation': 'La Bastille a été prise le 14 juillet 1789, marquant le début de la Révolution française.'},
    {'text': 'Qui a découvert l\'Amérique?', 'choice_a': 'Vasco de Gama', 'choice_b': 'Christophe Colomb', 'choice_c': 'Ferdinand Magellan', 'choice_d': 'Bartolomeu Dias', 'correct': 'b', 'theme': 'Histoire', 'difficulty': 'easy', 'explanation': 'Christophe Colomb a atteint les Amériques en 1492.'},
    {'text': 'En quelle année la Seconde Guerre mondiale a-t-elle terminé?', 'choice_a': '1943', 'choice_b': '1944', 'choice_c': '1945', 'choice_d': '1946', 'correct': 'c', 'theme': 'Histoire', 'difficulty': 'medium', 'explanation': 'La Seconde Guerre mondiale s\'est terminée le 2 septembre 1945 avec la reddition du Japon.'},
    {'text': 'Qui était le premier président des États-Unis?', 'choice_a': 'Thomas Jefferson', 'choice_b': 'George Washington', 'choice_c': 'John Adams', 'choice_d': 'James Madison', 'correct': 'b', 'theme': 'Histoire', 'difficulty': 'easy', 'explanation': 'George Washington a été le premier président des États-Unis (1789-1797).'},
    {'text': 'L\'empire romain a connu sa chute en?', 'choice_a': '376 AD', 'choice_b': '410 AD', 'choice_c': '476 AD', 'choice_d': '526 AD', 'correct': 'c', 'theme': 'Histoire', 'difficulty': 'hard', 'explanation': 'L\'Empire romain d\'Occident s\'est effondré en 476 AD quand Romulus Augustulus a été déposé.'},
    
    # Science
    {'text': 'Quelle est la vitesse de la lumière?', 'choice_a': '150,000 km/s', 'choice_b': '200,000 km/s', 'choice_c': '300,000 km/s', 'choice_d': '400,000 km/s', 'correct': 'c', 'theme': 'Science', 'difficulty': 'medium', 'explanation': 'La vitesse de la lumière est d\'environ 299,792 km/s, soit environ 300,000 km/s.'},
    {'text': 'Quel élément chimique a le symbole Au?', 'choice_a': 'Argent', 'choice_b': 'Or', 'choice_c': 'Aluminium', 'choice_d': 'Arsenic', 'correct': 'b', 'theme': 'Science', 'difficulty': 'easy', 'explanation': 'Au est le symbole de l\'or (du latin "aurum").'},
    {'text': 'Quel est le gaz le plus abondant dans l\'atmosphère?', 'choice_a': 'Oxygène', 'choice_b': 'Dioxyde de carbone', 'choice_c': 'Azote', 'choice_d': 'Hydrogène', 'correct': 'c', 'theme': 'Science', 'difficulty': 'medium', 'explanation': 'L\'azote représente environ 78% de l\'atmosphère terrestre.'},
    {'text': 'Combien de chromosomes les humains ont-ils?', 'choice_a': '23', 'choice_b': '46', 'choice_c': '46 paires', 'choice_d': '23 paires', 'correct': 'b', 'theme': 'Science', 'difficulty': 'medium', 'explanation': 'Les humains ont 46 chromosomes (23 paires).'},
    {'text': 'Quel est le plus grand organe du corps humain?', 'choice_a': 'Cœur', 'choice_b': 'Poumons', 'choice_c': 'Peau', 'choice_d': 'Foie', 'correct': 'c', 'theme': 'Science', 'difficulty': 'hard', 'explanation': 'La peau est le plus grand organe du corps humain avec une surface d\'environ 2 m².'},
    {'text': 'En quelle année Einstein a-t-il publié la théorie de la relativité?', 'choice_a': '1895', 'choice_b': '1905', 'choice_c': '1915', 'choice_d': '1925', 'correct': 'b', 'theme': 'Science', 'difficulty': 'hard', 'explanation': 'Einstein a publié la théorie de la relativité restreinte en 1905.'},
    
    # Mathématiques
    {'text': 'Combien de côtés a un hexagone?', 'choice_a': '4', 'choice_b': '5', 'choice_c': '6', 'choice_d': '7', 'correct': 'c', 'theme': 'Mathématiques', 'difficulty': 'easy', 'explanation': 'Un hexagone a 6 côtés.'},
    {'text': 'Quel est le résultat de 15 × 12?', 'choice_a': '160', 'choice_b': '170', 'choice_c': '180', 'choice_d': '190', 'correct': 'c', 'theme': 'Mathématiques', 'difficulty': 'easy', 'explanation': '15 × 12 = 180.'},
    {'text': 'Quel est le chiffre romain pour 49?', 'choice_a': 'XLIX', 'choice_b': 'IL', 'choice_c': 'XDIX', 'choice_d': 'VIL', 'correct': 'a', 'theme': 'Mathématiques', 'difficulty': 'medium', 'explanation': '49 en chiffres romains est XLIX (40 + 9).'},
    {'text': 'Quelle est la racine carrée de 144?', 'choice_a': '10', 'choice_b': '11', 'choice_c': '12', 'choice_d': '13', 'correct': 'c', 'theme': 'Mathématiques', 'difficulty': 'easy', 'explanation': 'La racine carrée de 144 est 12 car 12 × 12 = 144.'},
    {'text': 'Quel est le nombre premier après 17?', 'choice_a': '18', 'choice_b': '19', 'choice_c': '20', 'choice_d': '21', 'correct': 'b', 'theme': 'Mathématiques', 'difficulty': 'medium', 'explanation': '19 est un nombre premier (seulement divisible par 1 et 19).'},
    
    # Biologie
    {'text': 'Quel est le plus grand mammifère du monde?', 'choice_a': 'Éléphant', 'choice_b': 'Girafe', 'choice_c': 'Baleine bleue', 'choice_d': 'Rhinocéros', 'correct': 'c', 'theme': 'Biologie', 'difficulty': 'easy', 'explanation': 'La baleine bleue est le plus grand animal du monde avec une longueur de 25 à 30 mètres.'},
    {'text': 'Combien de chambres a un cœur humain?', 'choice_a': '2', 'choice_b': '3', 'choice_c': '4', 'choice_d': '5', 'correct': 'c', 'theme': 'Biologie', 'difficulty': 'medium', 'explanation': 'Le cœur humain a 4 chambres: 2 oreillettes et 2 ventricules.'},
    {'text': 'Quel est le plus petit os du corps humain?', 'choice_a': 'Péroné', 'choice_b': 'Étrier', 'choice_c': 'Tibia', 'choice_d': 'Fémur', 'correct': 'b', 'theme': 'Biologie', 'difficulty': 'hard', 'explanation': 'L\'étrier (dans l\'oreille interne) est le plus petit os du corps humain, mesurant environ 2,8 mm.'},
    {'text': 'Combien de dents un adulte humain a-t-il normalement?', 'choice_a': '28', 'choice_b': '30', 'choice_c': '32', 'choice_d': '34', 'correct': 'c', 'theme': 'Biologie', 'difficulty': 'easy', 'explanation': 'Un adulte humain a normalement 32 dents.'},
    {'text': 'Quel type de sanguin est le plus rare?', 'choice_a': 'O-', 'choice_b': 'AB-', 'choice_c': 'A+', 'choice_d': 'B+', 'correct': 'b', 'theme': 'Biologie', 'difficulty': 'hard', 'explanation': 'Le type AB- est le plus rare, ne représentant qu\'environ 1% de la population.'},
    
    # Art & Culture
    {'text': 'Qui a peint la Joconde?', 'choice_a': 'Michel-Ange', 'choice_b': 'Léonard de Vinci', 'choice_c': 'Raphaël', 'choice_d': 'Botticelli', 'correct': 'b', 'theme': 'Art', 'difficulty': 'easy', 'explanation': 'Léonard de Vinci a peint la Joconde entre 1503 et 1519.'},
    {'text': 'En quelle année Van Gogh a-t-il peint "La Nuit étoilée"?', 'choice_a': '1885', 'choice_b': '1889', 'choice_c': '1893', 'choice_d': '1897', 'correct': 'b', 'theme': 'Art', 'difficulty': 'medium', 'explanation': 'Van Gogh a peint "La Nuit étoilée" en 1889.'},
    {'text': 'Quel compositeur a composé la "Symphonie n°9"?', 'choice_a': 'Mozart', 'choice_b': 'Beethoven', 'choice_c': 'Brahms', 'choice_d': 'Tchaikovsky', 'correct': 'b', 'theme': 'Art', 'difficulty': 'medium', 'explanation': 'Ludwig van Beethoven a composé la célèbre Symphonie n°9 avec "Ode à la Joie".'},
    {'text': 'Quel est le plus ancien sport olympique?', 'choice_a': 'Natation', 'choice_b': 'Lutte', 'choice_c': 'Course', 'choice_d': 'Équitation', 'correct': 'c', 'theme': 'Art', 'difficulty': 'hard', 'explanation': 'La course est le plus ancien sport olympique, disputé aux jeux olympiques anciens.'},
    
    # Technologie
    {'text': 'Qui a inventé l\'ampoule électrique?', 'choice_a': 'Thomas Edison', 'choice_b': 'Nicola Tesla', 'choice_c': 'Benjamin Franklin', 'choice_d': 'Michael Faraday', 'correct': 'a', 'theme': 'Technologie', 'difficulty': 'easy', 'explanation': 'Thomas Edison a développé la première ampoule incandescente pratique en 1879.'},
    {'text': 'En quelle année Internet a-t-il été créé?', 'choice_a': '1969', 'choice_b': '1979', 'choice_c': '1989', 'choice_d': '1999', 'correct': 'a', 'theme': 'Technologie', 'difficulty': 'medium', 'explanation': 'L\'ancêtre d\'Internet, ARPANET, a été créé en 1969.'},
    {'text': 'Quel est le langage de programmation le plus ancien encore utilisé?', 'choice_a': 'Python', 'choice_b': 'Java', 'choice_c': 'FORTRAN', 'choice_d': 'C', 'correct': 'c', 'theme': 'Technologie', 'difficulty': 'hard', 'explanation': 'FORTRAN (1957) est l\'un des plus anciens langages de programmation encore utilisés.'},
]

# Supprimer les anciennes questions pour éviter les doublons
Question.objects.all().delete()

# Créer les nouvelles questions
for q_data in questions_data:
    Question.objects.create(**q_data)

print(f"✓ {len(questions_data)} questions créées avec succès!")
print(f"  - Géographie: 7")
print(f"  - Histoire: 6")
print(f"  - Science: 6")
print(f"  - Mathématiques: 5")
print(f"  - Biologie: 5")
print(f"  - Art: 4")
print(f"  - Technologie: 3")
