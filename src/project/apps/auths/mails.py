from apps.core.mails import BaseMailTemplate


class RegisterMail(BaseMailTemplate):
    subject_template_name = "auths/mails/register_subject.txt"
    body_template_name = "auths/mails/register_body.txt"
    body_html_template_name = "auths/mails/register_body.html"


register_mail = RegisterMail()
