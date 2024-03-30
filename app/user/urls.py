from rest_framework.routers import DefaultRouter
from app.user.views import UserViewset
from app.user.user import register_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

router = DefaultRouter() # Viewset
router.register('user', UserViewset, basename='user')

urlpatterns = [
    path('register/', register_user, name = 'register')
]

# Agrega las rutas generadas por el enrutador al urlpatterns
urlpatterns += router.urls
# urlpatterns = [
#   path('user', UserViewset, name = 'user'),
#   path('register/', register_user, name = 'register'),
  
#   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#   # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
'''
path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
     
'''
