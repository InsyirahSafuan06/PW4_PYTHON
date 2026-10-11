import numpy as np

# 1. 2D array: rows = faculties, columns = years
data = np.array([
    [120, 135, 150, 160],   # Engineering
    [100, 110, 130, 145],   # Business
    [80,  90,  95,  105]    # Information Technology
])

years = np.array([2022, 2023, 2024, 2025])
faculties = np.array(["Engineering", "Business", "Information Technology"])

# i. Total graduates for each faculty
faculty_totals = np.sum(data, axis=1)
print("Total graduates for each faculty:", faculty_totals)

# i. Average graduates per year across all faculties
yearly_avg = np.mean(data, axis=1)
print("\nAverage graduates per year across all faculties:", yearly_avg)

# ii. Faculty with the highest number of graduates in 2025
index_faculty = np.argmax(data[:, 3]) 
print("\nHighest graduates in 2025: ",(faculties[index_faculty]))

# ii. Year with the lowest total number of graduates
yearly_totals = np.sum(data, axis=0)
low_year_index = np.argmin(yearly_totals)
print("Lowest total graduates: ",(years[low_year_index]) )
     