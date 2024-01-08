import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Electric_Vehicle_Population_Data.csv"
df = pd.read_csv(file_path)

# Compute summary statistics
summary_stats = df.describe()

# Set up the visualization
plt.figure(figsize=(16, 12))
plt.subplots_adjust(top=2, bottom=1.8)
plt.suptitle("Electric Vehicle Population Data Infographic", fontsize=18)
plt.figtext(0.5, 0.02, "Student Name: Yogesh Pandit\nID Number: 22095146", ha="center", fontsize=12)

# Plot 1: Distribution of Electric Vehicle Types
plt.subplot(2, 2, 1)
sns.countplot(x="Electric Vehicle Type", data=df, palette="viridis")
plt.title("Distribution of Electric Vehicle Types")
plt.xlabel("Electric Vehicle Type")
plt.ylabel("Count")

# Plot 2: Average Electric Range by Make
plt.subplot(2, 2, 2)
sns.barplot(x="Make", y="Electric Range", data=df, errorbar=None, palette="muted")
plt.title("Average Electric Range by Make")
plt.xlabel("Make")
plt.ylabel("Average Electric Range (miles)")
plt.xticks(rotation=45, ha="right")

# Plot 3: CAFV Eligibility Proportion
plt.subplot(2, 2, 3)
df["CAFV Eligibility"] = df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].map(
    {"Clean Alternative Fuel Vehicle Eligible": "Eligible", "Not eligible due to low battery range": "Not Eligible"}
)
sns.countplot(x="CAFV Eligibility", data=df, palette="Set2")
plt.title("Proportion of CAFV Eligibility")
plt.xlabel("CAFV Eligibility")
plt.ylabel("Count")

# Plot 4: Distribution of Model Years
plt.subplot(2, 2, 4)
sns.histplot(x="Model Year", data=df, bins=20, kde=True, color="skyblue")
plt.title("Distribution of Model Years")
plt.xlabel("Model Year")
plt.ylabel("Count")

# Adjust layout
plt.tight_layout(rect=[0, 0.3, 1, 0.95])

description_text = """
Descriptions:
The figure highlights the distribution of types of electric vehicle depicts more use of battery electric in comparison of plug-in hybrid electric vehicles. 
Hence, it can be seen in the figure that a series of electric vehicle manufacturing companies are launching their electric cars in the market. 
These visualizations of electric car distributions shed lights on the optimistic growth of Electric car use by people. 
Subsequently, the electric car manufacturing industry will also flourish in the near future. Few new car manufacturing companies have got the recognition 
just like Tesla such as Wheego Electric car, Think. Likewise, it also justifies the environment friendly response even after excessive use of electric cars.  
In addition, fulfillment of CAFV eligibility criteria by electric cars inspire the governmental bodies to support these manufacturing companies.
"""

plt.figtext(0.5, 0.06, description_text, ha="center", fontsize=12)

# Save the infographic as a PNG file
plt.savefig("22095146.png", dpi=300)

# # Display the infographic
# plt.show()

# # Display summary statistics
# print("Summary Statistics:")
# print(summary_stats)
