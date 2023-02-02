from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(JobTitle)
admin.site.register(DaysOffTypes)
admin.site.register(Department)
admin.site.register(branches)
admin.site.register(DaysOff)
admin.site.register(management)
admin.site.register(equipment)
admin.site.register(weakly_leave)
admin.site.register(leave_request)
admin.site.register(yearly_leave)


# Register your models here.
