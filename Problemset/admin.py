from django.contrib import admin
from .models import Problem, Testcase  # Import your Problem model

admin.site.register(Problem)
admin.site.register(Testcase)