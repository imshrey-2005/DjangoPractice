from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Enter your name")
    email = forms.EmailField(label="Enter your email")
    message = forms.CharField(widget=forms.Textarea, label="Enter your message")

    def send_email(self):
        print(f"Sending email to {self.cleaned_data['email']}")
        print(f"Message: {self.cleaned_data['message']}")   