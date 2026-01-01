from .models import Link

def ctx_dict_social_links(request):
    ctx = {}
    social_links = Link.objects.all()
    for link in social_links:
        ctx[link.key] = link.url
    return ctx
