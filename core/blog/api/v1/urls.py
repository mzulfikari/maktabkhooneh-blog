from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls


# urlpatterns = [
# path('post/',views.postlist,name="api-post-views"),
# path('post/<int:id>/',views.postDetail,name='post-detail')
# path('post/',views.PostList.as_view(),name="api-post-views"),
# path('post/<int:pk>/',views.PostDetail.as_view(),name="api-post-views"),
# path('post/',views.PostViewSet.as_view({'get':'list','post':'create'}),name="api-post-views"),
# path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name="api-post-views"),

# ]
