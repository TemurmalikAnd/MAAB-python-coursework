universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities_list):
    """Returns two lists: enrollment numbers and tuition fees"""
    enrollments = []
    tuitions = []
    
    for university in universities_list:
        enrollments.append(university[1])  # student count
        tuitions.append(university[2])     # tuition fee
    
    return enrollments, tuitions

def mean(values_list):
    """Calculates and returns the mean of a list of numbers"""
    return sum(values_list) / len(values_list)

def median(values_list):
    """Calculates and returns the median of a list of numbers"""
    sorted_values = sorted(values_list)
    n = len(sorted_values)
    
    if n % 2 == 0:
        # Even number of values - average of two middle values
        median_val = (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
    else:
        # Odd number of values - middle value
        median_val = sorted_values[n//2]
    
    return median_val

# Main program
print('******************************')

# Get enrollment and tuition data
enrollments, tuitions = enrollment_stats(universities)

# Calculate totals
total_students = sum(enrollments)
total_tuition = sum(tuitions)

# Calculate means and medians
student_mean = mean(enrollments)
student_median = median(enrollments)
tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

# Display results
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")

print('******************************')