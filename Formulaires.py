from django.forms.models import ModelForm
from .models import Student, Presence

class FormulaireEtudiant(ModelForm):
  class Meta:
    model = Student
    fields = [
      "firstName",
      "lastName",
      "dateOfBirth",
      "email",
      "phoneNumber",
      "comments",
      "cursus",
    ]

class FormulairePresence(ModelForm):
  class Meta:
    model = Presence
    fields = [
      "dateOfCall",
      "isMissing",
      "reason",
      "student",
      "start_time",
      "stop_time",
    ]