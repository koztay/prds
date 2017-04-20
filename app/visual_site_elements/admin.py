from django.contrib import admin
from django import forms
from .models import SliderImage, SliderImageTextFields, Testimonial


class SliderImageForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SliderImage
        fields = '__all__'


class SiderImageTextInline(admin.TabularInline):
    model = SliderImageTextFields
    extra = 1
    ordering = ("siralama",)


class SliderImageAdmin(admin.ModelAdmin):
    inlines = [SiderImageTextInline, ]
    form = SliderImageForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'siralama']
    list_editable = ['siralama']

admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Testimonial)
