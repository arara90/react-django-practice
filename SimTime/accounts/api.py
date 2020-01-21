from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # save user into db

        [_, token] = AuthToken.objects.create(user)  # Tuple을 return하기 때문에

        # response back
        return Response({
            "user": UserSerializer(
                user,  # pass user object
                context=self.get_serializer_context()
            ).data,

            # Token은 Header에 담기게되고, 이를 활용해서 user를 식별,인증함
            "token": token
        })
# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        [_, token] = AuthToken.objects.create(user)  # Tuple을 return하기 때문에

        # response back
        return Response({
            "user": UserSerializer(
                user,  # pass user object
                context=self.get_serializer_context()
            ).data,

            # Token은 Header에 담기게되고, 이를 활용해서 user를 식별,인증함
            "token": token
        })





# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
