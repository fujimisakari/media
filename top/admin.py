from django.contrib import admin
from top.models import WhatNew

class WhatNewOptions(admin.ModelAdmin):
    list_display = ('regist_date', 'content',)
    ordering = ('-regist_date',)

admin.site.register(WhatNew, WhatNewOptions)
