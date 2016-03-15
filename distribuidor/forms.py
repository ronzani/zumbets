from django import forms
from distribuidor.models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=False):
        pessoa = super(PessoaForm, self).save(commit=commit)
        pessoa.set_password(self.cleaned_data['password'])
        pessoa.save()

        return pessoa
