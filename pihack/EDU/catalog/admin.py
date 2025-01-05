from django.contrib import admin # type: ignore
from .models import catalog, Subject

admin.site.register(catalog)
admin.site.register(Subject)

