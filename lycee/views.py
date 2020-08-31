from django.shortcuts import reverse
from django.template import loader
from django.http import HttpResponse
from .models import Cursus, Student, Presence
from .form import FormulaireEtudiant, FormulairePresence
from django.views.generic import CreateView, UpdateView




def index(request):
  listeCursus = Cursus.objects.order_by('name')
  #chargement du template
  template = loader.get_template('lycee/index.html')
  #contexte
  context = {
    'liste' : listeCursus
  }
  return HttpResponse(template.render(context,request))

def detailCursus(request, cursus_id):
  listeEtudiant = Student.objects.filter(cursus=cursus_id)

  template = loader.get_template('lycee/detailsCursus.html')

  context = {
    'liste' : listeEtudiant,
    'cursus' : Cursus.objects.get(id=cursus_id)
  }
  return HttpResponse(template.render(context,request))

def appelParticulier(request):
  listeCursus = Cursus.objects.order_by('name')
  #chargement du template
  template = loader.get_template('lycee/createCall.html')
  #contexte
  context = {
    'liste' : listeCursus
  }
  return HttpResponse(template.render(context,request))

def detailEtudiant(request, student_id):
  listeEtudiant = Student.objects.filter(id=student_id)

  template = loader.get_template('lycee/detailsStudent.html')

  context = {
    'liste' : listeEtudiant,
    'absence' : len(Presence.objects.filter(student=student_id))
  }
  return HttpResponse(template.render(context,request))

def absence(request, cursus_id):
  listeEtudiant = Student.objects.filter(cursus=cursus_id).order_by('cursus')
  template = loader.get_template('lycee/detailsAbsence.html')
  context = {
    'liste' : listeEtudiant,
    'cursus' : Cursus.objects.get(id=cursus_id)
  }
  return HttpResponse(template.render(context,request))

def visualiserAbsences(request, cursus_id, student_id):
  listePresence = Presence.objects.filter(student=student_id).order_by('date')
  lenght = len(listePresence)

  template = loader.get_template('lycee/visualizeAbsence.html')
  context = {
    'student' : Student.objects.get(id=student_id),
    'cursus' : Cursus.objects.get(id=cursus_id),
    'liste' : listePresence,
    'lenght' : lenght
  }
  return HttpResponse(template.render(context,request))


class creerAppelParticulier(CreateView):
  #le model au se refere cette view
  model = Presence
  #le formulaire associé (dans form.py)
  form_class = FormulairePresence
  #le nom du template
  template_name = "lycee/createPresence.html" 
  
  def get_success_url(self):
    return reverse('lycee/index')

class creerEtudiant(CreateView):

  #le model au se refere cette view
  model = Student
  #le formulaire associé (dans form.py)
  form_class = FormulaireEtudiant
  #le nom du template
  template_name = "lycee/createStudent.html" 
  
  def get_success_url(self):
    return reverse('lycee/detailEtudiant', args=(self.object.id,))

class modifierEtudiant(UpdateView):
  #le model au se refere cette view
  model = Student
  #le formulaire associé (dans form.py)
  form_class = FormulaireEtudiant
  #le nom du template
  template_name = "lycee/editStudent.html"
  
  def get_success_url(self):
    return reverse('lycee/detailEtudiant', args=(self.object.id,))





  
    
