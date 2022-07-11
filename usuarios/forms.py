from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from usuarios.models import Personal

#creo usuario en consola
class FormaRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Personal
        fields = ('matricula',)

    def clean_email(self):
        matricula = self.cleaned_data.get('matricula')
        qs = Personal.objects.filter(matricula=matricula)
        if qs.exists():
            raise forms.ValidationError('Matricula ya registrada')
        return matricula

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

class AdminFormaCreacionUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Personal
        fields = ('matricula', 'nombre', 'apellido')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        usuario = super(AdminFormaCreacionUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario

class AdminFormaActualizar(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Personal
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']
