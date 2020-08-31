
from django.forms.models import ModelForm
from .models import Student, Presence

class FormulaireEtudiant(ModelForm):
  class Meta:
    model = Student
    fields = [
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    ]

class FormulairePresence(ModelForm):
  class Meta:
    model = Presence
    fields = [
      "reason",
      "isMissing",
      "date",
      "student",
    ]