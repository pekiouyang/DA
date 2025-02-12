import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Sample_Data_for_Activity.csv"  # Update with the correct file path
df = pd.read_csv(file_path)

# Set the style
sns.set_style("whitegrid")

# Create the displot for the "Normal_Distribution" column
plt.figure(figsize=(8, 5))
sns.histplot(df["Normal_Distribution"], kde=True, bins=30, color="blue")

# Labels and title
plt.xlabel("Value", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution Plot of Normal_Distribution", fontsize=14)

# Show plot
plt.show()