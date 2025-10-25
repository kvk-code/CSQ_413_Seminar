import csv
import os

# File paths
class_roll_list = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\class_roll_list.csv'
monday_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Participation_Columns_Boost\Consolidated_Evaluation_Monday_Boosted_csv.csv'
friday_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Consolidated_Evaluation_Friday_Boosted.csv'
output_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Combined_Consolidated_Evaluation.csv'

# Step 1: Create name to roll number mapping
print("Creating name to roll number mapping...")
name_to_roll = {}
with open(class_roll_list, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Normalize name by removing extra spaces and converting to uppercase
        name = ' '.join(row['Name'].strip().upper().split())
        roll_no = row['Class Roll No'].strip()
        name_to_roll[name] = roll_no

print(f"Loaded {len(name_to_roll)} students from class roll list")

# Function to normalize names for matching
def normalize_name(name):
    return ' '.join(name.strip().upper().split())

# Step 2: Read Monday batch data
print("\nReading Monday batch data...")
monday_data = []
with open(monday_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        student_name = row.get('Student Name', '').strip()
        if not student_name:
            continue

        normalized_name = normalize_name(student_name)
        roll_no = name_to_roll.get(normalized_name, '')

        if not roll_no:
            print(f"  Warning: Could not find roll number for '{student_name}' (normalized: '{normalized_name}')")
            continue

        monday_data.append({
            'Roll No': roll_no,
            'Student Name': student_name,
            'Presentation Title': row.get('Presentation Title', '').strip(),
            'Avg Organization (10)': row.get('Avg Organization (10)', '').strip(),
            'Avg Clarity & Communication (10)': row.get('Avg Clarity & Communication (10)', '').strip(),
            'Avg Q&A (10)': row.get('Avg Q&A (10)', '').strip(),
            'Avg Overall Participation (10)': row.get('Avg Overall Participation (10)', '').strip(),
            'Consolidated Total (40)': row.get('Consolidated Total (40)', '').strip()
        })

print(f"Loaded {len(monday_data)} students from Monday batch")

# Step 3: Read Friday batch data
print("\nReading Friday batch data...")
friday_data = []
with open(friday_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        roll_no = row.get('Roll No', '').strip()
        student_name = row.get('Student Name', '').strip()

        if not roll_no or not student_name:
            continue

        friday_data.append({
            'Roll No': roll_no,
            'Student Name': student_name,
            'Presentation Title': row.get('Presentation Title', '').strip(),
            'Avg Organization (10)': row.get('Avg Organization (10)', '').strip(),
            'Avg Clarity & Communication (10)': row.get('Avg Clarity & Communication (10)', '').strip(),
            'Avg Q&A (10)': row.get('Avg Q&A (10)', '').strip(),
            'Avg Overall Participation (10)': row.get('Avg Overall Participation (10)', '').strip(),
            'Consolidated Total (40)': row.get('Consolidated Total (40)', '').strip()
        })

print(f"Loaded {len(friday_data)} students from Friday batch")

# Step 4: Combine and sort by roll number
print("\nCombining data...")
all_data = monday_data + friday_data
all_data.sort(key=lambda x: int(x['Roll No']))

print(f"Total students in combined file: {len(all_data)}")

# Step 5: Write to output file
print(f"\nWriting to {output_file}...")
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = [
        'Roll No',
        'Student Name',
        'Presentation Title',
        'Avg Organization (10)',
        'Avg Clarity & Communication (10)',
        'Avg Q&A (10)',
        'Avg Overall Participation (10)',
        'Consolidated Total (40)'
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_data)

print("\nDone! Combined evaluation file created successfully.")
print(f"Roll numbers range from {all_data[0]['Roll No']} to {all_data[-1]['Roll No']}")

# Summary
print("\n=== SUMMARY ===")
print(f"Monday batch: {len(monday_data)} students")
print(f"Friday batch: {len(friday_data)} students")
print(f"Total combined: {len(all_data)} students")
print(f"Output file: {output_file}")
