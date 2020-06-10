from django.contrib import admin

from .models import *
from employer.models import Article
admin.site.register(Article)
