from django.conf.urls import url , path

from . import views

app_name = 'core'
urlpatterns = [
    url('movies',
         views.MovieList.as_view(),
         name='MovieList'),
    path('movie/<int:pk>',
        views.MovieDetail.as_view(),
        name='MovieDetail'),
]
