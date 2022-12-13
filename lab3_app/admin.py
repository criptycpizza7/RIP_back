from django.contrib import admin
from lab3_app.models import Game, Genre, Developers, Publishers, Users, Cart
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


@admin.register(Users)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'login', 'join_date')
    list_display_links = ('email',)

# Register your models here.


@admin.register(Cart)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'game_id')


@admin.register(Game)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Genre)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Developers)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Publishers)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('name', )
