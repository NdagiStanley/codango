from django import forms

class EmailForm(forms.Form):
    
    email = forms.EmailField(label='Email', max_length=200, widget=forms.TextInput(attrs={
            "class": "",
            "placeholder": "Enter your email address"
        }))

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(label=_("Email"), max_length=254)

#     def save(self, domain_override=None,
#              subject_template_name='registration/password_reset_subject.txt',
#              email_template_name='registration/password_reset_email.html',
#              use_https=False, token_generator=default_token_generator,
#              from_email=None, request=None):
#         """
#         Generates a one-use only link for resetting password and sends to the
#         user.
#         """
#         from django.core.mail import send_mail
#         UserModel = get_user_model()
#         email = self.cleaned_data["email"]
#         active_users = UserModel._default_manager.filter(
#             email__iexact=email, is_active=True)
#         for user in active_users:
#             # Make sure that no email is sent to a user that actually has
#             # a password marked as unusable
#             if not user.has_usable_password():
#                 continue
#             if not domain_override:
#                 current_site = get_current_site(request)
#                 site_name = current_site.name
#                 domain = current_site.domain
#             else:
#                 site_name = domain = domain_override
#             c = {
#                 'email': user.email,
#                 'domain': domain,
#                 'site_name': site_name,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'user': user,
#                 'token': token_generator.make_token(user),
#                 'protocol': 'https' if use_https else 'http',
#             }
#             subject = loader.render_to_string(subject_template_name, c)
#             # Email subject *must not* contain newlines
#             subject = ''.join(subject.splitlines())
#             email = loader.render_to_string(email_template_name, c)
#             send_mail(subject, email, from_email, [user.email])
