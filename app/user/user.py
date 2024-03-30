from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# own moduls
from app.user.serializers import UserSerializer
from .serializers import UserSerializer

# Register new user
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send email of new registration
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    
# User login
# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = None
#         if '@' in username:
#             try:
#                 user = User.objects.get(email=username)
#             except ObjectDoesNotExist:
#                 pass

#         if not user:
#             user = authenticate(username=username, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)

#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
