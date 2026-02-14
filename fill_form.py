import csv
from pypdf import PdfReader, PdfWriter

def fill_student_form(template_pdf, output_pdf, form_data):
    reader = PdfReader(template_pdf)
    writer = PdfWriter()
    writer.append(reader)

    writer.update_page_form_field_values(
        writer.pages[0],
        form_data,
        auto_regenerate=True,
    )

    with open(output_pdf, "wb") as f:
        writer.write(f)


path_to_pdf = r"c:\users\owner\documents\studentforms"
pdf_name = "Student Recommendation Form"
pdf_end = ".pdf"

template_pdf = f"{path_to_pdf}\\{pdf_name}{pdf_end}"

with open(r"c:\users\owner\documents\studentforms\students.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)  # keys from header row
    for row in reader:
        # Optionally clean/convert or subset keys here
        form_data = {
            "instructor": row["instructor"],
            "student_name": row["student_name"],
            "term": row["term"],
            "grade": row["grade"],
            "semester": row["semester"],
            "class_name": row["class_name"],
            "number_of_hours": row["number_of_hours"],
            "pre_michigan_score": row["pre_michigan_score"],
            "post_michigan_score": row["post_michigan_score"],
            "pre_michigan_date": row["pre_michigan_date"],
            "post_michigan_date": row["post_michigan_date"],
            "hours_absent": row["hours_absent"],
            "post_clip_date": row["post_clip_date"],
            "pre_CR": row["pre_CR"],
            "pre_DEV": row["pre_DEV"],
            "pre_ORG": row["pre_ORG"],
            "pre_WC": row["pre_WC"],
            "pre_GR": row["pre_GR"],
            "pre_total": row["pre_total"],
            "post_CR": row["post_CR"],
            "post_DEV": row["post_DEV"],
            "post_ORG": row["post_ORG"],
            "post_WC": row["post_WC"],
            "post_GR": row["post_GR"],
            "post_total": row["post_total"],
            "hours_present": row["hours_present"],
        }

        # Use student name and class nameto make a unique output file
        safe_name = f"{row['student_name'].replace(' ', '_')} - {row['class_name'].replace(' ', '_')}"
        output_pdf = f"{path_to_pdf}\\filled\\{safe_name} - {pdf_name}{pdf_end}"
        fill_student_form(template_pdf, output_pdf, form_data)
