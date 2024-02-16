from django.contrib import admin
from AppKF.models import *
from django.contrib import admin
from django.contrib.auth.models import User 
from AppKF.views import *
from AppKF.forms import *
# Register your models here.


admin.site.register(Vinoteca)
admin.site.register(Cafeteria)
admin.site.register(Heladeria)
admin.site.register(Curso)
admin.site.register(Avatar)
