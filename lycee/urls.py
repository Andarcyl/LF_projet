from django.conf.urls import url
from . import views
from .views import creerEtudiant, modifierEtudiant, creerAppelParticulier

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<cursus_id>[0-9]+)$', views.detailCursus, name='detailCursus'),
  url(r'^student/create/$', creerEtudiant.as_view(), name="creerEtudiant"),
  url(r'^call/particular/$', views.appelParticulier, name='appelParticulier'),
  url(r'^student/(?P<student_id>[0-9]+)$', views.detailEtudiant, name='detailEtudiant'),
  url(r'^student/edit/(?P<student_id>\d+)/$', modifierEtudiant.as_view(), name='modifierEtudiant'),
  url(r'^particularCall/$', creerAppelParticulier.as_view(), name='creerAppelParticulier'),
  url(r'^absence/(?P<cursus_id>[0-9]+)/$', views.absence, name="absence"),
  url(r'^absence/(?P<cursus_id>[0-9]+)/(?P<student_id>\d+)/$', views.visualiserAbsences, name="visualiserAbsences"),
]