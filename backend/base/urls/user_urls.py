from django.urls import path
from base.views import user_views

urlpatterns = [
    path('login/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', user_views.UserRegisterAPIView.as_view(), name='register'),
    path('', user_views.UserAPIView.as_view(), name='users'),
    path('profile/', user_views.UserProfileAPIView.as_view(), name='user-profile'),
    path('profile/update/', user_views.UserProfileAPIView.as_view(), name='user-profile-update'),
]
