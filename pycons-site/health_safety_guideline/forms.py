"""
Forms and validation code for user registration.

Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.

"""
from django import forms

from registration.users import UserModel

# Third Parties
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_recaptcha.fields import ReCaptchaField


User = UserModel()


from .models import Health_Safety_Guideline

 


class Health_Safety_GuidelineForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Health_Safety_Guideline
        fields = ('title', 'health_safety_guideline', 'user',) 

    def __init__(self, *args, **kwargs):
        super(Health_Safety_GuidelineForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_Health_Safety_GuidelineForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('update', 'Health_Safety_Guideline '))

