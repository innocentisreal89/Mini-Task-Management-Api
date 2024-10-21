# from django.conf.urls import url 
from django.urls import path, include
from .views import (
   
    RegisterApiView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', RegisterApiView.as_view(), name='sign_up'),
    # path('users', UserListView.as_view(), name='user_list'),
    
]