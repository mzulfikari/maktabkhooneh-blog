from django.urls import path, include
from . import views


app_name = "blog"

urlpatterns = [
    path("cbv-index", views.Index.as_view(), name="cbv-index"),
    path("posts/", views.Posts.as_view(), name="post-list"),
    path(
        "go-to-maktbkhooneh",
        views.RedirectMaktanKhoneh.as_view(),
        name="redirect-maktbkhooneh",
    ),
    path("posts/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    # path('posts/create-form/',views.PostForm.as_view(),name="post-create-form"),
    path("posts/create-view/", views.PostCreated.as_view(), name="post-create-view"),
    path("posts/<int:pk>/edit/", views.PostEdit.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", views.PostDelete.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
