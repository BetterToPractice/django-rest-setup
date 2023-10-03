from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader


class BaseMailTemplate:
    subject_template_name = ""
    body_template_name = ""
    body_html_template_name = ""
    default_sender = settings.EMAIL_DEFAULT_SENDER

    def get_default_sender(self):
        return self.default_sender

    def get_subject(self, context=None):
        return "".join(
            loader.render_to_string(self.subject_template_name, context or {}).splitlines()
        )

    def get_body(self, context=None, is_html_template=False):
        body_template = (
            self.body_html_template_name if is_html_template else self.body_template_name
        )
        return loader.render_to_string(body_template, context or {})

    def send(self, receiver, sender=None, context=None):
        email_message = EmailMultiAlternatives(
            self.get_subject(context),
            self.get_body(context),
            sender if sender else self.get_default_sender(),
            [receiver] if isinstance(receiver, str) else receiver,
        )
        html_email = self.get_body(context, is_html_template=True)
        email_message.attach_alternative(html_email, "text/html")
        email_message.send()
