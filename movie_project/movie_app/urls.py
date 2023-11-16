from .import views
from django.urls import path
app_name='movie_app'
urlpatterns = [
    path('',views.movie_first_fun,name='movie_first_fun'),
    path('<int:movie_id>/',views.detail_view,name='detail_view'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
