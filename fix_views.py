#!/usr/bin/env python
import os

# Read the original file
with open(r'C:\Users\mgc\OneDrive\Desktop\SWENMY\accounts\views.py', 'r') as f:
    content = f.read()

# Replace the old function
old_func = "def forgotPassword(request):\n      return render(request, 'accounts/forgotPassword.html')"
new_func = """def forgot_password(request):
     if request.method == 'POST':
          email = request.POST.get('email')
          
          try:
               user = Account.objects.get(email=email)
               
               # Generate password reset token and UID
               current_site = get_current_site(request)
               mail_subject = 'Reset Your Password'
               message = render_to_string('accounts/reset_password_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
               })
               to_email = email
               send_email = EmailMessage(mail_subject, message, to=[to_email])
               send_email.send()
               messages.success(request, 'Password reset link has been sent to your email.')
               return redirect('login')
          except Account.DoesNotExist:
               messages.error(request, 'Email does not exist.')
               return redirect('forgot_password')
     
     return render(request, 'accounts/forgetPassword.html')"""

content = content.replace(old_func, new_func)

# Write back
with open(r'C:\Users\mgc\OneDrive\Desktop\SWENMY\accounts\views.py', 'w') as f:
    f.write(content)

print("views.py updated successfully!")
