from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from mysite import models


# Create your views here.
def index(request, pid=None, del_pass=None):
    template = get_template('index.html')

    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如果要张贴消息，那么每一个字段都要填...'

    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "数据删除成功"
            else:
                message = "密码错误"
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功存储！请记得您的编辑密码[{}]!,信息须经审查后才会显示。'.format(user_pass)
    html = template.render(locals())
    return HttpResponse(html)


def list(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)


def posting(request):
    template = get_template('posting.html')
    moods = models.Mood.objects.all()
    message = '如果要张贴信息,那么每一个字段都要填...'
    request_context = {'moods': moods, 'message': message}
    html = template.render(request, request_context)

    return HttpResponse(html)
