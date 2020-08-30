from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from .ModelesFormulaires import Cursus,Etudiant,Presence
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import Formulaires
from . import populate_Students3
import logging
from datetime import datetime

def index(request):
  listeCursus = Cursus.objects.order_by('name')
  template = loader.get_template('lycee/index.html')
  context = {
    'liste' : listeCursus
  }
  return HttpResponse(template.render(context,request))

def detailCursus(request, cursus_id):
  listeEtudiant = Etudiant.objects.filter(cursus=cursus_id)

  template = loader.get_template('lycee/cursus/detail.html')

  context = {
    'liste' : listeEtudiant,
    'cursus' : Cursus.objects.get(id=cursus_id)
  }
  return HttpResponse(template.render(context,request))

def appelParticulier(request):
  listeCursus = Cursus.objects.order_by('name')
  template = loader.get_template('lycee/student/formcall.html')
  context = {
    'liste' : listeCursus
  }
  return HttpResponse(template.render(context,request))

def detailEtudiant(request, student_id):
  listeEtudiant = Etudiant.objects.filter(id=student_id)

  template = loader.get_template('lycee/student/detail.html')

  context = {
    'liste' : listeEtudiant,
    'absence' : len(Presence.objects.filter(student=student_id))
  }
  return HttpResponse(template.render(context,request))

def absense(request, cursus_id):
  listeEtudiant = Etudiant.objects.filter(cursus=cursus_id).order_by('cursus')
  template = loader.get_template('lycee/presence/detail.html')
  context = {
    'listeEtudiant' : listeEtudiant,
    'cursus' : Cursus.objects.get(id=cursus_id)
  }
  return HttpResponse(template.render(context,request))

def visualiserAbsences(request, cursus_id, student_id):
  listePresence = Presence.objects.filter(student=student_id).order_by('date')
  lenght = len(listePresence)

  template = loader.get_template('lycee/presence/vizualize.html')
  context = {
    'student' : Etudiant.objects.get(id=student_id),
    'cursus' : Cursus.objects.get(id=cursus_id),
    'listePresence' : listePresence,
    'lenght' : lenght
  }
  return HttpResponse(template.render(context,request))


class creerVueAppelParticulier(CreateView):
  model = Presence
  form_class = Formulaires.FormulairePresence
  template_name = "lycee/presence/create.html" 
  
  def get_success_url(self):
    return reverse('index')

class creerVueEtudiant(CreateView):

  model = Etudiant
  form_class = Formulaires.FormulaireEtudiant
  template_name = "lycee/student/create.html" 
  
  def get_success_url(self):
    return reverse('detailEtudiant', args=(self.object.id,))

class modifierVueEtudiant(UpdateView):
  model = Etudiant
  form_class = Formulaires.FormulaireEtudiant
  template_name = "lycee/student/edit.html"
  
  def get_success_url(self):
    return reverse('detailEtudiant', args=(self.object.id,))