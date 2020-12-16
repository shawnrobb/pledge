from django.urls import path

from .views import HomeView, UserPledgesView

urlpatterns = [
    path("pledges/<username>/", UserPledgesView.as_view(), name="user-pledges"),
    path("", HomeView.as_view(), name="home"),
]
