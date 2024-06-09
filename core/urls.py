from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='home'),
    path('book/<int:pk>',views.details_book),
    path('create-book',views.append_book),
    path('create-author',views.append_author),
    path('update-book/<int:pk>',views.update_book),
    path('delete-book/<int:pk>',views.delete_book),
]