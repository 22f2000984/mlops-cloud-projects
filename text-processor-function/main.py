import hashlib
import functions_framework

@functions_framework.http
def process_text(request):
    j=request.get_json()
    t=j["text"]
    return {"uppercase":t.upper()}
