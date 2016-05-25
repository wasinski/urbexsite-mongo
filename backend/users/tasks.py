from configuration.celery import app
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse


@app.task(name='email_confirmation')
def email_confirmation(user):
    url = reverse('activation', args=(user.activation_key,))
    email_subject = 'Account confirmation!'
    email_body = ('Thanks for signing up. To activate your account '
                  'click this link %s%s' % (settings.DOMAIN, url))
    email_from = settings.EMAILS['registration']
    send_mail(
        email_subject,
        email_body,
        email_from,
        [user.email],
        fail_silently=False
    )
