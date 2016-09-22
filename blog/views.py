from django.shortcuts import render
from django.views import View

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