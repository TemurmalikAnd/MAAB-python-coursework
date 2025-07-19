import csv

# Step 1: Read the CSV and store as list of dictionaries
student_data = []
with open("grades.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert Grade to integer for later calculation
        row['Grade'] = int(row['Grade'])
        student_data.append(row)

# Step 2: Calculate average grades per subject
subject_totals = {}
subject_counts = {}

for entry in student_data:
    subject = entry['Subject']
    grade = entry['Grade']
    subject_totals[subject] = subject_totals.get(subject, 0) + grade
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

average_grades = []
for subject in subject_totals:
    avg = subject_totals[subject] / subject_counts[subject]
    average_grades.append({'Subject': subject, 'Average Grade': round(avg, 1)})

# Step 3: Write the result to average_grades.csv
with open("average_grades.csv", 'w', newline='') as file:
    fieldnames = ['Subject', 'Average Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(average_grades)
