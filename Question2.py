# Import NumPy for creating and handling arrays (numerical data)
import numpy as np
# Import pyplot from Matplotlib for drawing charts; "plt" is the usual short name
import matplotlib.pyplot as plt

# Create a 2D array to store the graduate data
# Each row is one faculty, each column is one year (2022, 2023, 2024, 2025)
data = np.array([
    [120, 135, 150, 160],   # Row 0: Engineering
    [100, 110, 130, 145],   # Row 1: Business
    [80,  90,  95,  105]    # Row 2: Information Technology
])

# Years go on the x-axis. Their order matches the columns of "data"
years = np.array([2022, 2023, 2024, 2025])

# Faculty names are used as line labels. Their order matches the rows of "data"
faculties = ["Engineering", "Business", "Information Technology"]

# Loop through the faculties and their data rows together
# zip() pairs them up: ("Engineering", [120, 135, 150, 160]), and so on
for name, row in zip(faculties, data):
    # Draw one line: x = years, y = that faculty's graduates
    # marker="o" draws a circle on each data point
    # label=name stores the faculty name so the legend can show it
    plt.plot(years, row, marker="o", label=name)

# Title shown at the top of the chart
plt.title("Trend of Graduates by Faculty (2022-2025)")

# Label for the horizontal axis (what the x values mean)
plt.xlabel("Year")

# Label for the vertical axis (what the y values mean)
plt.ylabel("Number of Graduates")

# Force the x-axis ticks to be exactly our four years
# Without this, Matplotlib may show decimals such as 2022.5
plt.xticks(years)

# Show the legend box that maps each line colour to its faculty name
# title="Faculty" adds a heading inside the legend box
plt.legend(title="Faculty")

# Add grid lines in the background so values are easier to read
plt.grid(True)

# Open a window and display the finished chart
# Nothing appears on screen until this line runs
plt.show()