from vercel import VercelResponse
import random

def handler(request):
    if request.method == "OPTIONS":
        return VercelResponse(
            "",
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                "Access-Control-Allow-Headers": "*"
            }
        )

    id = request.query.get("id")
    if not id:
        return VercelResponse(
            {"error": "Missing id parameter"}, 
            status=400,
            headers={"Access-Control-Allow-Origin": "*"}
        )

    available = random.choice([True, False])
    return VercelResponse(
        {"platform": "youtube", "id": id, "available": available},
        headers={"Access-Control-Allow-Origin": "*"}
    )
