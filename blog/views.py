from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)
    # return HttpResponse('This is blogHome. ')

def blogPost(request, slug):
    # post = Post.objects.get(slug=slug)
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f'This is blogPost.{slug}')

def postComment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        post = Post.objects.filter(sno=postSno).first()
        # save
        comments = BlogComment(comment=comment, user=user, post=post)
        comments.save()
        messages.success(request, "Your comment has been posted successfully.")
        return redirect(f"/blog/{post.slug}")
    else:
        messages.error(request, "something wrong")
        return redirect("/")