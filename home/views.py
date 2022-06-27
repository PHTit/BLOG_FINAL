from django.shortcuts import render
from django.db.models import Q
from user.models import Avatar


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}



def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(name__contains=search_param)

    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )

def about(request):
    context_dict = {}
    return render(
        request=request,
        context=context_dict,
        template_name="home/about.html",
    )


def handler404(request, exception, template_name="home/not-found.html"):
    response = render('/not-found')
    response.status_code = 404
    return render(request, response)
