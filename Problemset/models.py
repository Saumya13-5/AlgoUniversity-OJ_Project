from tkinter import CASCADE
from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Testcase(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    input = models.TextField()
    expected_output = models.TextField()
