
from django.shortcuts import render, redirect
from .models import Institution, StudentApplication
import joblib

model = joblib.load("models/fake_model.pkl")
le = joblib.load("models/label_encoder.pkl")

def search_institution(request):
    if request.method == "POST":
        name = request.POST["name"]

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



def apply_student(request, inst_id):
    inst = Institution.objects.get(id=inst_id)

    if request.method == "POST":
        student_name = request.POST["student_name"]
        email = request.POST["email"]
        course = request.POST["course"]

        StudentApplication.objects.create(
            student_name=student_name,
            email=email,
            institution=inst,
            course=course
        )

        return render(request, "success.html")

    return render(request, "apply.html", {"inst": inst})


from .models import StudentApplication

def view_students(request):
    students = StudentApplication.objects.all()
    return render(request, "students.html", {"students": students})


from django.shortcuts import render, redirect
from .models import AdminUser, StudentApplication

def admin_login(request):
    error = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        admin = AdminUser.objects.filter(
            username=username,
            password=password
        ).first()

        if admin:
            request.session["admin"] = admin.username
            return redirect("admin_students")
        else:
            error = "Invalid username or password"

    return render(request, "admin_login.html", {"error": error})

def admin_students(request):
    if "admin" not in request.session:
        return redirect("admin_login")

    students = StudentApplication.objects.all()
    return render(request, "admin_students.html", {"students": students})
def admin_logout(request):
    if "admin" in request.session:
        del request.session["admin"]
    return redirect("admin_login")


import csv
from django.http import HttpResponse
from .models import StudentApplication

def download_students_report(request):
    # 🔐 Protect page (admin only)
    if "admin" not in request.session:
        return redirect("admin_login")

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="students_report.csv"'

    writer = csv.writer(response)
    writer.writerow(["Student Name", "Email", "Course", "Institution"])

    students = StudentApplication.objects.all()

    for s in students:
        writer.writerow([
            s.student_name,
            s.email,
            s.course,
            s.institution.name
        ])

    return response
