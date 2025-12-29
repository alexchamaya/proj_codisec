def ctx_general(request):
    from applications.general.models import General
    general = General.objects.first()
    return {
        'general': general
    }