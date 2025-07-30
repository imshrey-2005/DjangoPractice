# Django Forms App

This app provides a contact form feature for the WorldTour Django project.

## Features

- Home page view
- Contact form with name, email, and message fields
- Email sending simulation (prints to console)
- Success page after form submission

## File Structure

- `views.py` — View functions for home, contact, and success pages
- `forms.py` — Contains the `ContactForm` class
- `urls.py` — URL routing for the app
- `templates/forms/` — HTML templates for the app

## Usage

1. **Access the contact form:**  
   Visit `/contact/` to fill out and submit the form.

2. **Form submission:**  
   On valid submission, the form simulates sending an email and redirects to the success page.

3. **Templates:**  
   - `contact.html` renders the form.
   - `success.html` shows a confirmation message.

## Setup

- Ensure the app is included in your Django project's `INSTALLED_APPS`.
- Configure URLs in your main project to include the app's `urls.py`.
- Make sure your templates directory is set up correctly in Django settings.

## Notes

- The email sending is simulated with a print statement in `ContactForm.send_email()`.  
  For real email functionality, configure Django's email backend and update the method.

---
