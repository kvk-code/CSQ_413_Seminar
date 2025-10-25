import csv

# Read the combined CSV file
csv_file = r'C:\Users\kiran\Downloads\Projects\CSQ_413_Seminar\Evaluations\Boosted_Evaluations\Combined_Consolidated_Evaluation.csv'

print("=" * 100)
print("DETAILED VERIFICATION OF ALL STUDENT ENTRIES")
print("=" * 100)
print()

students = []
issues = []
perfect_matches = 0

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        roll_no = row['Roll No']
        name = row['Student Name']

        # Get the values
        org = float(row['Avg Organization (10)']) if row['Avg Organization (10)'] else 0
        clarity = float(row['Avg Clarity & Communication (10)']) if row['Avg Clarity & Communication (10)'] else 0
        qa = float(row['Avg Q&A (10)']) if row['Avg Q&A (10)'] else 0
        participation = float(row['Avg Overall Participation (10)']) if row['Avg Overall Participation (10)'] else 0
        consolidated = float(row['Consolidated Total (40)']) if row['Consolidated Total (40)'] else 0

        # Calculate sum
        calculated_sum = org + clarity + qa + participation

        # Check if they match
        difference = abs(calculated_sum - consolidated)

        students.append({
            'roll': roll_no,
            'name': name,
            'org': org,
            'clarity': clarity,
            'qa': qa,
            'participation': participation,
            'calculated': calculated_sum,
            'consolidated': consolidated,
            'difference': difference
        })

        # Check for issues (difference > 0.01 to account for rounding)
        if difference > 0.01:
            issues.append({
                'roll': roll_no,
                'name': name,
                'calculated': calculated_sum,
                'consolidated': consolidated,
                'difference': difference
            })
        else:
            perfect_matches += 1

print(f"Total Students Checked: {len(students)}")
print(f"Perfect Matches (difference <= 0.01): {perfect_matches}")
print(f"Issues Found (difference > 0.01): {len(issues)}")
print()

if issues:
    print("=" * 100)
    print("ISSUES DETECTED:")
    print("=" * 100)
    for issue in issues:
        print(f"\nRoll No: {issue['roll']}")
        print(f"Name: {issue['name']}")
        print(f"Calculated Sum: {issue['calculated']:.2f}")
        print(f"Consolidated Total: {issue['consolidated']:.2f}")
        print(f"Difference: {issue['difference']:.2f}")
        print("-" * 100)
else:
    print("ALL ENTRIES VERIFIED SUCCESSFULLY!")
    print("  All calculated sums match the consolidated totals.")
    print()

# Show sample verification for first 10 students
print()
print("=" * 100)
print("SAMPLE VERIFICATION (First 10 Students):")
print("=" * 100)
print(f"{'Roll':<6} {'Name':<25} {'Org':<6} {'Clar':<6} {'Q&A':<6} {'Part':<6} {'Sum':<7} {'Total':<7} {'Match':<6}")
print("-" * 100)

for i, s in enumerate(students[:10]):
    match = "OK" if s['difference'] <= 0.01 else "FAIL"
    print(f"{s['roll']:<6} {s['name']:<25} {s['org']:<6.2f} {s['clarity']:<6.2f} {s['qa']:<6.2f} {s['participation']:<6.2f} {s['calculated']:<7.2f} {s['consolidated']:<7.2f} {match:<6}")

print()
print("=" * 100)
print("SAMPLE VERIFICATION (Last 10 Students):")
print("=" * 100)
print(f"{'Roll':<6} {'Name':<25} {'Org':<6} {'Clar':<6} {'Q&A':<6} {'Part':<6} {'Sum':<7} {'Total':<7} {'Match':<6}")
print("-" * 100)

for s in students[-10:]:
    match = "OK" if s['difference'] <= 0.01 else "FAIL"
    print(f"{s['roll']:<6} {s['name']:<25} {s['org']:<6.2f} {s['clarity']:<6.2f} {s['qa']:<6.2f} {s['participation']:<6.2f} {s['calculated']:<7.2f} {s['consolidated']:<7.2f} {match:<6}")

print()
print("=" * 100)
print("SUMMARY STATISTICS:")
print("=" * 100)
print(f"Average Consolidated Total: {sum(s['consolidated'] for s in students) / len(students):.2f}")
print(f"Highest Total: {max(s['consolidated'] for s in students):.2f} ({[s['name'] for s in students if s['consolidated'] == max(s['consolidated'] for s in students)][0]})")
print(f"Lowest Total: {min(s['consolidated'] for s in students):.2f} ({[s['name'] for s in students if s['consolidated'] == min(s['consolidated'] for s in students)][0]})")
print(f"Maximum Difference Found: {max(s['difference'] for s in students):.10f}")
print()
print("=" * 100)
