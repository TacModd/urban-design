from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
        # eg. /gallery/
        path('', views.index, name='index'),
        # eg. /gallery/5/
        path('<int:gallery_id>/', views.detail, name='detail'),
        # eg. /gallery/5/results/
        path('<int:gallery_id>/results/', views.results, name='results'),
        # eg. /gallery/5/vote/
        path('<int:gallery_id>/vote/', views.vote, name='vote')
]
