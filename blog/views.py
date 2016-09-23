from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
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
        #TODO: No mostrar los que tengan fecha futura
        posts = Post.objects.all().order_by('-created_at')
        context = {'posts_list': posts[:10]}
        return render(request, 'blog/home.html', context)


class PostDetailView(View):

    def get(self, request):
        """
        Renderiza un post
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todas los posts publicados
        #TODO: No mostrar los que tengan fecha futura
        #posts = Post.objects.all().order_by('-created_at')
        context = {}
        return render(request, 'blog/home.html', context)


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
