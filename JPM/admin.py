from django.contrib import admin
from .models import Technology, BlackBall, GStack, JobPost, HLF


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)    


class BlackBallAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GStackAdmin(admin.ModelAdmin):
    list_display = ('name','p')


class JobPostAdmin(admin.ModelAdmin):
    
    list_display = ('title','company_name','job_type','location','cp','created_at')


class HLFAdmin(admin.ModelAdmin):
    list_display = ('filter_name','filter_url','days')


admin.site.register(Technology, TechnologyAdmin)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(HLF, HLFAdmin)
admin.site.register(GStack, GStackAdmin)
admin.site.register(BlackBall, BlackBallAdmin)