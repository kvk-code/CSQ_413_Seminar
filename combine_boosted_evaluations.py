import csv
import os

# File paths
monday_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Consolidated_Evaluation_Monday_Boosted.csv'
friday_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Consolidated_Evaluation_Friday_Boosted.csv'
output_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Combined_Consolidated_Evaluation.csv'
report_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Verification_Report.txt'

def parse_float(value):
    """Safely parse float values, return None for empty strings"""
    if value == '' or value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None

def process_csv_file(file_path):
    """Extract required fields from CSV file"""
    students = []

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Skip empty rows
            if not row.get('Roll No') or row.get('Roll No').strip() == '':
                continue

            roll_no = row['Roll No'].strip()
            student_name = row['Student Name'].strip()

            # Extract the average columns
            avg_org = parse_float(row.get('Avg Organization (10)', ''))
            avg_clarity = parse_float(row.get('Avg Clarity & Communication (10)', ''))
            avg_qa = parse_float(row.get('Avg Q&A (10)', ''))
            avg_participation = parse_float(row.get('Avg Overall Participation (10)', ''))
            consolidated_total = parse_float(row.get('Consolidated Total (40)', ''))

            # Calculate sum of averages
            sum_of_averages = None
            if all(v is not None for v in [avg_org, avg_clarity, avg_qa, avg_participation]):
                sum_of_averages = avg_org + avg_clarity + avg_qa + avg_participation

            # Check for discrepancy
            discrepancy = None
            flag = ''
            if sum_of_averages is not None and consolidated_total is not None:
                discrepancy = abs(sum_of_averages - consolidated_total)
                # Flag if difference is more than 0.1 (accounting for rounding)
                if discrepancy > 0.1:
                    flag = 'MISMATCH'
            elif consolidated_total is None:
                flag = 'MISSING_TOTAL'
            elif sum_of_averages is None:
                flag = 'MISSING_AVERAGES'

            students.append({
                'Roll No': roll_no,
                'Student Name': student_name,
                'Avg Organization (10)': avg_org,
                'Avg Clarity & Communication (10)': avg_clarity,
                'Avg Q&A (10)': avg_qa,
                'Avg Overall Participation (10)': avg_participation,
                'Consolidated Total (40)': consolidated_total,
                'Calculated Sum': sum_of_averages,
                'Discrepancy': discrepancy,
                'Flag': flag
            })

    return students

# Process both files
print("Processing Monday batch file...")
monday_students = process_csv_file(monday_file)
print(f"Found {len(monday_students)} students in Monday batch")

print("\nProcessing Friday batch file...")
friday_students = process_csv_file(friday_file)
print(f"Found {len(friday_students)} students in Friday batch")

# Combine and sort by roll number
all_students = monday_students + friday_students
all_students.sort(key=lambda x: int(x['Roll No']) if x['Roll No'].isdigit() else 999)

print(f"\nTotal students: {len(all_students)}")

# Write combined CSV
print(f"\nWriting combined CSV to: {output_file}")
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = [
        'Roll No',
        'Student Name',
        'Avg Organization (10)',
        'Avg Clarity & Communication (10)',
        'Avg Q&A (10)',
        'Avg Overall Participation (10)',
        'Consolidated Total (40)',
        'Calculated Sum',
        'Discrepancy',
        'Flag'
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for student in all_students:
        writer.writerow(student)

# Generate verification report
print(f"Writing verification report to: {report_file}")
with open(report_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("COMBINED CONSOLIDATED EVALUATION - VERIFICATION REPORT\n")
    f.write("=" * 80 + "\n\n")

    f.write(f"Monday Batch Students: {len(monday_students)}\n")
    f.write(f"Friday Batch Students: {len(friday_students)}\n")
    f.write(f"Total Students: {len(all_students)}\n\n")

    # Find students with flags
    flagged_students = [s for s in all_students if s['Flag']]

    if flagged_students:
        f.write("=" * 80 + "\n")
        f.write(f"FLAGGED STUDENTS ({len(flagged_students)} found):\n")
        f.write("=" * 80 + "\n\n")

        for student in flagged_students:
            f.write(f"Roll No: {student['Roll No']}\n")
            f.write(f"Name: {student['Student Name']}\n")
            f.write(f"Flag: {student['Flag']}\n")
            f.write(f"Avg Organization: {student['Avg Organization (10)']}\n")
            f.write(f"Avg Clarity & Communication: {student['Avg Clarity & Communication (10)']}\n")
            f.write(f"Avg Q&A: {student['Avg Q&A (10)']}\n")
            f.write(f"Avg Overall Participation: {student['Avg Overall Participation (10)']}\n")
            f.write(f"Calculated Sum: {student['Calculated Sum']:.2f if student['Calculated Sum'] is not None else 'N/A'}\n")
            f.write(f"Consolidated Total (40): {student['Consolidated Total (40)'] if student['Consolidated Total (40)'] is not None else 'N/A'}\n")
            f.write(f"Discrepancy: {student['Discrepancy']:.2f if student['Discrepancy'] is not None else 'N/A'}\n")
            f.write("-" * 80 + "\n\n")
    else:
        f.write("=" * 80 + "\n")
        f.write("ALL STUDENTS VERIFIED - NO DISCREPANCIES FOUND\n")
        f.write("=" * 80 + "\n\n")

    # Summary statistics
    f.write("=" * 80 + "\n")
    f.write("SUMMARY STATISTICS:\n")
    f.write("=" * 80 + "\n\n")

    # Calculate averages
    valid_totals = [s['Consolidated Total (40)'] for s in all_students if s['Consolidated Total (40)'] is not None]
    if valid_totals:
        f.write(f"Average Consolidated Total: {sum(valid_totals) / len(valid_totals):.2f}\n")
        f.write(f"Minimum Consolidated Total: {min(valid_totals):.2f}\n")
        f.write(f"Maximum Consolidated Total: {max(valid_totals):.2f}\n")

    # Check for missing data
    missing_data = [s for s in all_students if s['Flag'] in ['MISSING_TOTAL', 'MISSING_AVERAGES']]
    if missing_data:
        f.write(f"\nStudents with missing data: {len(missing_data)}\n")

    f.write("\n" + "=" * 80 + "\n")
    f.write("END OF REPORT\n")
    f.write("=" * 80 + "\n")

print("\nProcessing complete!")
print(f"\nOutput files created:")
print(f"  - Combined CSV: {output_file}")
print(f"  - Verification Report: {report_file}")

if flagged_students:
    print(f"\n⚠️  WARNING: {len(flagged_students)} students have discrepancies or missing data!")
    print("   Please review the verification report for details.")
else:
    print("\n✓ All students verified - no discrepancies found!")
