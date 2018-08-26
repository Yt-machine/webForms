from django.http import HttpResponse
from django.template.loader import get_template
from .models import Post, Mood


# Create your views here.
def index(request):
    template = get_template('index.html')
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)
