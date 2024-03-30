from rest_framework import serializers
from app.user.models import User

class UserSerializer(serializers.ModelSerializer):
  
  password_confirmation = serializers.CharField(style={"input_type": "password"}, write_only = True)
  
  class Meta:
    model = User
    # qué campos y en qué orden quiero ver
    fields = ["id", "username", "email", "password", "password_confirmation"]
    extra_kwargs = {'password': {'write_only': True}}
    
  def save(self):
      user = User(
          username=self.validated_data['username'],
          email=self.validated_data['email']
      )
      password = self.validated_data['password']
      password_confirmation = self.validated_data['password_confirmation']
      if password != password_confirmation:
        raise serializers.ValidationError({'password': 'Passwords must match'})
      user.set_password(password) # Encripta contraseña
      user.save()
      return user
