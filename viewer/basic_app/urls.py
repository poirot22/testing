from django.urls import path,re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="basic_app"

urlpatterns=[
    path('searchbar/',views.searchbar,name='searchbar'),
    re_path(r'^faculties$',views.FacultyListView.as_view(),name="list"),
    re_path(r'^(?P<pk>\d+)/$',views.FacultyDetailView.as_view(),name='detail'),
    re_path(r'^create/$',views.FacultyCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$',views.FacultyUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.FacultyDeleteView.as_view(),name='delete'),
    path('faculty_csv/',views.faculty_csv,name='faculty_csv'),

]
