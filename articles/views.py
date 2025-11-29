<<<<<<< HEAD
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import Article
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from reversion.models import Version
from taggit.models import Tag
from django.urls import reverse_lazy
from .forms import ArticleForm
import reversion

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = ['updated_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=tag)
        query = self.request.GET.get('q')
        if query:
            queryset= queryset.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['active_tag'] = self.kwargs.get('tag_slug','')
        context['query'] = self.request.GET.get('q','')
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'

    def form_valid(self, form):
        with reversion.create_revision():
            form.instance.author = self.request.user
            response = super().form_valid(form)
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            else:
                reversion.set_user(None)
            reversion.set_comment("Created")
            return response
    
    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'slug':self.object.slug})

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    context_object_name = 'article'

    def form_valid(self, form):
        with reversion.create_revision():
            response = super().form_valid(form)
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            else:
                reversion.set_user(None)
            return response

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'slug':self.object.slug})
    
class ArticleHistoryView(View):
    template_name = 'article_history.html'

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        versions = Version.objects.get_for_object(article)
        return render(request, self.template_name, {'article': article, 'versions': versions})
    
class ArticleRevertView(View):
    def post(self, request, slug, version_id):
        article = get_object_or_404(Article, slug=slug)
        version = get_object_or_404(Version, pk=version_id)
        with reversion.create_revision():
            version.revision.revert(delete=False)
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            else:
                reversion.set_user(None)
            reversion.set_comment(f"Reverted to version {version_id}")
        return redirect('article-detail', slug=slug)
    
class ArticlePreviewVersionView(View):
    template_name = 'article_preview.html'
    def get(self, request, slug, version_id):
        article = get_object_or_404(Article, slug=slug)
        version = get_object_or_404(Version, pk=version_id)
        version_data = version.field_dict
        preview_article = Article(**version_data)
        return render(request, self.template_name, {'article': article, 'preview_article': preview_article, 
=======
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import Article
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from reversion.models import Version
from taggit.models import Tag
from django.urls import reverse_lazy
from .forms import ArticleForm
import reversion

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = ['updated_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=tag)
        query = self.request.GET.get('q')
        if query:
            queryset= queryset.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['active_tag'] = self.kwargs.get('tag_slug','')
        context['query'] = self.request.GET.get('q','')
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'

    def form_valid(self, form):
        with reversion.create_revision():
            form.instance.author = self.request.user
            response = super().form_valid(form)
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            else:
                reversion.set_user(None)
            reversion.set_comment("Created")
            return response
    
    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'slug':self.object.slug})

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    context_object_name = 'article'

    def form_valid(self, form):
        with reversion.create_revision():
            response = super().form_valid(form)
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            else:
                reversion.set_user(None)
            return response

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'slug':self.object.slug})
    
class ArticleHistoryView(View):
    template_name = 'article_history.html'

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        versions = Version.objects.get_for_object(article)
        return render(request, self.template_name, {'article': article, 'versions': versions})
    
class ArticleRevertView(View):
    def post(self, request, slug, version_id):
        article = get_object_or_404(Article, slug=slug)
        version = get_object_or_404(Version, pk=version_id)
        with reversion.create_revision():
            version.revision.revert(delete=False)
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            else:
                reversion.set_user(None)
            reversion.set_comment(f"Reverted to version {version_id}")
        return redirect('article-detail', slug=slug)
    
class ArticlePreviewVersionView(View):
    template_name = 'article_preview.html'
    def get(self, request, slug, version_id):
        article = get_object_or_404(Article, slug=slug)
        version = get_object_or_404(Version, pk=version_id)
        version_data = version.field_dict
        preview_article = Article(**version_data)
        return render(request, self.template_name, {'article': article, 'preview_article': preview_article, 
>>>>>>> 40a0b34 (update- adding the desktop app)
                                                    'version': version})