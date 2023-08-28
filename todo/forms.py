from django.contrib.auth.forms import UserCreationForm,User

class RegistraionForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']
