from lab3_app.models import Game, Publishers, Developers, Genre, Users, Cart
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Game
        # Поля, которые мы сериализуем
        fields = ["id", "name", "genre", "releasedate", "developer", "publisher", "price"]


class PubSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Publishers
        # Поля, которые мы сериализуем
        fields = ["id", "name"]


class DevSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Developers
        # Поля, которые мы сериализуем
        fields = ["id", "name"]


class GameSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', "name", 'genre', "releasedate", "publisher", "developer",  "price"]


class GenSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Genre
        # Поля, которые мы сериализуем
        fields = ["id", "name"]


class GenSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['pk', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Users
        # Поля, которые мы сериализуем
        fields = ["id", "login", "password", "email"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user_id', 'game_id']


'''class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ["login", "password", "email"]
        extra_kwargs = {
            'password' : 
        }
'''