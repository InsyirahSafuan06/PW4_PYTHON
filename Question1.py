import numpy as np

# Create a 2D array: rows = faculties, columns = years (2022-2025)
data = np.array([
    [120, 135, 150, 160],   # Engineering
    [100, 110, 130, 145],   # Business
    [80,  90,  95,  105]    # Information Technology
])

# Labels for the columns (years) and rows (faculties)
years = np.array([2022, 2023, 2024, 2025])
faculties = np.array(["Engineering", "Business", "Information Technology"])

# i. Total graduates for each faculty
# axis=1 sums across the columns (years), giving one total per row (faculty)
faculty_totals = np.sum(data, axis=1)
print("Total graduates for each faculty:", faculty_totals)

# i. Average graduates per year across all faculties
# axis=0 averages down the rows (faculties), giving one average per column (year)
yearly_avg = np.mean(data, axis=0)
print("\nAverage graduates per year across all faculties:", yearly_avg)

# ii. Faculty with the highest number of graduates in 2025
# data[:, 3] selects the 2025 column; argmax returns the row index of its largest value
index_faculty = np.argmax(data[:, 3])
print("\nHighest graduates in 2025:", faculties[index_faculty])

# ii. Year with the lowest total number of graduates
# axis=0 sums down each column, giving the total for each year
yearly_totals = np.sum(data, axis=0)
# argmin returns the index of the smallest yearly total, which maps to a year
low_year_index = np.argmin(yearly_totals)
print("Lowest total graduates:", years[low_year_index])