import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from spodaily_api import views
from spodaily_api.views import DeleteSessionView, DeleteActivityView, AddActivityView, ExerciseGuideView, MuscleView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', RedirectView.as_view(url='spodaily-api/login/', permanent=False)),
    path('spodaily-api/', include('django.contrib.auth.urls'), name='spodaily_login'),
    url(r'^spodaily-api/home/', views.Home.as_view(), name='home'),
    url(r'^spodaily-api/register/', views.register, name='register'),
    url(r'^spodaily-api/account/', views.account, name='account'),
    url(r'^spodaily-api/routine/', views.routine, name='routine'),
    url(r'^spodaily-api/session/', views.session, name='session'),
    url(r'^spodaily-api/add_session/', views.AddSessionView.as_view(), name='add_session'),
    path('spodaily-api/delete_session/<uuid:pk>/', DeleteSessionView.as_view(), name='delete_session'),
    path('spodaily-api/delete_activity/<uuid:pk>/', DeleteActivityView.as_view(), name='delete_activity'),
    path('spodaily-api/add_activity/<uuid:fk>/', AddActivityView.as_view(), name='add_activity'),
    url(r'^spodaily-api/exercise_guide/', ExerciseGuideView.as_view(), name='exercise_guide'),
    path('spodaily-api/muscle/<uuid:fk>/', MuscleView.as_view(), name='muscle'),
    url(r'^spodaily-api/contact/', views.contact, name='contact'),
    url(r'^spodaily-api/rule_of_use/', views.rules_of_use, name='rules_of_use'),
    path('__debug__/', include(debug_toolbar.urls)),
]
