import pandas as pd
import matplotlib.pyplot as plt

data = {
    "G1": [10, 15, 12, 18, 14],
    "G2": [11, 14, 13, 17, 15],
    "sex": ["F", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)

print("Data Preview:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

print("\nAverage Grades:")
print("G1:", df["G1"].mean())
print("G2:", df["G2"].mean())

plt.hist(df["G1"], bins=5)
plt.title("Final Grades Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()

df["sex"].value_counts().plot(kind="bar")
plt.title("Students by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

