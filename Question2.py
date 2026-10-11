import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [120, 135, 150, 160],   # Engineering
    [100, 110, 130, 145],   # Business
    [80,  90,  95,  105]    # Information Technology
])

years = np.array([2022, 2023, 2024, 2025])
faculties = ["Engineering", "Business", "Information Technology"]

plt.title("Trend of Graduates by Faculty (2022-2025)")
plt.xlabel("Year")                  
plt.ylabel("Number of Graduates")
plt.xticks(years)
plt.legend(title="Faculty")
plt.grid(True)
plt.show()