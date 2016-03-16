# coding=utf-8
from django import forms
from distribuidor.models import Pessoa, validate_cpf


class LoginForm(forms.Form):
    username = forms.CharField(label='CPF', required=False)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)


class PasswordResetForm(forms.Form):
    cpf = forms.CharField(label='CPF', required=True)
    email = forms.EmailField(label='E-mail', max_length=254)


class PasswordResetUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput, min_length=4, required=True)
    password2 = forms.CharField(label='Digite novamente a senha', widget=forms.PasswordInput, min_length=4, required=True)

    class Meta:
        model = Pessoa
        fields = ['password1', 'password2']

    def save(self, commit=False):
        pessoa = super(PasswordResetUserForm, self).save(commit=commit)
        pessoa.set_password(self.cleaned_data['password1'])
        pessoa.save()
        return pessoa

    def clean(self):
        cleaned_data = super(PasswordResetUserForm, self).clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            msg_pwd = 'As duas senhas não conferem!. Por favor, confira os dados digitados.'
            self._errors['password1'] = msg_pwd
            self._errors['password2'] = msg_pwd
            raise forms.ValidationError('As duas senhas não conferem!. Por favor, confira os dados digitados.')
        return cleaned_data


class PasswordChangeForm(forms.ModelForm):

    password_old = forms.CharField(label='Senha Atual', widget=forms.PasswordInput, min_length=4, required=True)
    password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput, min_length=4, required=True)
    password2 = forms.CharField(label='Digite novamente a senha', widget=forms.PasswordInput, min_length=4, required=True)

    class Meta:
        model = Pessoa
        fields = ['password_old', 'password1', 'password2']

    def save(self, commit=False):
        pessoa = super(PasswordChangeForm, self).save(commit=commit)
        pessoa.set_password(self.cleaned_data['password1'])
        pessoa.save()
        return pessoa

    def clean(self):
        cleaned_data = super(PasswordChangeForm, self).clean()
        user = super(PasswordChangeForm, self).save(commit=False)

        if not user.check_password(cleaned_data['password_old']):
            self._errors['password_old'] = 'Senha incorreta'
            raise forms.ValidationError('A senha atual esta incorreta! Por favor, tente novamente')

        if cleaned_data['password_old'] == cleaned_data['password1']:
            self._errors['password1'] = 'A Nova Senha de ser diferente da Senha Atual.'
            raise forms.ValidationError('A Nova Senha de ser diferente da Senha Atual. Por favor confira os dados digitados.')

        if cleaned_data['password1'] != cleaned_data['password2']:
            msg_pwd = 'As duas senhas não conferem!. Por favor, confira os dados digitados.'
            self._errors['password1'] = msg_pwd
            self._errors['password2'] = msg_pwd
            raise forms.ValidationError('As duas senhas não conferem!. Por favor, confira os dados digitados.')

        return cleaned_data


class PessoaForm(forms.ModelForm):
    first_name = forms.CharField(label='Primeiro Nome', required=True)
    last_name = forms.CharField(label='Sobrenome', required=True)
    email = forms.CharField(label='E-mail', required=True)


    class Meta:
        model = Pessoa
        fields = '__all__'

    def save(self, commit=False):
        pessoa = super(PessoaForm, self).save(commit=commit)
        if not pessoa.id:
            pessoa.set_password('zumbeats@'+pessoa.cpf[:3])
            pessoa.username = pessoa.cpf
        pessoa.save()

        return pessoa

    def clean(self):
        data = super(PessoaForm, self).clean()

        if not validate_cpf(data.get('cpf')):
            self._errors['cpf'] = u'CPF inválido'

        return data
