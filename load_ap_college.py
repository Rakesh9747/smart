import os
import csv
import random
import django

# SET DJANGO SETTINGS
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartinstitution.settings")
django.setup()

from app.models import Institution

file_path = os.path.join(os.getcwd(), "andhra_pradesh_100_colleges.csv")

print("File exists:", os.path.exists(file_path))

count = 0

with open(file_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    print("CSV headers:", reader.fieldnames)

    for row in reader:
        Institution.objects.create(
            name=row["name"],
            rating=round(random.uniform(3.8, 5.0), 1),
            accreditation=1,
            website_valid=1,
            reviews_count=random.randint(500, 2500),
            placement_score=random.randint(70, 95),
            website=row["website"],
            image_url=row["image_url"]
        )
        count += 1

print(f"✅ {count} Andhra Pradesh colleges inserted successfully")
