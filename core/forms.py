from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'company', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
            'phone': forms.TextInput(attrs={'placeholder': '(555) 123-4567'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('email', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6'),
                Column('company', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'subject',
            Field('message', rows="4"),
            Submit('submit', 'Send Message', css_class='btn btn-primary btn-lg mt-4')
        )
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove all non-numeric characters
            phone = ''.join(filter(str.isdigit, phone))
            if len(phone) < 10:
                raise forms.ValidationError("Please enter a valid phone number.")
        return phone 