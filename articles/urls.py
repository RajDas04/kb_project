<<<<<<< HEAD
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleHistoryView, ArticleRevertView, ArticlePreviewVersionView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('new/', ArticleCreateView.as_view(), name='article-create'),
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug:slug>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<slug:slug>/history/', ArticleHistoryView.as_view(), name='article-history'),
    path('<slug:slug>/revert/<int:version_id>', ArticleRevertView.as_view(), name='article-revert'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('<slug:slug>/preview/<int:version_id>', ArticlePreviewVersionView.as_view(), name='article-preview'),
=======
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleHistoryView, ArticleRevertView, ArticlePreviewVersionView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('new/', ArticleCreateView.as_view(), name='article-create'),
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug:slug>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<slug:slug>/history/', ArticleHistoryView.as_view(), name='article-history'),
    path('<slug:slug>/revert/<int:version_id>', ArticleRevertView.as_view(), name='article-revert'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('<slug:slug>/preview/<int:version_id>', ArticlePreviewVersionView.as_view(), name='article-preview'),
>>>>>>> 40a0b34 (update- adding the desktop app)
]