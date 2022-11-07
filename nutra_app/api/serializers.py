from rest_framework import serializers
from nutra_app.models import CustomUser, AdminUser, DeveloperUser, ApiUsersUser



class RegisterApiUsersUser(serializers.ModelSerializer):

    password_2 = serializers.CharField(style={'input_type':'password_2'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','username','password','password_2','user_type']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        api_user = CustomUser(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            user_type = 3
        )

        password = self.validated_data['password']
        password_2 = self.validated_data['password_2']

        if password != password_2:
            raise serializers.ValidationError({'password':'Password must match'})
        api_user.set_password(password)
        api_user.save()
        return api_user


















