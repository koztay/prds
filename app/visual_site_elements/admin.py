from django.contrib import admin
from django import forms
from .models import SliderImage, Testimonial


class SliderImageForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SliderImage
        fields = '__all__'


class SliderImageAdmin(admin.ModelAdmin):
    form = SliderImageForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'siralama']
    list_editable = ['siralama']

admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Testimonial)
