from django.contrib import admin
from .models import Blog
from .models import Profile
from .models import Sponsor
from .models import Events


# Register your models here.


admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Sponsor)
admin.site.register(Events)

