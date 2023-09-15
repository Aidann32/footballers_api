from django.contrib import admin

from .models import Country, FootballClub, Footballer


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(FootballClub)
class FootballClubAdmin(admin.ModelAdmin):
    pass


@admin.register(Footballer)
class FootballerAdmin(admin.ModelAdmin):
    pass

