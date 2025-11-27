from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm
from .models import Grabber
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('grabber')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga automaticamente após criar
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('grabber')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados.')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def grabber_page(request):
    grabbers = Grabber.objects.all()
    
    # Formatar o JSON para exibição bonita
    for grabber in grabbers:
        grabber.grab = json.dumps(grabber.grab, indent=2, ensure_ascii=False)
    
    return render(request, 'grabber.html', {
        'grabbers': grabbers
    })


@csrf_exempt
@require_http_methods(["POST"])
def grabber_create(request):
    try:
        # Pegar dados do POST
        data = json.loads(request.body)
        
        name = data.get('name')
        grab = data.get('grab')
        
        # Validação básica
        if not name or not grab:
            return JsonResponse({
                'error': 'Os campos name e grab são obrigatórios'
            }, status=400)
        
        # Criar o grabber
        grabber = Grabber.objects.create(
            name=name,
            grab=grab
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Grabber criado com sucesso',
            'id': grabber.id,
            'name': grabber.name
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'JSON inválido'
        }, status=400)
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)