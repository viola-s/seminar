from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the healines index.")


def showHeadlines(request):
    from . import requestsExample
    from django.template import loader

    url = "https://www.ynet.co.il"
    data = requestsExample.executeRequestsAndParseHeadlineContent(url)

    # create templates directory
    # add 'os.path.join(BASE_DIR, 'templates') ' to template dirs in settings
    template = loader.get_template('headlines/showHeadlines.html')
    context = {
        "data": data
    }
    return HttpResponse(template.render(context, request))