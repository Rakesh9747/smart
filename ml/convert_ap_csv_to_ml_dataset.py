import csv
import random

input_file = "andhra_pradesh_100_colleges.csv"
output_file = "media/datasets/institution_ml.csv"

with open(output_file, "w", newline="", encoding="utf-8") as out_csv:
    writer = csv.writer(out_csv)

    # ML DATASET HEADER
    writer.writerow([
        "rating",
        "accreditation",
        "website_valid",
        "reviews_count",
        "placement_score",
        "status"
    ])

    # ---- PART 1: GENUINE COLLEGES (FROM AP CSV) ----
    with open(input_file, newline="", encoding="utf-8") as in_csv:
        reader = csv.DictReader(in_csv)

        for row in reader:
            writer.writerow([
                round(random.uniform(3.8, 5.0), 1),   # rating
                1,                                    # accreditation
                1,                                    # website_valid
                random.randint(500, 2500),            # reviews
                random.randint(70, 95),               # placement
                "Genuine"
            ])

    # ---- PART 2: AUTO‑GENERATED FAKE COLLEGES ----
    for i in range(1, 101):  # 100 fake institutions
        writer.writerow([
            round(random.uniform(0.5, 2.5), 1),   # rating
            0,                                    # accreditation
            0,                                    # website_valid
            random.randint(5, 100),               # reviews
            random.randint(15, 40),               # placement
            "Fake"
        ])

print("✅ ML dataset created successfully")
