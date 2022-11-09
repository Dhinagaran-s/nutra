from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from nutra.settings import BASE_DIR

from nutra_app.models import CustomUser
from .serializers import RegisterApiUsersUser







@api_view(['POST'])
def register_api_user(request):

    serializer = RegisterApiUsersUser(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'Successfully registered a new Public User'
        data['email'] = account.email
        data['username'] = account.username
        # data['token'] = Token.objects.get(user=account).key
    else:
        data = serializer.errors
    return Response(data)




