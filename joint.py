import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Sample_Data_for_Activity.csv"  # Update with the correct file path
df = pd.read_csv(file_path)

# Create a jointplot for Normal_Distribution vs Uniform_Distribution
sns.jointplot(
    data=df,
    x="Normal_Distribution",
    y="Uniform_Distribution",
    kind="scatter",  # Options: "scatter", "kde", "hex", "hist", "reg"
    color="blue"
)

# Show the plot
plt.show()