from django.shortcuts import render
from .models import Institution
import joblib

model = joblib.load("models/fake_model.pkl")
le = joblib.load("models/label_encoder.pkl")

def search_institution(request):
    if request.method == "POST":
        name = request.POST["name"].strip()

        # ✅ PARTIAL, CASE‑INSENSITIVE SEARCH
        inst = Institution.objects.filter(name__icontains=name).first()

        if not inst:
            return render(request, "index.html", {"not_found": True})

        features = [[
            inst.rating,
            inst.accreditation,
            inst.website_valid,
            inst.reviews_count,
            inst.placement_score
        ]]

        prediction = model.predict(features)[0]
        result = le.inverse_transform([prediction])[0]

        if result == "Genuine":
            return render(request, "index.html", {
                "genuine": True,
                "inst": inst
            })
        else:
            return render(request, "index.html", {
                "fake": True
            })

    return render(request, "index.html")

from django.http import JsonResponse
from .models import Institution

def autosuggest(request):
    query = request.GET.get("q", "")

    results = []
    if query:
        qs = Institution.objects.filter(
            name__icontains=query
        ).order_by("name")[:5]

        for inst in qs:
            results.append({
                "name": inst.name,
                "rating": inst.rating,
                "placement": inst.placement_score,
                "accreditation": "Yes" if inst.accreditation == 1 else "No"
            })

    return JsonResponse(results, safe=False)
