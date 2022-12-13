from rest_framework import viewsets
from lab3_app.serializers import *
from lab3_app.models import Game, Publishers, Developers, Genre, Users
from rest_framework import generics, filters, permissions
from rest_framework.views import APIView, Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


class IsExecutor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Game.objects.select_related('publisher').all()
    serializer_class = GameSerializer  # Сериализатор для модели
    permission_classes = (IsExecutor,)


class PubViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Publishers.objects.all().order_by('id')
    serializer_class = PubSerializer  # Сериализатор для модели


class DevViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Developers.objects.all().order_by('id')
    serializer_class = DevSerializer  # Сериализатор для модели


class GameAPIView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Game.objects.filter()
    serializer_class = GameSearchSerializer

# select game.id, game.name, game.releaseDate, game.price, genre.name from game, game_genre, genre where game.id = game_genre.game_id and game_genre.genre_id = genre.id;


class GenViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenSerializer  # Сериализатор для модели


class GenApiView(generics.ListCreateAPIView):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Genre.objects.all()
    serializer_class = GenSearchSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Users.objects.all().order_by('pk')
    serializer_class = UserSerializer  # Сериализатор для модели


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        login = request.data['login']
        password = request.data['password']

        user = Users.objects.filter(login = login).first()

        if user is None:
            raise AuthenticationFailed('User not found.')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = Users.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response


class CartView(APIView):
    def post(self, request):
        serializer = CartSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CartViewSet(generics.ListCreateAPIView):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    search_fields = ['user_id__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['login'] = user.login
        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
