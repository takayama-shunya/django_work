from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.urls import reverse

from .models import Blog

class BlogIndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = "blog_list"

    def get_queryset(self):
        return Blog.objects.order_by('id')[:10]

class CreateView(generic.CreateView):
     #Cテーブル連携
    model = Blog
    #入力項目定義
    fields = ("title","content")
    #テンプレートファイル連携
    template_name = 'blogs/form.html'
    #作成後のリダイレクト先
    success_url = reverse_lazy("blogs:index")

class UpdateView(generic.UpdateView):
    #入力項目定義
    fields = ("title","content")
    #Companyテーブル連携
    model = Blog
    #テンプレートファイル連携
    template_name = "blogs/form.html"
    #更新後のリダイレクト先
    def get_success_url(self):
        return reverse('blogs:index')

def blogDelete(request, pk):
    # import pdb; pdb.set_trace() //デバック 関数
    blog = get_object_or_404(Blog, pk=pk)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    blog.delete()
    blog_list = Blog.objects.order_by('id')[:10]
    # success_url = reverse_lazy("blogs:index")
    return render(request, 'blogs/index.html', {'blog_list':blog_list})


# class DeleteView(generic.DeleteView):
#     model = Blog
#     template_name = "blogs/delete.html"
#     succes_url = reverse_lazy("blogs:index")
