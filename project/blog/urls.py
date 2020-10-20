from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.Post_list_view),
    path('tag/<slug:tag_slug>/', views.Post_list_view, name='post_list_by_tag_name'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name = 'post_detail'),
    #path('<int:id>/share/',views.mail_send),
    ]