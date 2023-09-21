from django.contrib import admin

from .models import Country, FootballClub, Footballer, FootballerImage


class FootballerImageInline(admin.TabularInline):
    model = FootballerImage


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(FootballClub)
class FootballClubAdmin(admin.ModelAdmin):
    pass


@admin.register(Footballer)
class FootballerAdmin(admin.ModelAdmin):
    inlines = [FootballerImageInline,]

