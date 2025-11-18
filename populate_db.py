import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizsite.settings')
django.setup()

from quiz.models import Question

# Sample questions
questions_data = [
    {'text': 'Quelle est la capitale de la France?', 'choice_a': 'Paris', 'choice_b': 'Lyon', 'choice_c': 'Marseille', 'choice_d': 'Nice', 'correct': 'a', 'theme': 'Géographie'},
    {'text': 'Quel est le plus grand océan du monde?', 'choice_a': 'Océan Atlantique', 'choice_b': 'Océan Pacifique', 'choice_c': 'Océan Indien', 'choice_d': 'Océan Arctique', 'correct': 'b', 'theme': 'Géographie'},
    {'text': 'En quelle année l\'homme a-t-il marché sur la Lune?', 'choice_a': '1965', 'choice_b': '1969', 'choice_c': '1971', 'choice_d': '1973', 'correct': 'b', 'theme': 'Histoire'},
    {'text': 'Quel est le plus haut sommet du monde?', 'choice_a': 'K2', 'choice_b': 'Mont Blanc', 'choice_c': 'Mont Everest', 'choice_d': 'Denali', 'correct': 'c', 'theme': 'Géographie'},
    {'text': 'Combien de continents y a-t-il?', 'choice_a': '5', 'choice_b': '6', 'choice_c': '7', 'choice_d': '8', 'correct': 'c', 'theme': 'Géographie'},
    {'text': 'Quel est le plus grand désert du monde?', 'choice_a': 'Désert de Mojave', 'choice_b': 'Désert du Sahara', 'choice_c': 'Désert de Gobi', 'choice_d': 'Désert de l\'Atacama', 'correct': 'b', 'theme': 'Géographie'},
    {'text': 'Qui a peint la Joconde?', 'choice_a': 'Michel-Ange', 'choice_b': 'Léonard de Vinci', 'choice_c': 'Raphaël', 'choice_d': 'Botticelli', 'correct': 'b', 'theme': 'Art'},
    {'text': 'Quelle est la vitesse de la lumière?', 'choice_a': '150,000 km/s', 'choice_b': '200,000 km/s', 'choice_c': '300,000 km/s', 'choice_d': '400,000 km/s', 'correct': 'c', 'theme': 'Science'},
    {'text': 'Combien de côtés a un hexagone?', 'choice_a': '4', 'choice_b': '5', 'choice_c': '6', 'choice_d': '7', 'correct': 'c', 'theme': 'Mathématiques'},
    {'text': 'Quel est le plus grand mammifère du monde?', 'choice_a': 'Éléphant', 'choice_b': 'Girafe', 'choice_c': 'Baleine bleue', 'choice_d': 'Rhinocéros', 'correct': 'c', 'theme': 'Biologie'},
    {'text': 'En quelle année la Bastille a-t-elle été prise?', 'choice_a': '1787', 'choice_b': '1789', 'choice_c': '1791', 'choice_d': '1793', 'correct': 'b', 'theme': 'Histoire'},
    {'text': 'Quel élément chimique a le symbole Au?', 'choice_a': 'Argent', 'choice_b': 'Or', 'choice_c': 'Aluminium', 'choice_d': 'Arsenic', 'correct': 'b', 'theme': 'Science'},
]

for q_data in questions_data:
    Question.objects.create(**q_data)

print(f"✓ {len(questions_data)} questions créées avec succès!")
