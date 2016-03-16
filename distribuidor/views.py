# coding=utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import hashlib
from datetime import datetime

from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from distribuidor.forms import LoginForm, PasswordResetForm, PasswordResetUserForm, PasswordChangeForm
from distribuidor.models import Pessoa
from zumbets.settings import EMAIL_HOST_USER


def login_view(request):
    msg_error = None
    msg_sucess = None
    msg_reset = None

    if request.method == "POST":
        if request.POST.get('submit_reset', False):
            form_login = LoginForm()
            form_reset = PasswordResetForm(request.POST)
            if form_reset.is_valid():
                pessoa = Pessoa.objects.filter(username=form_reset.cleaned_data.get('cpf')).first()
                if pessoa:
                    if pessoa.email == form_reset.cleaned_data['email']:

                        hash_user = hashlib.sha256(str(pessoa.id) + datetime.now().strftime('%Y%m%d'))
                        link = 'http://localhost:8001/pwd_reset/' + pessoa.username + '/' + hash_user.hexdigest()

                        pagina = render_to_string('email_reset_password.html',
                                                  {'frase': 'Clique aqui para redefinir sua senha','link': link})

                        if pessoa.email:
                            send_mail('Redefinição de senha CCZ', strip_tags(pagina), EMAIL_HOST_USER,
                                      [pessoa.email], fail_silently=True, html_message=pagina)

                        msg_sucess = u'Foi um enviado um email, com instruções para redefinir sua senha.'
                    else:
                        msg_reset = u'E-mail informado não encontrado'
                else:
                    msg_reset = u'CPF não cadastrado'

        elif request.POST.get('submit_login', False):
            form_login = LoginForm(request.POST)
            form_reset = PasswordResetForm()
            if form_login.is_valid():
                try:
                    username = form_login.cleaned_data['username']
                    password = form_login.cleaned_data['password']

                    user_authenticated = authenticate(username=username, password=password)
                    if user_authenticated:
                        if user_authenticated.is_active:
                            login(request, user_authenticated)
                            page = request.GET.get('next')
                            if page:
                                return HttpResponseRedirect(page)
                            else:
                                return HttpResponseRedirect('/')
                        else:
                            msg_error = 'Usuário bloqueado, entre em contato com o CCZ'
                    else:
                        msg_error = 'Usuário ou senha incorretos'

                except:
                    msg_error = 'Erro no login, entre em contato com o CCZ'

        else:
            msg_error = 'Verifique os dados informados'
            form_login = LoginForm()
            form_reset = PasswordResetForm()
    else:
        logout(request)
        form_login = LoginForm()
        form_reset = PasswordResetForm()

    context = {'form': form_login,
               'form_reset': form_reset,
               'msg_error': msg_error,
               'msg_sucess': msg_sucess,
               'msg_reset': msg_reset
               }
    return render_to_response("login.html", context, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def password_user_reset(request, username, hash_val):
    pessoa = Pessoa.objects.filter(username=username).first()
    msg_erro = None
    form = None

    if pessoa:
        hash_user = hashlib.sha256(str(pessoa.id) + datetime.now().strftime('%Y%m%d'))
        if hash_val == hash_user.hexdigest():
            if request.method == "POST":
                form = PasswordResetUserForm(request.POST, request.FILES, instance=pessoa)
                if form.is_valid():
                    form.save()
                    return redirect('login')
            else:
                form = PasswordResetUserForm(instance=pessoa)
        else:
            msg_erro = 'A validação do link para redefinição de senha Falhou!'
    else:
        msg_erro = 'Usuario para redefinição de senha não encontrado!'

    return render_to_response('password_reset.html',
                              {'form': form, 'msg_erro': msg_erro, 'titulo': 'Redefinição de Senha'},
                              context_instance=RequestContext(request))


@login_required(login_url='/login')
def password_change(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        form = PasswordChangeForm(request.POST, request.FILES, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa_list')  # render_to_response("/index.html", {})
    else:
        form = PasswordChangeForm(instance=pessoa)
    return render_to_response('pessoa_password_change.html', {'form': form, 'titulo': 'Alterar Senha'},
                              context_instance=RequestContext(request))