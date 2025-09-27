from django.urls import path,include
from . import views


app_name = "api-v1"

urlpatterns = [  
    path('post/',views.postlist,name="api-post-views"),
    path('post/<int:id>/',views.postDetail,name='post-detail')
   

]
