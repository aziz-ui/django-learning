from django.conf.urls import url 

from . import views

app_name = 'core'
urlpatterns = [
    url('movies',
         views.MovieList.as_view(),
         name='MovieList'),
    url('movie/<int:pk>',
        views.MovieDetail.as_view(),
        name='MovieDetail'),
]
