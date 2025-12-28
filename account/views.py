from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView):

    def post(self, request):
        uid = request.data.get('uid')
        password = request.data.get('password')

        user = User.objects.filter(uid=uid).first()

        if not user or not user.check_password(password):
            return Response({"error": "Invalid UID or password"}, status=401)

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "uid": user.uid,
                "username": user.username,
                "role": user.role
            }
        })
