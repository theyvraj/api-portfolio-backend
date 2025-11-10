from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

ABOUT = {
    "name": "Dev",
    "role": "Backend Developer",
    "location": "India",
    "tech_stack": ["Python", "Django", "DRF", "Playwright", "AsyncIO"],
    "summary": "I build API-first systems and automation tools."
}
SKILLS = {
    "python": 5, "django": 5, "rest_framework": 5,
    "asyncio": 4, "scraping": 5, "docker": 3
}
PROJECTS = [
    {
        "name": "SEO Scanner",
        "description": "Async SEO crawler with schema extraction & PageSpeed integration.",
        "tech": ["Django", "Playwright", "DRF"],
        "links": {"repo": "https://github.com/theyvraj?tab=repositories"}
    },
    {
        "name": "Inventory System",
        "description": "Django inventory management for peripherals & accessories.",
        "tech": ["Django", "PostgreSQL"]
    }
]

def require_post(request):
    if request.method != "POST":
        return Response({"detail": "POST only."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["POST"])
def about(request):
    detail = request.data.get("detail")
    data = ABOUT | ({"detail": "full", "interests": ["SEO crawling", "system design", "automation"]} if detail=="full" else {})
    return Response(data)

@api_view(["POST"])
def skills(request): return Response(SKILLS)

@api_view(["POST"])
def projects(request): return Response(PROJECTS)

@api_view(["POST"])
def resume(request):
    return Response({
        "download": "https://limewire.com/d/iUKoj#QCyFpTyi2y",
        "format": "pdf",
    })

@api_view(["POST"])
def random_fact(request):
    return Response({"fact": "I prefer async for IO-bound workloads."})

@api_view(["POST"])
def hireme(request):
    payload = request.data or {}
    note = payload.get("note", "Thanks for reaching out!")
    return Response({"message": note, "contact": "youremail@example.com"})
