from django.contrib import admin
from .models import Institution

admin.site.register(Institution)

from .models import StudentApplication
admin.site.register(StudentApplication)
