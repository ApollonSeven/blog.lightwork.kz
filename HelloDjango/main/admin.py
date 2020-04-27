from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Articles, ArticleTags, Policy

class ArticlesAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'

class PolicyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(ArticleTags)