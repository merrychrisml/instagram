from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, ArchiveIndexView, YearArchiveView
from django.http import HttpResponse, HttpRequest, Http404
from .models import Post
from .forms import PostForm


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(
        request,
        "instagram/post_form.html",
        {
            "form": form,
        },
    )


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

post_archive = ArchiveIndexView.as_view(
    model=Post, date_field="created_at", paginate_by=10
)

post_archive_year = YearArchiveView.as_view(
    model=Post, date_field="created_at", make_object_list=True
)
