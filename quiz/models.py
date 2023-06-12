from django.db import models
from course.models import Course
from myapp.models import User
import random
from event.models import Event
from django.db.models.signals import post_delete
from django.dispatch import receiver

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

# Crate a quiz models
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name}-{self.course}"

    # returns a list of questions associated with the quiz using reverse query
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]
    
    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        # Create an event for the quiz
        event = Event.objects.create(
            name=self.name,
            start=self.start_date,
            course=self.course,
            end=self.end_date
            )
        event.save()

    class Meta:
        verbose_name_plural = 'Quizes'
        
@receiver(post_delete, sender=Quiz)
def delete_associated_event(sender, instance, **kwargs):
    event = Event.objects.filter(name=instance.title).first()
    if event:
        event.delete()
        
# Create a question model
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

# create an answer model
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
    
# create a result model
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    completion_time = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    started = models.BooleanField(default=False)  # Track whether the quiz has started
    
    def __str__(self):
        return self.user.username