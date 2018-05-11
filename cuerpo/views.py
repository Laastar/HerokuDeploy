from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.utils import timezone
from datetime import time, datetime
from django.contrib import messages, sessions
from cuerpo.models import Post, User, Opiniones, Producto, Barnice, CuidadoCabello, CuidadoPersonal, PerfumesLociones
from cuerpo.forms import PostFormulario, SignUpForm, LoginForm, CitasForm, OpinionForm, RecuperarForm

# Create your views here. Ba

def index(request):
    return render(request, 'cuerpo/index.html', {})

def menuproductos(request):
    return render(request, 'cuerpo/menuproductos.html', {})

def cabello(request):
    cuidadocabellos = CuidadoCabello.objects.all()
    return render(request, 'cuerpo/cabello.html', {'cuidadocabellos' : cuidadocabellos})

def perfumes(request):
    perfumeslocioness = PerfumesLociones.objects.all()
    return render(request, 'cuerpo/perfumes.html', {'perfumeslocioness' : perfumeslocioness})

def cuidado(request):
    cuidadopersonals = CuidadoPersonal.objects.all()
    return render(request, 'cuerpo/cuidado.html', {'cuidadopersonals' : cuidadopersonals})

def barnices(request):
    barnices = Barnice.objects.all()
    return render(request, 'cuerpo/barnices.html', {'barnices' : barnices})

def maquillaje(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/maquillaje.html', {'productos' : productos})

def unete(request):
    return render(request, 'cuerpo/unete.html', {})


def opiniones(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.save()
            return redirect('opiniones')
    else:
        form = OpinionForm()
    return render(request, 'cuerpo/opiniones.html', {'form' : form})

def contacto(request):
    return render(request, 'cuerpo/contacto.html', {})

def tips(request):
    return render(request, 'cuerpo/tips.html', {})

def recuperar(request):
    if request.method == 'POST':
        form = RecuperarForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                usuario = User.objects.get(email=user.email)
                passwd = usuario.password1
                correo = usuario.email
                email = EmailMessage('Recuperacion de contraseña', 'Contraseña: ' + passwd, to=[correo])
                email.send()
                return render(request, 'cuerpo/index.html', {})
            except User.DoesNotExist:
                messages.info(request, 'Infromación errónea')
                redirect('login')
    else:
        form = RecuperarForm()
    return render(request, 'cuerpo/recuperacion.html', {'form': form})

def cerrar(request):
        request.session['USUARIO_LOGEADO'] = ""
        messages.info(request, 'Se ha cerrado la sesion')
        return redirect('login')

def login(request):
    USUARIO_LOGEADO = request.session.get('USUARIO_LOGEADO')
    if not USUARIO_LOGEADO:
        request.session['USUARIO_LOGEADO'] = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password = form.cleaned_data.get('password')
            try:
                usuario = User.objects.get(username=user.username)
                if (USUARIO_LOGEADO != ""):
                    messages.info(request, 'Usuario ya esta logeado')
                elif (user.password != usuario.password1):
                    messages.info(request, 'Informacion erronea')
                else:
                    request.session['USUARIO_LOGEADO'] = user.username
                    messages.info(request, 'Bienvenid@ ' + user.username)
                    return render(request, 'cuerpo/index.html', {})
            except User.DoesNotExist:
                messages.info(request, 'Infromación errónea')
                redirect('login')
    else:
        form = LoginForm()
    return render(request, 'cuerpo/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            if(user.password1 != user.password2):
                messages.info(request, 'Contraseñas no concuerdan.')
            else:
                user.save()
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'cuerpo/registro.html', {'form': form})

def citas(request):
    usuario = request.session['USUARIO_LOGEADO']
    if not usuario or usuario == "":
        messages.info(request, 'Inicia sesión')
        redirect('login')
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=usuario)
                instance = form.save()
                instance.username = user.username
                instance.email = user.email
                if(instance.hora > time(19,00)):
                    messages.info(request, 'Información errónea')
                elif(instance.hora < time(9,00)):
                    messages.info(request, 'Información errónea')
                else:
                    instance.save()
                    messages.info(request, usuario + " ya se agendó tu cita")
                    return render(request, 'cuerpo/index.html', {})
            except User.DoesNotExist:
                messages.info(request, 'Información errónea')
    else:
        form = CitasForm()
    return render(request, 'cuerpo/citas.html', {'form': form})

def listadoPosts(request):
    posts = Post.objects.filter(fechaPublicacion__lte = timezone.now()).order_by('fechaPublicacion')
    return render(request,'cuerpo/listadoPosts.html',{'posts':posts})

def detalles(request, pk):
    posts = get_object_or_404(Post, pk = pk)
    return render(request, 'cuerpo/detalles.html', {'post': posts})

def nuevoPost(request):
    if request.method == 'POST':
        form = PostFormulario(request.POST)
        if  form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fechaPublicacion = timezone.now()
            post.save()
            return redirect('detalles',pk=post.pk)
    else:
        form = PostFormulario()
    return render(request, 'cuerpo/editar.html',{'form':form})

def modificar(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostFormulario(request.POST,instance=post)
        if  form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalles',pk=post.pk)
    else:
        form = PostFormulario(instance=post)
    return render(request, 'cuerpo/editar.html',{'form':form})