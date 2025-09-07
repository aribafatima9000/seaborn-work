import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# =======================
# Step 1: Sample Data
# =======================
data = {
    "Name": ["Ali", "Sara", "Ayesha", "Bilal", "Usman", "Hina", "Zara", "Omar"],
    "Math": [78, 55, 89, 92, 40, 65, 72, 88],
    "Science": [88, 72, 95, 60, 50, 70, 85, 90],
    "English": [90, 65, 85, 70, 45, 75, 80, 95],
    "Computer": [95, 80, 90, 75, 60, 85, 92, 98]
}
df = pd.DataFrame(data)

print("📌 Student Marks Data:")
print(df)

# =======================
# Step 2: Bar Plot
# =======================
plt.figure(figsize=(8,5))
sns.barplot(x="Name", y="Math", data=df)
plt.title("📊 Math Marks of Students")
plt.show()

# =======================
# Step 3: Scatter Plot
# =======================
plt.figure(figsize=(8,5))
sns.scatterplot(x="Math", y="Science", data=df, hue="Name", s=100)
plt.title("🔍 Math vs Science Marks")
plt.show()

# =======================
# Step 4: Box Plot
# =======================
plt.figure(figsize=(8,5))
sns.boxplot(data=df[["Math","Science","English","Computer"]])
plt.title("📦 Marks Distribution by Subject")
plt.show()

# =======================
# Step 5: Heatmap
# =======================
plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English","Computer"]].corr(), annot=True, cmap="coolwarm")
plt.title("🔥 Correlation Between Subjects")
plt.show()
