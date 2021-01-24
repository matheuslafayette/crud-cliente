from django.urls import path
from .views import editList, editCreate, editDelete, editUpdate

from . import views

urlpatterns = [
    path('', editList.as_view(), name='edit_list'),
    path('create/', editCreate.as_view(), name='edit_create'),
    path('update/<int:pk>/', editUpdate.as_view(), name='edit_Update'),
    path('delete/<int:pk>/', editDelete.as_view(), name='edit_delete'),
]