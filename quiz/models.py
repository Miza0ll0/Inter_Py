from django.db import models


class Question(models.Model):
    DIFFICULTY_CHOICES = [('easy', 'Facile'), ('medium', 'Moyen'), ('hard', 'Difficile')]
    
    text = models.TextField()
    choice_a = models.CharField(max_length=255)
    choice_b = models.CharField(max_length=255)
    choice_c = models.CharField(max_length=255, blank=True)
    choice_d = models.CharField(max_length=255, blank=True)
    CORRECT_CHOICES = [('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')]
    correct = models.CharField(max_length=1, choices=CORRECT_CHOICES)
    theme = models.CharField(max_length=100, blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    explanation = models.TextField(blank=True, help_text="Explication de la bonne réponse")

    def choices(self):
        # return list of tuples (key, label)
        items = [('a', self.choice_a), ('b', self.choice_b)]
        if self.choice_c:
            items.append(('c', self.choice_c))
        if self.choice_d:
            items.append(('d', self.choice_d))
        return items

    def __str__(self):
        return f"{self.text[:50]}..."
