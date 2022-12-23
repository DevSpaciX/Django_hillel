from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"groups", views.GroupListView, basename="groups")
router.register(r"teacher", views.TeacherListView, basename="teacher")
router.register(r"student", views.StudentListView, basename="student")

urlpatterns = [
    # path('groups/', views.GroupListView.as_view(), name='group_list')
    path("api-token/", obtain_auth_token, name="token")
] + router.urls
