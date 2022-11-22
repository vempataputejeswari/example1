from django.urls import path
from Crudapp.views import book
from . import views
urlpatterns = [
    path('', views.index, name = 'python'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_summary>', views.delete_book),
]