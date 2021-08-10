from . import views
from django.urls import path, register_converter
from .converters import YearConverter, MonthConverter, DayConverter


register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = "instagram"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>", views.post_detail, name="post_detail"),
    path("archive/", views.post_archive, name="post_archive"),
    path("archive/<year:year>/", views.post_archive_year, name="post_archive_year"),
    path('new/', views.post_new, name='post_new'),
]
