from vercel import VercelResponse
import random

def handler(request):
    id = request.query.get("id")
    if not id:
        return VercelResponse({"error": "Missing id"}, status=400)
    
    available = random.choice([True, False])
    return VercelResponse({"platform": "youtube", "id": id, "available": available})
