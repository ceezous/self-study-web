from django.urls import path
from . import views


# *** notes by crz at 2021-09-07 08:25 *** : Specify namespace.
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"), # *** notes by crz at 2021-09-07 08:41 *** : name是为了让template中的对象逆向路由
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]