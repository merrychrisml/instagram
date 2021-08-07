from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpRequest, Http404
from .models import Post


# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get("q", "")
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(
#         request,
#         "instagram/post_list.html",
#         {
#             "post_list": qs,
#         },
#     )

post_list = ListView.as_view(model=Post, paginate_by=10)


# def post_detail(request=HttpRequest, pk=int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "instagram/post_detail.html", {"post": post})

post_detail = DetailView.as_view(model=Post)