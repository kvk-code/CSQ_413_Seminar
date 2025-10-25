import csv
import os
from datetime import datetime

# Student information to update
ROLL_NO = "21"
STUDENT_NAME = "ARUN PRAKASH K"
NEW_BACKGROUND_KNOWLEDGE = "8"
NEW_TOPIC_RELEVANCE = "10"
NEW_GUIDE_TOTAL = "18"

print("=" * 100)
print(f"UPDATING GUIDE MARKS FOR {STUDENT_NAME} (Roll No: {ROLL_NO})")
print("=" * 100)
print(f"New Background Knowledge: {NEW_BACKGROUND_KNOWLEDGE}/10")
print(f"New Topic Relevance: {NEW_TOPIC_RELEVANCE}/10")
print(f"New Guide Total: {NEW_GUIDE_TOTAL}/20")
print("=" * 100)
print()

# File to update
guide_marks_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\For_Display\CSQ413_S7CSE_Seminar_Guide_Marks - Guide_Marks.csv'

# Create backup
backup_file = guide_marks_file.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')

# Read and update the file
updated_rows = []
student_found = False
old_values = {}

print(f"Reading file: {guide_marks_file}")

with open(guide_marks_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    for row in reader:
        if row['Roll No'] == ROLL_NO:
            student_found = True
            # Save old values for reporting
            old_values = {
                'Background Knowledge': row['Background Knowledge (10)'],
                'Topic Relevance': row['Topic Relevance (10)'],
                'Guide Total': row['Guide Total (20)']
            }

            # Update the values
            row['Background Knowledge (10)'] = NEW_BACKGROUND_KNOWLEDGE
            row['Topic Relevance (10)'] = NEW_TOPIC_RELEVANCE
            row['Guide Total (20)'] = NEW_GUIDE_TOTAL

            print(f"\nFound student: {row['Student Name']}")
            print(f"  Batch: {row['Batch']}")
            print(f"  Guide: {row['Guide Name']}")
            print(f"\nOLD VALUES:")
            print(f"  Background Knowledge: {old_values['Background Knowledge']}/10")
            print(f"  Topic Relevance: {old_values['Topic Relevance']}/10")
            print(f"  Guide Total: {old_values['Guide Total']}/20")
            print(f"\nNEW VALUES:")
            print(f"  Background Knowledge: {NEW_BACKGROUND_KNOWLEDGE}/10")
            print(f"  Topic Relevance: {NEW_TOPIC_RELEVANCE}/10")
            print(f"  Guide Total: {NEW_GUIDE_TOTAL}/20")

        updated_rows.append(row)

if not student_found:
    print(f"\nERROR: Student with Roll No {ROLL_NO} not found!")
    exit(1)

# Create backup
print(f"\nCreating backup: {backup_file}")
with open(backup_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    # Read original file again for backup
    with open(guide_marks_file, 'r', encoding='utf-8') as orig:
        reader = csv.DictReader(orig)
        for row in reader:
            writer.writerow(row)

# Write updated file
print(f"Writing updated file: {guide_marks_file}")
with open(guide_marks_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print("\n" + "=" * 100)
print("UPDATE COMPLETED SUCCESSFULLY!")
print("=" * 100)
print(f"\nSummary of changes:")
print(f"  Student: {STUDENT_NAME} (Roll No: {ROLL_NO})")
print(f"  Background Knowledge: {old_values['Background Knowledge']} -> {NEW_BACKGROUND_KNOWLEDGE}")
print(f"  Topic Relevance: {old_values['Topic Relevance']} -> {NEW_TOPIC_RELEVANCE}")
print(f"  Guide Total: {old_values['Guide Total']} -> {NEW_GUIDE_TOTAL}")
print(f"\n  Change in Guide Total: +{int(NEW_GUIDE_TOTAL) - int(old_values['Guide Total'])} marks")
print("\n" + "=" * 100)
