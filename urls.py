from django.conf.urls import url
from . import views
from .views import creerVueAppelParticulier, creerVueEtudiant, modifierVueEtudiant

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<cursus_id>[0-9]+)$', views.detailCursus, name='detailCursus'),
  url(r'^student/create/$', creerVueEtudiant.as_view(), name="creerVueEtudiant"),
  url(r'^call/particular/$', views.appelParticulier, name='appelParticulier'),
  url(r'^student/(?P<student_id>[0-9]+)$', views.detailEtudiant, name='detailEtudiant'),
  url(r'^student/edit/(?P<student_id>\d+)/$', modifierVueEtudiant.as_view(), name='modifierVueEtudiant'),
  url(r'^particularCall/$', creerVueAppelParticulier.as_view(), name='creerVueAppelParticulier'),
  url(r'^absence/(?P<cursus_id>[0-9]+)/$', views.absense, name="absence"),
  url(r'^absence/(?P<cursus_id>[0-9]+)/(?P<student_id>\d+)/$', views.visualiserAbsences, name="visualiserAbsences"),
]