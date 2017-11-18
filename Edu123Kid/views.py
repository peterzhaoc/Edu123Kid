from django.http import HttpResponse

import os

def test(request):
    BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR2 = BASE_DIR1 + "0000" + os.path.join(BASE_DIR1, 'static').replace('\\', '/')
    html = "<html><body>It is now %s.</body></html>" % BASE_DIR1
    return HttpResponse(html)
