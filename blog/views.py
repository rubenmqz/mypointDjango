from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from blog.forms import PostForm
from blog.models import Post


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con los últimos posts
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todas los posts publicados
        posts = Post.objects.filter(publish_at__lt=timezone.now()).order_by('-created_at')
        context = {'posts_list': posts[:10]}
        return render(request, 'blog/home.html', context)


class BlogListView(ListView):
    """
    Muestra el listado de blogs disponibles (de los usuarios que han publicado algo)
    """
    model = User
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        return User.objects.filter(post__isnull=False).distinct()



class PostsByUserView(View):

    def get(self, request, nombre_de_usuario):
        """
        Renderiza todos los posts de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todos los posts publicados del usuario
        user = User.objects.filter(username=nombre_de_usuario)
        if len(user) == 0:
            return HttpResponseNotFound("El blog que buscas no existe")
        elif len(user) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        posts = Post.objects.filter(owner=user, publish_at__lt=timezone.now()).order_by('-created_at')
        context = {'posts_list': posts, 'user': user[0]}
        return render(request, 'blog/blog_usuario.html', context)


class PostDetailView(View):

    def get(self, request, nombre_de_usuario, post_id):
        """
        Renderiza un post
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # se asegura de que el autor exista
        user = User.objects.filter(username=nombre_de_usuario)
        if len(user) == 0:
            return HttpResponseNotFound("El blog que buscas no existe")
        elif len(user) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        posts = Post.objects.filter(owner=user, pk=post_id, publish_at__lt=timezone.now())

        if len(posts) == 0:
            return HttpResponseNotFound("El post que buscas no existe")
        elif len(posts) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        context = {'post': posts[0]}
        return render(request, 'blog/post_detail.html', context)


class NewPostView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear un post
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        post_form = PostForm()
        context = {'form': post_form}
        return render(request, 'blog/new_post.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Valida la petición, y crea el post asociado al user logado
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        new_post = None

        if not request.user.is_authenticated:
            message = "No estás logado. Es posible que tu sesión haya caducado. Vuelve a hacer login antes de publicar el post."
            post_form = PostForm()
        else:
            post_with_user = Post(owner=request.user)
            post_form = PostForm(request.POST, instance=post_with_user)
            if post_form.is_valid():
                new_post = post_form.save()
                post_form = PostForm()

        context = {'form': post_form, 'new_post': new_post, 'error': message}
        return render(request, 'blog/new_post.html', context)
