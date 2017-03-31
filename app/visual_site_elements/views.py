from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import SliderImage


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def post(self, request, *args, **kwargs):
        print('I am posting...')
        context = self.get_context_data()
        if context["contact_form"].is_valid():
            print('yes done form is valid no we can send mail here')
            email = context["contact_form"].cleaned_data.get('email')
            name = context["contact_form"].cleaned_data.get('name')
            surname = context["contact_form"].cleaned_data.get('surname')
            message = context["contact_form"].cleaned_data.get('message')
            subject = 'Pureads Web Sitesi İletişim Formu ile Mesaj Gönderildi'
            from_email = 'noreply@pureads.com'
            to_email = ['neslihan@pureads.com', 'koztay@me.com']
            contact_message = '%s aşağıdaki mesajı gönderdi:\n\n %s\n\n Gönderen e-posta: %s' % (name, message, email)

            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=True)
            context['message'] = 'Mesajınız başarıyla gönderildi!'
            context['alert_type'] = 'alert-success'

        else:
            context['message'] = 'Hata! Lütfen bilgilerinizi kontrol edin.!'
            context['alert_type'] = 'alert-danger'

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        print('I am getting context')
        context = super(HomePageView, self).get_context_data(**kwargs)

        form = ContactForm(self.request.POST or None)  # instance= None
        sliders = SliderImage.objects.all().filter(active=True).order_by('siralama')
        context["contact_form"] = form
        context["sliders"] = sliders

        return context

