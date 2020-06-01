from django.shortcuts import render
from .models import Post,Categery,Comment
from taggit.models import Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):
    postlist=Post.objects.all()

    search_query=request.GET.get('q')
    if search_query:
        postlist=postlist.filter(
            Q(title__icontains = search_query)|
            Q(content__icontains =search_query)|
            Q(tags__name__icontains =search_query)
        ).distinct()


    paginator = Paginator(postlist, 6)
    page_number = request.GET.get('page')
    postlist = paginator.get_page(page_number)

    context={'post_list':postlist,}

    return render(request,'blog/post_list.html',context)


def post_details(request,id):
    detail_list=Post.objects.get(id=id)
    categeries=Categery.objects.all()
    all_tags=Tag.objects.all()
    comments=Comment.objects.filter(post=detail_list)
    comment_form=CommentForm()
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.user=request.user
            new_comment.post=detail_list
            new_comment.save()

    context={'post':detail_list,
             'categeries':categeries,
             'all_tags':all_tags,
             'comments':comments,
             'comment_form':comment_form,}
    return render(request,'blog/post_details.html',context)

# Create your views here.
def post_by_tag(request,tag):
    post_bytag=Post.objects.filter(tags__name__in=[tag])
    context={'post_list':post_bytag,}

    return render(request,'blog/post_list.html',context)

def post_by_categery(request,categery):
    post_bycategery = Post.objects.filter(categery__categery_name=categery)
    context = {'post_list': post_bycategery, }

    return render(request, 'blog/post_list.html', context)