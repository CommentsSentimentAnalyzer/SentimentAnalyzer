from django.shortcuts import render,redirect,HttpResponse
from Community.models import Post, BlogComment
from django.contrib import messages
from SentimentAnalysis import views
from Community.templatetags import extras
# Create your views here.

def CommHome(request):
    allpost = Post.objects.all()
    cntxt = {'posts': allpost}
    return render(request, 'Community/CommHome.html', cntxt)

def CommPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    cmmnt = BlogComment.objects.filter(post=post, parent=None)
    rply = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in rply:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    cntxt = {'post': post, 'comments': cmmnt, 'user': request.user, 'replyDict':replyDict}
    return render(request, 'Community/CommPost.html', cntxt)

def CommPostComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno') 
        commentRes = views.make_prediction(comment)

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, status=commentRes, post=post)
            comment.save()
            messages.success(request, "Your Comment Has Been Posted Successfully...")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post,status=commentRes, parent=parent)
            comment.save()
            messages.success(request, "Your Reply Has Been Posted Successfully...")
    return redirect(f'/community/{post.slug}')
