from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('create', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/delete', views.blogDelete, name='delete'),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('/create/', views.CreateView.as_view(), name='create'),
    # path('<int:blog_id>/edit/', views.EditView.as_view(), name='edit'),
    # path('<int:blog_id>/update', views.update, name='update'),
]
